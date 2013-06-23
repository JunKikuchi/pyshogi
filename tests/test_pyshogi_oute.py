#
#  test_pyshogi_tsumi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class OuteTestCase(unittest.TestCase):
    '''
    def test_oute(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (True,  Kin,   (4, 1), False),
                    (True,  Fu,    (4, 2), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertFalse(ban.oute())

        ban.teban = False
        self.assertTrue(ban.oute())

    def test_sente_ugoki1(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (False, Hisya, (4, 1), False),
                    (True,  Kin,   (4, 7), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertFalse(ban.oute())

        kin = ban.masu(4, 7).koma
        self.assertEqual(kin.ugoki(), frozenset([ban.masu(4, 6)]))

        ban.teban = False
        self.assertFalse(ban.oute())

    def test_gote_ugoki1(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (False, Kin,   (4, 1), False),
                    (True,  Hisya, (4, 7), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = False
        self.assertFalse(ban.oute())

        kin = ban.masu(4, 1).koma
        self.assertEqual(kin.ugoki(), frozenset([ban.masu(4, 2)]))

        ban.teban = True
        self.assertFalse(ban.oute())

    def test_sente_ugoki2(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (False, Hisya, (4, 1), False),
                    (True,  Kin,   (3, 7), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertTrue(ban.oute())

        kin = ban.masu(3, 7).koma
        self.assertEqual(
            kin.ugoki(), frozenset([ban.masu(4, 6), ban.masu(4, 7)]))

        ban.teban = False
        self.assertFalse(ban.oute())
    '''

    def test_sente_ugoki3(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Hisya, (0, 8), False),
                    (False, Kin,   (1, 8), False),
                    (True,  Gyoku, (3, 8), False),
                ]
            ]
        )

        ban.teban = True
        self.assertFalse(ban.oute())

    '''
    def test_gote_ugoki2(self):
        ban = pyshogi.Shogiban(
            [
                True,
                [
                    (False, Gyoku, (4, 0), False),
                    (False, Kin,   (3, 1), False),
                    (True,  Hisya, (4, 7), False),
                    (True,  Gyoku, (4, 8), False),
                ]
            ]
        )

        ban.teban = False
        self.assertTrue(ban.oute())

        kin = ban.masu(3, 1).koma
        self.assertEqual(
            kin.ugoki(), frozenset([ban.masu(4, 1), ban.masu(4, 2)]))

        ban.teban = True
        self.assertFalse(ban.oute())
    '''

if __name__ == '__main__': unittest.main()
