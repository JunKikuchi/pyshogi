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
    def test_oute(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (0, Kin,   (4, 1), 0),
                    (0, Fu,    (4, 2), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 0
        self.assertFalse(ban.oute())

        ban.teban = 1
        self.assertTrue(ban.oute())

    def test_sente_ugoki1(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (1, Hisya, (4, 1), 0),
                    (0, Kin,   (4, 7), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 0
        self.assertFalse(ban.oute())

        kin = ban.masu(4, 7).koma
        self.assertEqual(kin.ugoki(), frozenset([ban.masu(4, 6)]))

        ban.teban = 1
        self.assertFalse(ban.oute())

    def test_gote_ugoki1(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (1, Kin,   (4, 1), 0),
                    (0, Hisya, (4, 7), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 1
        self.assertFalse(ban.oute())

        kin = ban.masu(4, 1).koma
        self.assertEqual(kin.ugoki(), frozenset([ban.masu(4, 2)]))

        ban.teban = 0
        self.assertFalse(ban.oute())

    def test_sente_ugoki2(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (1, Hisya, (4, 1), 0),
                    (0, Kin,   (3, 7), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 0
        self.assertTrue(ban.oute())

        kin = ban.masu(3, 7).koma
        self.assertEqual(
            kin.ugoki(), frozenset([ban.masu(4, 6), ban.masu(4, 7)]))

        ban.teban = 1
        self.assertFalse(ban.oute())

    def test_gote_ugoki2(self):
        ban = pyshogi.Shogiban(
            [
                0,
                [
                    (1, Gyoku, (4, 0), 0),
                    (1, Kin,   (3, 1), 0),
                    (0, Hisya, (4, 7), 0),
                    (0, Gyoku, (4, 8), 0),
                ]
            ]
        )

        ban.teban = 1
        self.assertTrue(ban.oute())

        kin = ban.masu(3, 1).koma
        self.assertEqual(
            kin.ugoki(), frozenset([ban.masu(4, 1), ban.masu(4, 2)]))

        ban.teban = 0
        self.assertFalse(ban.oute())

if __name__ == '__main__': unittest.main()
