
import zipfile
from lxml import etree

def pase_epub(filename):
    z = zipfile.ZipFile( filename, 'r')
    content= z.read('OPS/toc.ncx')

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
    print (dom.xpath('/ncx/docTitle/text/text()'))
    print (dom.xpath('/ncx/docAuthor/text/text()'))

if __name__ == '__main__':
    pase_epub(filename='/tmp/django.epub')