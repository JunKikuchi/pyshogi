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
        (True,  'Fu', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Fu)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Kyosya', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kyosya)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Keima', (4, 4))
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Keima)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Gin', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Gin)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Kin', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kin)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Kaku', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Kaku)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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
        (True, 'Hisya', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Hisya)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

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

class SenteGyokuTestCase(unittest.TestCase):
    BAN = [
        (True, 'Gyoku', (4, 4)),
    ]

    def setUp(self):
        self.ban  = pyshogi.Ban(self.BAN)
        self.koma = self.ban.masu(4, 4).koma

    def test_koma(self):
        self.assertIsInstance(self.koma, pyshogi.Gyoku)
        self.assertIsNotNone(self.koma.masu)
        self.assertFalse(self.koma.narikoma)

    def test_movables(self):
        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                self.ban.masu(5, 5), self.ban.masu(4, 5), self.ban.masu(3, 5),
            ]))

    def test_narikoma_movables(self):
        self.koma.naru()

        self.assertEqual(
            self.koma.movables(),
            frozenset([
                self.ban.masu(5, 3), self.ban.masu(4, 3), self.ban.masu(3, 3),
                self.ban.masu(5, 4),                      self.ban.masu(3, 4),
                self.ban.masu(5, 5), self.ban.masu(4, 5), self.ban.masu(3, 5),
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

        for sente, koma, (x, y) in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__.__name__, koma)

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

        for sente, koma, (x, y) in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertNotEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__.__name__, koma)

            if y < 3:
                self.assertTrue(masu.koma.sente)
            else:
                self.assertFalse(masu.koma.sente)

if __name__ == '__main__': unittest.main()
