#
#  test_pyshogi_mochi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012-2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class MochiKomaTestCase:
    def test_ugoki(self):
        self.ban.teban = self.koma.sengo
        self.assertEqual(
            dict([(masu, self.koma.narikomi(masu)) for masu in self.koma.ugoki()]),
            self.ugoki
        )

    def test_move(self):
        for m in self.ugoki.keys():
            self.setUp()
            masu = self.ban.masu(m.x, m.y)

            self.assertEqual(masu.koma, None)
            self.assertEqual(self.koma.masu, None)

            self.ban.teban = self.koma.sengo
            self.koma.move(m.x, m.y)

            self.assertEqual(masu.koma, self.koma)
            self.assertEqual(self.koma.masu, masu)
            self.assertEqual([], self.ban.mochigoma(0))
            self.assertEqual([], self.ban.mochigoma(1))

    def test_move_error(self):
        ugokis = frozenset(self.ban).difference(frozenset(self.ugoki.keys()))
        for m in ugokis:
            self.setUp()
            masu = self.ban.masu(m.x, m.y)

            self.assertEqual(masu.koma, None)
            self.assertEqual(self.koma.masu, None)

            self.ban.teban = self.koma.sengo
            with self.assertRaises(pyshogi.CanNotPlaceKomaError):
                self.koma.move(m.x, m.y)

### Fu
class SenteFu_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban  = pyshogi.ShogiBan([0, [(0, Fu, None, 0)]])
        self.koma = self.ban.mochigoma(0)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteFu_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban  = pyshogi.ShogiBan([0, [(1, Fu, None, 0)]])
        self.koma = self.ban.mochigoma(1)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Kyosya
class SenteKyosya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban  = pyshogi.ShogiBan([0, [(0, Kyosya, None, 0)]])
        self.koma = self.ban.mochigoma(0)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteKyosya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban  = pyshogi.ShogiBan([0, [(1, Kyosya, None, 0)]])
        self.koma = self.ban.mochigoma(1)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Keima
class SenteKeima_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban  = pyshogi.ShogiBan([0, [(0, Keima, None, 0)]])
        self.koma = self.ban.mochigoma(0)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
            masus.remove(self.ban.masu(x, 1))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteKeima_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(1, Keima, None, 0)]])
        self.koma  = self.ban.mochigoma(1)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 7))
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Gin
class SenteGin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(0, Gin, None, 0)]])
        self.koma  = self.ban.mochigoma(0)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteGin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(1, Gin, None, 0)]])
        self.koma  = self.ban.mochigoma(1)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Kin
class SenteKin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(0, Kin, None, 0)]])
        self.koma  = self.ban.mochigoma(0)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteKin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(1, Kin, None, 0)]])
        self.koma  = self.ban.mochigoma(1)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Kaku
class SenteKaku_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(0, Kaku, None, 0)]])
        self.koma  = self.ban.mochigoma(0)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteKaku_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(1, Kaku, None, 0)]])
        self.koma  = self.ban.mochigoma(1)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Hisya
class SenteHisya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(0, Hisya, None, 0)]])
        self.koma  = self.ban.mochigoma(0)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteHisya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.ShogiBan([0, [(1, Hisya, None, 0)]])
        self.koma  = self.ban.mochigoma(1)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

if __name__ == '__main__': unittest.main()
