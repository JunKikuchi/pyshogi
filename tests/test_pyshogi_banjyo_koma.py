#
#  test_pyshogi_banjyo_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class BanjyoKomaTestCase:
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
        for (x, y), narikomi in self.ugoki:
            if narikomi is None:
                self.setUp()
                old_masu = self.koma.masu
                masu = self.ban.masu(x, y)
                self.koma.move(masu)
                self.assertEqual(masu.koma, self.koma)
                self.assertEqual(self.koma.masu, masu)
                self.assertIsNone(old_masu.koma)
            else:
                for narikomi in narikomi:
                    self.setUp()
                    old_masu = self.koma.masu
                    masu = self.ban.masu(x, y)
                    self.koma.move(masu, narikomi)
                    self.assertEqual(masu.koma, self.koma)
                    self.assertEqual(self.koma.masu, masu)
                    self.assertEqual(self.koma.narikoma, narikomi)
                    self.assertIsNone(old_masu.koma)

    def test_move_error(self):
        ugoki = frozenset([
            apply(self.ban.masu, masume) for masume, narikomi in self.ugoki])

        for x in range(9):
            for y in range(9):
                masu = self.ban.masu(x, y)
                if masu not in ugoki:
                    with self.assertRaises(pyshogi.CanNotPlaceKomaError):
                        self.koma.move(masu)

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(-1, -1))

        with self.assertRaises(pyshogi.CanNotPlaceKomaError):
            self.koma.move(self.ban.masu(9, 9))

### Fu
class SenteFu44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 3), None)]

class SenteFu44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteFu80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteFu70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteFu10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteFu00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class SenteFu43F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 3)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 2), [False, True])]

class SenteFu41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Ban([(True, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 0), [True])]

class GoteFu44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 5), None)]

class GoteFu44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteFu88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteFu78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteFu18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteFu08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]

class GoteFu45F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 5)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 6), [False, True])]

class GoteFu47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Ban([(False, 'Fu', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 8), [True])]

# Kyosya
class SenteKyosya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, False)])
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
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 2), [False, True]),
                        ((4, 1), [False, True]),
                        ((4, 0), [True])
                      ]

class SenteKyosya41F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 1)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 0), [True])]

class SenteKyosya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((5, 3), None), ((4, 3), None), ((3, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                                        ((4, 5), None),
                      ]

class SenteKyosya80T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 0)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 0), None),
                        ((8, 1), None),
                      ]

class SenteKyosya70T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 0)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 0), None),                 ((6, 0), None),
                                        ((7, 1), None),
                      ]

class SenteKyosya10T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 0)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((2, 0), None),                 ((0, 0), None),
                                        ((1, 1), None),
                      ]

class SenteKyosya00T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 0)
        self.ban    = pyshogi.Ban([(True, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((1, 0), None),
                                        ((0, 1), None),
                      ]

class GoteKyosya44F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, False)])
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
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((4, 6), [False, True]),
                        ((4, 7), [False, True]),
                        ((4, 8), [True])
                      ]

class GoteKyosya47F_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 7)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, False)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [((4, 8), [True])]

class GoteKyosya44T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (4, 4)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((4, 3), None),
                        ((5, 4), None),                 ((3, 4), None),
                        ((5, 5), None), ((4, 5), None), ((3, 5), None),
                      ]

class GoteKyosya88T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (8, 8)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                        ((8, 7), None),
                                        ((7, 8), None),
                      ]

class GoteKyosya78T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (7, 8)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((7, 7), None),
                        ((8, 8), None),                 ((6, 8), None),
                      ]

class GoteKyosya18T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (1, 8)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((1, 7), None),
                        ((2, 8), None),                 ((0, 8), None),
                      ]

class GoteKyosya08T_TestCase(unittest.TestCase, BanjyoKomaTestCase):
    def setUp(self):
        self.masume = (0, 8)
        self.ban    = pyshogi.Ban([(False, 'Kyosya', self.masume, True)])
        self.koma   = apply(self.ban.masu, self.masume).koma
        self.ugoki  = [
                                        ((0, 7), None),
                        ((1, 8), None),
                      ]

if __name__ == '__main__': unittest.main()
