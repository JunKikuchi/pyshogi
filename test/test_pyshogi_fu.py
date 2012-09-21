#
#  test_pyshogi_fu.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class FuTestCase:
    def test_masu(self):
        masu = self.ban.masu(4, 4)
        self.assertEqual(masu.koma, self.koma)
        self.assertEqual(self.koma.masu, masu)

    def test_move(self):
        masu = self.ban.masu(4, 3)
        self.koma.move(masu)
        self.assertEqual(masu.koma, self.koma)
        self.assertEqual(self.koma.masu, masu)

        self.assertIsNone(self.ban.masu(4, 4).koma)

    def test_move_naru(self):
        pass

    def test_move_error(self):
        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(5, 3))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(3, 3))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(5, 4))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(3, 4))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(3, 5))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(4, 5))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(5, 5))

    def test_movables(self):
        pass

class SenteFuTestCase(unittest.TestCase, FuTestCase):
    def setUp(self):
        self.ban  = pyshogi.Ban([(True, 'Fu', (4, 4))])
        self.koma = self.ban.masu(4, 4).koma

class GoteFuTestCase(unittest.TestCase, FuTestCase):
    def setUp(self):
        self.ban  = pyshogi.Ban([(True, 'Fu', (4, 4))])
        self.koma = self.ban.masu(4, 4).koma

if __name__ == '__main__': unittest.main()
