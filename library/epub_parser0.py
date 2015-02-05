import zipfile
from lxml import etree
import os
from pprint import pprint
import hashlib


def pase_epub(filename):
    try:
        res = {'filename': os.path.basename(filename)}
        res = {'md5': hashlib.md5(open(filename, 'rb').read()).hexdigest().upper()}
        zip = zipfile.ZipFile(filename, 'r')
        container_before_transfomation = zip.read('META-INF/container.xml')
        xslt = b'''\
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="no"/>

    <xsl:template match="/|comment()|processing-instruction()">
        <xsl:copy>
          <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="*">
        <xsl:element name="{local-name()}">
          <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:attribute name="{local-name()}">
          <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    </xsl:stylesheet>
    '''
        transform = etree.XSLT(etree.XML(xslt))
        container = transform(etree.XML(container_before_transfomation))
        rootfile_location = container.xpath('/container/rootfiles/rootfile')[0].get('full-path')
        rootfile_before_transformation = zip.read(rootfile_location)
        rootfile = transform(etree.XML(rootfile_before_transformation))

        for s in ['title', 'language', 'creator', 'date', 'identifier', 'description']:
            try:
                res[s] = str(rootfile.xpath('/package/metadata/%s/text()' % s)[0])
            except IndexError:
                res[s] = None
                continue
        try:
            res['cover_filename'] = rootfile.xpath('/package/manifest/item[@id="%s"]' %
                                                   (rootfile.xpath('/package/metadata/meta[@name="cover"]')
                                                    [0].get('content')))[0].get('href')

            try:
                for inzip_dir in (list(set([('/'.join(filename.split('/')[:-1])) for filename in zip.namelist()]))):
                    candidate = os.path.join('', *[inzip_dir, os.path.basename(res['cover_filename'])])
                    try:
                        cover_file = zip.read(candidate)
                        if cover_file:
                            new_cover_filename = os.path.join('/tmp/test',res['md5']+os.path.splitext(res['cover_filename'])[1])
                            with open(new_cover_filename ,'wb') as f:
                                f.write(cover_file)
                            res['new_cover_filename']=new_cover_filename
                    except:
                        continue
            except:
                res['cover_filename'] = None
                res['new_cover_filename'] = None

            return res
        except:
            pass
        return res
    except zipfile.BadZipfile as E:
        print(E)
        return


if __name__ == '__main__':

    for root, dirs, files in os.walk("/tmp/test/"):
        for file in files:
            if file.endswith(".epub"):

                x=pase_epub(filename=os.path.join(root, file))
                y=[]
                for tag in ['title','md5','new_cover_filename','cover_filename']:
                    y.append(x[tag])
                print(y)



                # pase_epub(filename="D:\\test.epub")
                # pase_epub(filename="d:\Dropbox\\books\epub\djobs_bio.epub")