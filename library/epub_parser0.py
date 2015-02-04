
import zipfile
from lxml import etree
import os
from pprint import pprint
def pase_epub(filename):
    try:
        try:
            z = zipfile.ZipFile( filename, 'r')
            content= z.read('META-INF/container.xml')
            xslt=b'''\
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
            transform=etree.XSLT(etree.XML(xslt))
            dom=transform(etree.XML(content))
            rootfile_location=dom.xpath('/container/rootfiles/rootfile')[0].get('full-path')

            # print(rootfile_location)

            content= z.read(rootfile_location)
            dom=transform(etree.XML(content))

            # print(etree.tostring(dom, pretty_print=True))
            # print('*'*80)
            # print(dom.xpath('/package/metadata/title/text()')[0])
            # print(dom.xpath('/package/metadata/creator/text()'))
            # print(dom.xpath('/package/metadata/language/text()')[0])
            # print(tree.xpath('/soft/os/item[@name="linux"]')[0].get('dist'))
            # cover=

            # print(cover)
            cover_filename=dom.xpath('/package/manifest/item[@id="%s"]'%(dom.xpath('/package/metadata/meta[@name="cover"]')[0].get('content')))[0].get('href')
            print(cover_filename)
            print('*'*80)
            try:
                z.extract(cover_filename,'d:/test/')
            except KeyError as E:
                for dir in set([('/'.join(filename.split('/')[:-1])) for filename  in z.namelist()]):
                    try:
                        coverfile=z.read('/'.join([dir,cover_filename]))
                        print(len(cover_filename))
                    except KeyError:
                        pass
                    except Exception as E:
                        print(E)





            except Exception as E:
                print(E)
        except Exception as E:
                print(E)
                return None


    except  Exception as E:
        print(E)
        return None



if __name__ == '__main__':

    for root, dirs, files in os.walk("d://test/"):
        for file in files:
            if file.endswith(".epub"):
                print('*'*80)
                print(os.path.join(root, file))
                pase_epub(filename=os.path.join(root, file))
    # pase_epub(filename="D:\\test.epub")
    # pase_epub(filename="d:\Dropbox\\books\epub\djobs_bio.epub")