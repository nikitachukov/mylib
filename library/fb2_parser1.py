# -*- coding: utf-8 -*-
__author__ = 'nikitos'

import os
import hashlib
from pprint import pprint
import traceback
from lxml import etree

def find_files_by_mask(location, mask):
    find_files = []
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(mask):
                find_files += [[os.path.join(root, file),
                                hashlib.md5(open(os.path.join(root, file), 'rb').read()).hexdigest().upper()]]
    return find_files

def check_file_md5(md5):
    if md5 in ['7B0BB8B28BAA7C9655D75886132CB7BE', '0F19F5D897E468587734CD5A23D5287A']:
        return False
    else:
        return True


def parser(files):
    Books = []
    Doubles = []
    Errors = []

    for file in files[:]:
        if check_file_md5(file[1]):
            try:
                parser = etree.XMLParser(recover=True)
                xmlfile = etree.parse(file[0], parser)
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
                book = transform(xmlfile)
                description = book.getroot().find("description/")

                print(file[0])
                print(book.xpath('/FictionBook/description/title-info/genre/text()'))
                print(book.xpath('/FictionBook/description/title-info/book-title/text()'))
                # print(book.xpath('/FictionBook/description/title-info/annotation/p/text()'))
                # [0].get('text')


                nodes = book.xpath('/FictionBook/description/title-info/annotation'
                                   '') # Открываем раздел
                for node in nodes: # Перебираем элементы
                    # print (node.tag,node.keys(),node.values())
                    print( 'text =',[node.text]) # Выводим текст элемента

            except Exception as E:
                Errors.append({'filename': file[0], 'md5': file[1]})
                print(traceback.format_exc())
        else:
            Doubles.append({'filename': file[0], 'md5': file[1]})

    return Books, Doubles, Errors





if __name__=='__main__':
    files = find_files_by_mask('/home/nikitos/media/books/test/', ".fb2")[:1]
    parser(files)


    from pprint import pprint

    # Books, Doubles, Errors = parse_files(files[:1],'D:\\media\\')