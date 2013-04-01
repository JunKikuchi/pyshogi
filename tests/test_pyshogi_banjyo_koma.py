#
#  test_pyshogi_banjyo_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class BanjyoKomaTestCase:
    def test_masu(self):
        masu = apply(self.ban.masu, self.masume)
        self.assertEqual(masu.koma, self.koma)
        self.assertEqual(self.koma.masu, masu)

    def test_ugoki(self):
        self.ban.teban = self.koma.sengo

        ugoki = self.koma.ugoki()

        self.assertIsInstance(ugoki, frozenset)
        self.assertEqual(len(ugoki), len(self.ugoki))

        for (x, y), narikomi in self.ugoki:
            masu = self.ban.masu(x, y)
            self.assertIn(masu, ugoki)
            self.assertEqual(self.koma.narikomi(masu), narikomi)

    def test_idou(self):
        for (x, y), narikomi in self.ugoki:
            if narikomi is None:
                self.setUp()
                old_masu = self.koma.masu
                masu = self.ban.masu(x, y)
                self.ban.teban = self.koma.sengo
                self.koma.idou(x, y)
                self.assertEqual(masu.koma, self.koma)
                self.assertEqual(self.koma.masu, masu)
                self.assertIsNone(old_masu.koma)
            else:
                for nari in narikomi:
                    self.setUp()
                    old_masu = self.koma.masu
                    masu = self.ban.masu(x, y)
                    self.ban.teban = self.koma.sengo
                    self.koma.idou(x, y, nari)
                    self.assertEqual(masu.koma, self.koma)
                    self.assertEqual(self.koma.masu, masu)
                    self.assertEqual(self.koma.nari, nari)
                    self.assertIsNone(old_masu.koma)

    def test_idou_error(self):
        ugoki = frozenset([
            apply(self.ban.masu, masume) for masume, narikomi in self.ugoki])

        for x in range(9):
            for y in range(9):
                masu = self.ban.masu(x, y)
                if masu not in ugoki:
                    self.ban.teban = self.koma.sengo
                    with self.assertRaises(pyshogi.CanNotPlaceKomaError):
                        self.koma.idou(x, y)

        self.ban.teban = self.koma.sengo
        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.idou(-1, -1)

        self.ban.teban = self.koma.sengo
        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.idou(9, 9)


### Fu
class SenteFu44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 3), None)]

class SenteFu44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteFu80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteFu70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteFu10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteFu00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class SenteFu43F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 2), [False, True])]

class SenteFu41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Shogiban([0, [(0, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 0), [True])]

class GoteFu44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 5), None)]

class GoteFu44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteFu88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteFu78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteFu18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteFu08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]

class GoteFu45F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 6), [False, True])]

class GoteFu47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Shogiban([0, [(1, Fu, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 8), [True])]


# Kyosya
class SenteKyosya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 3), None),
                        ((4, 2), [False, True]),
                        ((4, 1), [False, True]),
                        ((4, 0), [True])
                      ]

class SenteKyosya43F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 2), [False, True]),
                        ((4, 1), [False, True]),
                        ((4, 0), [True])
                      ]

class SenteKyosya41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 0), [True])]

class SenteKyosya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteKyosya80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteKyosya70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteKyosya10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteKyosya00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class GoteKyosya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 5), None),
                        ((4, 6), [False, True]),
                        ((4, 7), [False, True]),
                        ((4, 8), [True])
                      ]

class GoteKyosya45F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 6), [False, True]),
                        ((4, 7), [False, True]),
                        ((4, 8), [True])
                      ]

class GoteKyosya47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 8), [True])]

class GoteKyosya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteKyosya88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteKyosya78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteKyosya18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteKyosya08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Kyosya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]


# Keima
class SenteKeima44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((5, 2), [False, True]), ((3, 2), [False, True])]

class SenteKeima42F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 2)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((5, 0), [True]), ((3, 0), [True])]

class GoteKeima44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((5, 6), [False, True]), ((3, 6), [False, True])]

class SenteKeima44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteKeima80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteKeima70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteKeima10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteKeima00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class GoteKeima46F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 6)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((5, 8), [True]), ((3, 8), [True])]

class GoteKeima44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteKeima88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteKeima78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteKeima18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteKeima08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Keima, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]


# Gin
class SenteGin44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),

                        ((5, 5), None),                 ((3, 5), None),
                      ]

class SenteGin43F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 2), [False, True]),
                        ((4, 2), [False, True]),
                        ((3, 2), [False, True]),

                        ((5, 4), None),
                        ((3, 4), None),
                      ]

class SenteGin42F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 2)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 1), [False, True]),
                        ((4, 1), [False, True]),
                        ((3, 1), [False, True]),

                        ((5, 3), [False, True]),
                        ((3, 3), [False, True]),
                      ]

class SenteGin41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 0), [False, True]),
                        ((4, 0), [False, True]),
                        ((3, 0), [False, True]),

                        ((5, 2), [False, True]),
                        ((3, 2), [False, True]),
                      ]

class SenteGin40F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 1), [False, True]),
                        ((3, 1), [False, True]),
                      ]

class SenteGin44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteGin80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteGin70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteGin10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteGin00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class GoteGin44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None),                 ((3, 3), None),

                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteGin45F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 4), None),
                        ((3, 4), None),

                        ((5, 6), [False, True]),
                        ((4, 6), [False, True]),
                        ((3, 6), [False, True]),
                      ]

class GoteGin46F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 6)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 5), [False, True]),
                        ((3, 5), [False, True]),

                        ((5, 7), [False, True]),
                        ((4, 7), [False, True]),
                        ((3, 7), [False, True]),
                      ]

class GoteGin47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 6), [False, True]),
                        ((3, 6), [False, True]),

                        ((5, 8), [False, True]),
                        ((4, 8), [False, True]),
                        ((3, 8), [False, True]),
                      ]

class GoteGin48F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 7), [False, True]),
                        ((3, 7), [False, True]),
                      ]

class GoteGin44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteGin88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteGin78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteGin18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteGin08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Gin, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]


# Kin
class SenteKin44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteKin43F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Shogiban([0, [(0, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 2), None), ((4, 2), None), ((3, 2), None),
                        ((5, 3), None),                 ((3, 3), None),
                                        ((4, 4), None),
                      ]

class SenteKin42F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 2)
        self.ban    = pyshogi.Shogiban([0, [(0, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 1), None), ((4, 1), None), ((3, 1), None),
                        ((5, 2), None),                 ((3, 2), None),
                                        ((4, 3), None),
                      ]

class SenteKin41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Shogiban([0, [(0, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 0), None), ((4, 0), None), ((3, 0), None),
                        ((5, 1), None),                 ((3, 1), None),
                                        ((4, 2), None),
                      ]

class SenteKin40F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 0)
        self.ban    = pyshogi.Shogiban([0, [(0, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 0), None),                 ((3, 0), None),
                                        ((4, 1), None),
                      ]

class GoteKin44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteKin45F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Shogiban([0, [(1, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 4), None),
                        ((5, 5), None),                 ((3, 5), None),
                        ((5, 6), None), ((4, 6), None), ((3, 6), None),
                      ]

class GoteKin46F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 6)
        self.ban    = pyshogi.Shogiban([0, [(1, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 5), None),
                        ((5, 6), None),                 ((3, 6), None),
                        ((5, 7), None), ((4, 7), None), ((3, 7), None),
                      ]

class GoteKin47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Shogiban([0, [(1, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 6), None),
                        ((5, 7), None),                 ((3, 7), None),
                        ((5, 8), None), ((4, 8), None), ((3, 8), None),
                      ]

class GoteKin48F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 8)
        self.ban    = pyshogi.Shogiban([0, [(1, Kin, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 7), None),
                        ((5, 8), None),                 ((3, 8), None),
                      ]


# Kaku
class SenteKaku44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Kaku, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), [False, True]), ((0, 0), [False, True]),
                        ((7, 1), [False, True]), ((1, 1), [False, True]),
                        ((6, 2), [False, True]), ((2, 2), [False, True]),
                        ((5, 3), None),          ((3, 3), None),

                        ((5, 5), None),          ((3, 5), None),
                        ((6, 6), None),          ((2, 6), None),
                        ((7, 7), None),          ((1, 7), None),
                        ((8, 8), None),          ((0, 8), None),
                      ]

class SenteKaku44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Kaku, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((0, 0), None),
                        ((7, 1), None),                 ((1, 1), None),
                        ((6, 2), None),                 ((2, 2), None),
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                        ((6, 6), None),                 ((2, 6), None),
                        ((7, 7), None),                 ((1, 7), None),
                        ((8, 8), None),                 ((0, 8), None),
                      ]

class GoteKaku44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Kaku, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),          ((0, 0), None),
                        ((7, 1), None),          ((1, 1), None),
                        ((6, 2), None),          ((2, 2), None),
                        ((5, 3), None),          ((3, 3), None),

                        ((5, 5), None),          ((3, 5), None),
                        ((6, 6), [False, True]), ((2, 6), [False, True]),
                        ((7, 7), [False, True]), ((1, 7), [False, True]),
                        ((8, 8), [False, True]), ((0, 8), [False, True]),
                      ]

class GoteKaku44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Kaku, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((0, 0), None),
                        ((7, 1), None),                 ((1, 1), None),
                        ((6, 2), None),                 ((2, 2), None),
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                        ((6, 6), None),                 ((2, 6), None),
                        ((7, 7), None),                 ((1, 7), None),
                        ((8, 8), None),                 ((0, 8), None),
                      ]


# Hisya
class SenteHisya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Hisya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 0), [False, True]),
                        ((4, 1), [False, True]),
                        ((4, 2), [False, True]),
                        ((4, 3), None),

                        ((8, 4), None),
                        ((7, 4), None),
                        ((6, 4), None),
                        ((5, 4), None),

                        ((3, 4), None),
                        ((2, 4), None),
                        ((1, 4), None),
                        ((0, 4), None),

                        ((4, 5), None),
                        ((4, 6), None),
                        ((4, 7), None),
                        ((4, 8), None),
                      ]

class SenteHisya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Hisya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 0), None),
                        ((4, 1), None),
                        ((4, 2), None),
                        ((4, 3), None),

                        ((8, 4), None),
                        ((7, 4), None),
                        ((6, 4), None),
                        ((5, 4), None),

                        ((5, 3), None),
                        ((3, 3), None),

                        ((5, 5), None),
                        ((3, 5), None),

                        ((3, 4), None),
                        ((2, 4), None),
                        ((1, 4), None),
                        ((0, 4), None),

                        ((4, 5), None),
                        ((4, 6), None),
                        ((4, 7), None),
                        ((4, 8), None),
                      ]

class GoteHisya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Hisya, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 0), None),
                        ((4, 1), None),
                        ((4, 2), None),
                        ((4, 3), None),

                        ((8, 4), None),
                        ((7, 4), None),
                        ((6, 4), None),
                        ((5, 4), None),

                        ((3, 4), None),
                        ((2, 4), None),
                        ((1, 4), None),
                        ((0, 4), None),

                        ((4, 5), None),
                        ((4, 6), [False, True]),
                        ((4, 7), [False, True]),
                        ((4, 8), [False, True]),
                      ]

class GoteHisya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Hisya, self.masume, 1)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 0), None),
                        ((4, 1), None),
                        ((4, 2), None),
                        ((4, 3), None),

                        ((8, 4), None),
                        ((7, 4), None),
                        ((6, 4), None),
                        ((5, 4), None),

                        ((5, 3), None),
                        ((3, 3), None),

                        ((5, 5), None),
                        ((3, 5), None),

                        ((3, 4), None),
                        ((2, 4), None),
                        ((1, 4), None),
                        ((0, 4), None),

                        ((4, 5), None),
                        ((4, 6), None),
                        ((4, 7), None),
                        ((4, 8), None),
                      ]


# Gyoku
class SenteGyoku44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(0, Gyoku, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteGyoku44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Shogiban([0, [(1, Gyoku, self.masume, 0)]])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

if __name__ == '__main__': unittest.main()
