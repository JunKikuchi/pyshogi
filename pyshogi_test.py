#
#  pyshogi_test.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class SenteFuTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Fu, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Fu)

    def test_movables(self):
        self.assertEqual(self.koma.movables(), frozenset([self.ban.masu(4, 3)]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

class SenteKyosyaTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Kyosya, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kyosya)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(4, 3),
                self.ban.masu(4, 2),
                self.ban.masu(4, 1),
                self.ban.masu(4, 0),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

class SenteKeimaTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Keima, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Keima)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 2),
                self.ban.masu(3, 2),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

class SenteGinTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Gin, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Gin)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),

                self.ban.masu(5, 5),                      self.ban.masu(3, 5),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

class SenteKinTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Kin, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kin)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                                     self.ban.masu(4, 5),
            ]))

class SenteKakuTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Kaku, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kaku)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(8, 0),                      self.ban.masu(0, 0),
                self.ban.masu(7, 1),                      self.ban.masu(1, 1),
                self.ban.masu(6, 2),                      self.ban.masu(2, 2),
                self.ban.masu(5, 3),                      self.ban.masu(3, 3),

                self.ban.masu(5, 5),                      self.ban.masu(3, 5),
                self.ban.masu(6, 6),                      self.ban.masu(2, 6),
                self.ban.masu(7, 7),                      self.ban.masu(1, 7),
                self.ban.masu(8, 8),                      self.ban.masu(0, 8),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(8, 0),                      self.ban.masu(0, 0),
                self.ban.masu(7, 1),                      self.ban.masu(1, 1),
                self.ban.masu(6, 2),                      self.ban.masu(2, 2),
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                self.ban.masu(5, 5), self.ban.masu(4, 5), self.ban.masu(3, 5),
                self.ban.masu(6, 6),                      self.ban.masu(2, 6),
                self.ban.masu(7, 7),                      self.ban.masu(1, 7),
                self.ban.masu(8, 8),                      self.ban.masu(0, 8),
            ]))

class SenteHisyaTestCase(unittest.TestCase):
    BAN = [
        ((4, 4), pyshogi.Hisya, True),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Hisya)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                                     self.ban.masu(4, 0),
                                     self.ban.masu(4, 1),
                                     self.ban.masu(4, 2),
                                     self.ban.masu(4, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                self.ban.masu(6, 4),                      self.ban.masu(2, 4),
                self.ban.masu(7, 4),                      self.ban.masu(1, 4),
                self.ban.masu(8, 4),                      self.ban.masu(0, 4),
                                     self.ban.masu(4, 5),
                                     self.ban.masu(4, 6),
                                     self.ban.masu(4, 7),
                                     self.ban.masu(4, 8),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                                     self.ban.masu(4, 0),
                                     self.ban.masu(4, 1),
                                     self.ban.masu(4, 2),
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                self.ban.masu(6, 4),                      self.ban.masu(2, 4),
                self.ban.masu(7, 4),                      self.ban.masu(1, 4),
                self.ban.masu(8, 4),                      self.ban.masu(0, 4),
                self.ban.masu(5, 5), self.ban.masu(4, 5), self.ban.masu(3, 5),
                                     self.ban.masu(4, 6),
                                     self.ban.masu(4, 7),
                                     self.ban.masu(4, 8),
            ]))

class HirateBanTestCase(unittest.TestCase):
    def setUp(self):
        self.ban = pyshogi.Ban()

    def test_size(self):
        self.assertEqual(len(self.ban.masus), 9)
        for xs in self.ban.masus:
            self.assertEqual(len(xs), 9)

    def test_masus(self):
        for masu in self.ban:
            self.assertIsInstance(masu, pyshogi.Masu)

        for x in range(0, 9):
            for y in range(0, 9):
                masu = self.ban.masu(x, y)
                self.assertIsInstance(masu, pyshogi.Masu)

        for x, y in [(-1, -1), (-1, 0), (0, -1), (-1, 9), (-1, 8), (0, 9), (9, 9), (9, -1)]:
            masu = self.ban.masu(x, y)
            self.assertIsNone(masu)

    def test_komas(self):
        self.assertEqual(len(self.ban.komas), 9 * 4 + 4)

        for koma in self.ban.komas:
            self.assertIsInstance(koma, pyshogi.Koma)
            self.assertIsInstance(koma.masu, pyshogi.Masu)

            masu = self.ban.masu(koma.masu.x, koma.masu.y)
            self.assertEqual(koma.masu, masu)

            if koma.masu.y < 3:
                self.assertFalse(koma.sente)
            else:
                self.assertTrue(koma.sente)

        for (x, y), koma, sente in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__, koma)

            if y < 3:
                self.assertFalse(masu.koma.sente)
            else:
                self.assertTrue(masu.koma.sente)

    def test_round(self):
        self.ban.round()

        self.assertEqual(len(self.ban.komas), 9 * 4 + 4)

        for koma in self.ban.komas:
            self.assertIsInstance(koma, pyshogi.Koma)
            self.assertIsInstance(koma.masu, pyshogi.Masu)

            masu = self.ban.masu(koma.masu.x, koma.masu.y)
            self.assertEqual(koma.masu, masu)

            if koma.masu.y < 3:
                self.assertTrue(koma.sente)
            else:
                self.assertFalse(koma.sente)

        for (x, y), koma, sente in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertNotEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__, koma)

            if y < 3:
                self.assertTrue(masu.koma.sente)
            else:
                self.assertFalse(masu.koma.sente)

if __name__ == '__main__': unittest.main()
