#
#  test_pyshogi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class KomaTestCase:
    def test_masu(self):
        masu = apply(self.ban.masu, self.masume)
        self.assertEqual(masu.koma, self.koma)
        self.assertEqual(self.koma.masu, masu)

    def test_ugoki(self):
        ugoki = self.koma.ugoki()

        self.assertIsInstance(ugoki, dict)
        self.assertEqual(len(ugoki), len(self.ugoki))

        for (x, y), narikomi in self.ugoki:
            masu = self.ban.masu(x, y)
            self.assertIn(masu, ugoki)
            self.assertEqual(ugoki[masu], narikomi)

    def test_move(self):
        for (x, y), narikomis in self.ugoki:
            if narikomis is None:
                self.setUp()
                old_masu = self.koma.masu
                masu = self.ban.masu(x, y)
                self.koma.move(masu)
                self.assertEqual(masu.koma, self.koma)
                self.assertEqual(self.koma.masu, masu)
                self.assertFalse(self.koma.narikoma)
                self.assertIsNone(old_masu.koma)
            else:
                for narikomi in narikomis:
                    self.setUp()
                    old_masu = self.koma.masu
                    masu = self.ban.masu(x, y)
                    self.koma.move(masu, narikomi)
                    self.assertEqual(masu.koma, self.koma)
                    self.assertEqual(self.koma.masu, masu)
                    self.assertEqual(self.koma.narikoma, narikomi)
                    self.assertIsNone(old_masu.koma)

    def test_move_error(self):
        for x in range(9):
            for y in range(9):
                if x <> 4 and y <> 3:
                    with self.assertRaises(pyshogi.CanNotPlaceKomaError):
                        self.koma.move(self.ban.masu(x, y))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(-1, -1))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(9, 9))

class SenteKomaCenterTestCase(unittest.TestCase, KomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 3), None)]

class SenteKomaNaruTestCase(unittest.TestCase, KomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 2), [False, True])]

class GoteKomaCenterTestCase(unittest.TestCase, KomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 5), None)]

class GoteKomaNaruTestCase(unittest.TestCase, KomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 6), [False, True])]

if __name__ == '__main__': unittest.main()
