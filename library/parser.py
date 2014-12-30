#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import hashlib
from lxml import etree

__author__ = 'ChukovNA'


def find_files_by_mask(location, mask):
    find_files = []
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(mask):
                find_files += [[os.path.join(root, file),
                                hashlib.md5(open(os.path.join(root, file), 'rb').read()).hexdigest().upper()]]
    print(location, mask)
    return find_files


def check_file_md5(md5):
    return True


def parse_files(files):
    ns = "{http://www.gribuser.ru/xml/fictionbook/2.0}"
    Books = []

    for file in files[:]:
        # print(file[0])
        if check_file_md5(file[1]):
            try:
                parser = etree.XMLParser(recover=True)
                book = etree.parse(file[0], parser)
                Authors = []
                Book = {}
                Annotation = ""
                Genre = []

                description = book.getroot().find(ns + "description/")

                Book = {"md5": file[1]}

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
                Books.append(Book)
            except Exception as E:
                print(E)


        else:
            print("re")
            # todo: repeat action
    return Books


def main():
    import platform

    if platform.node().upper() == "LENOVO":
        path = "/home/nikitos/Downloads/S.T.A.L.K.E.R__[rutracker.org]/"
    else:
        path = "c:\\Downloads\\S.T.A.L.K.E.R__[rutracker.org]"

    files = find_files_by_mask(path, ".fb2")
    # print(parse_files(files))

    for book in parse_files(files):
        if 'Authors' in book.keys():
            print(book['Authors'])


if __name__ == "__main__":
    main()


