#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ChukovNA'
from  library.epub_parser0 import parse_epub



import unittest


def foo(par):
    return par


class Test(unittest.TestCase):
    def test1(self):

        result={'date': '2012',
             'cover_filename': 'images/cover.jpg',
             'identifier': 'urn:uuid:094ba05b-3368-45e0-9892-e39380ded1c3',
             'language': 'ru', 'md5': '35BB8F7439350CB39AA6801D719F12A2',
             'description': 'Ночной дозор, Дневной, Сумеречный и, наконец. Последний. Все? Существует ли конец Пути? Нет! Читайте «Новый Дозор»!!! ',
             'title': 'Новый Дозор',
             'creator': 'Сергей Васильевич Лукьяненко'}


        self.res=parse_epub('d:\\test_cases\epub\\01.epub')
        self.assertEqual(self.res, result)

    def test2(self):

        # result={'date': '2012',
        #      'cover_filename': 'cover.jpg',
        #      'identifier': 'urn:uuid:2A1C46FA-5617-4EBE-BC2D-B6174BE9DE68',
        #      'language': 'ru',
        #      'md5': 'A12F2637DA1A05661BC4366CA0A155E9',
        #      'description': 'Человечество, некогда освоившее тысячи миров, а затем отброшенное в каменный век, снова поднимает голову. Будущее планеты зависит теперь от юноши по имени Маттер, на плечи которого неожиданно обрушилась величайшая ответственность. Он стал Посредником, одним из трех людей, связанных с иными обитателями Космоса. Реки крови и множество нелегких дорог приходится преодолеть ему в поисках хрустального Черепа, изготовленного в незапамятные времена Владыками Неба. В чужих руках этот загадочный артефакт может погубить Вселенную…',
        #      'title': 'Черный хрусталь',
        #      'creator': 'Алексей Игоревич Бессонов'}
        #
        result={'language': 'ru',
                'cover_filename': 'cover.jpg',
                'date': '0101-01-01T00:00:00+00:00',
                'creator': 'Алексей Игоревич Бессонов',
                'identifier': 'urn:uuid:2A1C46FA-5617-4EBE-BC2D-B6174BE9DE68',
                'md5': 'A12F2637DA1A05661BC4366CA0A155E9',
                'description': 'Человечество, некогда освоившее тысячи миров, а затем отброшенное в каменный век, снова поднимает голову. Будущее планеты зависит теперь от юноши по имени Маттер, на плечи которого неожиданно обрушилась величайшая ответственность. Он стал Посредником, одним из трех людей, связанных с иными обитателями Космоса. Реки крови и множество нелегких дорог приходится преодолеть ему в поисках хрустального Черепа, изготовленного в незапамятные времена Владыками Неба. В чужих руках этот загадочный артефакт может погубить Вселенную…',
                'title': 'Черный хрусталь'}


        self.res=parse_epub('d:\\test_cases\epub\\02.epub')
        self.assertEqual(self.res, result)

        #
        # return parse_epub('d:\\test_cases\epub\\01.epub')
        #
        # self.assertEqual('d:\\test_cases\epub\\01.epub',result)
        # # ...а это -- сохраненное значение
        # # self.assertEqual(inc(0), 8)

if __name__ == '__main__':
    unittest.main()