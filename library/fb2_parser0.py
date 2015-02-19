#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ChukovNA'
import os,sys
import hashlib
from lxml import etree
import base64
import traceback
import shutil

from django.conf import settings


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


def parse_files(files,media_root):
    ns = "{http://www.gribuser.ru/xml/fictionbook/2.0}"
    Books = []
    Doubles = []
    Errors = []

    for file in files[:]:
        if check_file_md5(file[1]):

            try:
                parser = etree.XMLParser(recover=True)
                book = etree.parse(file[0], parser)
                Authors = []
                Book = {}
                Annotation = ""
                Genre = []

                description = book.getroot().find(ns + "description/")

                Book = {"md5": file[1], 'filename': os.path.basename((file[0]))}

                for title in description.findall(ns + "book-title"):
                    Book["title"] = title.text

                for genre in description.findall(ns + "genre"):
                    Genre += [genre.text]
                    Book["Genre"] = Genre

                for annotation in description.findall(ns + "annotation"):
                    for child in annotation:
                        if (child is not None) and child.text:
                            Annotation += child.text
                            Book["Annotation"] = Annotation

                for cover in description.findall(ns + "coverpage"):
                    for child in cover:
                        if (child is not None):
                            binary = book.getroot().find(ns + "binary")
                            if (binary.attrib['id'] ==
                                    child.attrib.get('{http://www.w3.org/1999/xlink}href')[1:]):
                                print(os.path.join(media_root, 'covers'))
                                covers_store_path = os.path.join(media_root, 'covers')
                                # covers_store_path='/home/nikitos/books/covers'

                                if not os.path.exists(covers_store_path):
                                    os.makedirs(covers_store_path)
                                with open(os.path.join(covers_store_path,
                                                       file[1] + os.path.splitext(binary.attrib['id'])[1]), 'wb') as f:
                                    f.write(base64.b64decode(binary.text))
                                    f.close()
                                    Book['cover_file_name'] = os.path.join(covers_store_path, file[1] +
                                                                           os.path.splitext(binary.attrib['id'])[1])

                for author in description.findall(ns + "author"):
                    Author = {}
                    author_first_name = author.find(ns + "first-name")

                    if author_first_name is not None:
                        Author['author_first_name'] = author_first_name.text.strip()
                    author_last_name = author.find(ns + "last-name")
                    if author_last_name is not None:
                        Author['author_last_name'] = author_last_name.text.strip()
                    author_middle_name = author.find(ns + "middle-name")

                    if author_middle_name is not None:
                        Author['author_middle_name'] = author_middle_name.text.strip()

                    if Author:
                        Authors.append(Author)
                        Book["Authors"] = Authors


                Book['new_file_name']=os.path.join(media_root, 'books',Book['md5']+'.fb2')
                shutil.copyfile(file[0],Book['new_file_name'])
                # if  settings.DEBUG:
                #     book['new_file_name']=

                    # print(file[0])

                Books.append(Book)
            except Exception as E:
                Errors.append({'filename': file[0], 'md5': file[1]})
                print(traceback.format_exc())




        else:
            Doubles.append({'filename': file[0], 'md5': file[1]})
            # todo: repeat action
    return Books, Doubles, Errors


def main():
    path = 'D:/media/import/'

    files = find_files_by_mask(path, ".fb2")


    from pprint import pprint

    # Books, Doubles, Errors = parse_files(files[:1],'D:\\media\\')
    #
    # pprint(Books)
    # pprint()


if __name__ == "__main__":
    main()


