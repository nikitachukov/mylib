import zipfile
from lxml import etree
import os
from pprint import pprint
import hashlib


def parse_epub(filename):
    try:
        result = {'filename': os.path.basename(filename),
                  'md5': hashlib.md5(open(filename, 'rb').read()).hexdigest().upper()}
        zip = zipfile.ZipFile(filename, 'r')
        # container_before_transfomation =
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
        container = transform(etree.XML(zip.read('META-INF/container.xml')))
        rootfile_location = container.xpath('/container/rootfiles/rootfile/')[0].get('full-path')
        rootfile = transform(etree.XML(zip.read(rootfile_location)))

        for tag in ['title', 'language', 'creator', 'date', 'identifier', 'description']:
            try:
                result[tag] = str(rootfile.xpath('/package/metadata/%s/text()' % tag)[0])
            except IndexError:
                result[tag] = None
                continue

        try:
            result['cover_filename'] = rootfile.xpath('/package/manifest/item[@id="%s"]' % (rootfile.xpath('/package/metadata/meta[@name="cover"]')[0].get('content')))[0].get('href')

            for zipdir in list(set([('/'.join(filename.split('/')[:-1])) for filename in zip.namelist()])):
                try:
                    if not zipdir:
                        cover_file = zip.read(result['cover_filename'])

                    else:
                        cover_file = zip.read(zipdir + '/' + result['cover_filename'])

                    result['new_cover_filename'] = os.path.join('D:\\test_cases\\epub', result['md5'] +
                                                                os.path.splitext(result['cover_filename'])[1])
                    with open(result['new_cover_filename'], 'wb') as f:
                        f.write(cover_file)
                    break
                except:
                    continue
        except:
            pass

        return result
    except zipfile.BadZipfile as E:
        print(E)
        return


if __name__ == '__main__':

    for root, dirs, files in os.walk("D:\\test"):
        for file in files:
            if file.endswith(".epub"):
                pprint(parse_epub(filename=os.path.join(root, file)))