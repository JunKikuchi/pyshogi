#
#  test_pyshogi_tsumi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
from pyshogi import Gyoku, Hisya, Kaku, Kin, Gin, Keima, Kyosya, Fu
import unittest

class ShogibanTestCase(unittest.TestCase):
    def test_dump(self):
        shogiban = pyshogi.Shogiban()
        self.assertEqual(shogiban.dump(), pyshogi.HIRATE)

        shogiban1 = pyshogi.Shogiban(shogiban.dump())
        self.assertEqual(shogiban.dump(), shogiban1.dump())

    def test_clone(self):
        shogiban = pyshogi.Shogiban(
            [
                True,
                [
                    (True,  Gyoku, (4, 0), False),
                    (False, Kin,   (4, 1), False),
                    (False, Fu,    (4, 2), False),
                    (False, Gyoku, (4, 8), False),
                ]
            ]
        )
        shogiban1 = shogiban.clone()
        self.assertEqual(shogiban.dump(), shogiban1.dump())

    def test_size(self):
        shogiban = pyshogi.Shogiban()
        self.assertEqual(len(shogiban.masus), 9)
        for xs in shogiban.masus:
            self.assertEqual(len(xs), 9)

    def test_masus(self):
        shogiban = pyshogi.Shogiban()

        for masu in shogiban:
            self.assertIsInstance(masu, pyshogi.Masu)

        for x in range(0, 9):
            for y in range(0, 9):
                masu = shogiban.masu(x, y)
                self.assertIsInstance(masu, pyshogi.Masu)

        for x, y in [(-1, -1), (-1, 0), (0, -1), (-1, 9), (-1, 8), (0, 9), (9, 9), (9, -1)]:
            masu = shogiban.masu(x, y)
            self.assertIsNone(masu)

    def test_komas(self):
        shogiban = pyshogi.Shogiban()

        self.assertEqual(len(shogiban.komas), 9 * 4 + 4)

        for koma in shogiban.komas:
            self.assertIsInstance(koma, pyshogi.Koma)
            self.assertIsInstance(koma.masu, pyshogi.Masu)

            masu = shogiban.masu(koma.masu.x, koma.masu.y)
            self.assertEqual(koma.masu, masu)

            if koma.masu.y < 3:
                self.assertEqual(koma.sengo, False)
            else:
                self.assertEqual(koma.sengo, True)

        for sengo, koma, (x, y), nari in pyshogi.HIRATE[1]:
            masu = shogiban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertEqual(masu.koma.sengo, sengo)
            self.assertEqual(masu.koma.__class__, koma)
            self.assertEqual(masu.koma.nari, nari)

            if masu.y < 3:
                self.assertEqual(masu.koma.sengo, False)
            else:
                self.assertEqual(masu.koma.sengo, True)

    def test_kaiten(self):
        shogiban = pyshogi.Shogiban()
        shogiban.kaiten()

        self.assertEqual(len(shogiban.komas), 9 * 4 + 4)

        for koma in shogiban.komas:
            self.assertIsInstance(koma, pyshogi.Koma)
            self.assertIsInstance(koma.masu, pyshogi.Masu)

            masu = shogiban.masu(koma.masu.x, koma.masu.y)
            self.assertEqual(koma.masu, masu)

            if koma.masu.y < 3:
                self.assertEqual(koma.sengo, True)
            else:
                self.assertEqual(koma.sengo, False)

        for sengo, koma, (x, y), nari in pyshogi.HIRATE[1]:
            masu = shogiban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertNotEqual(masu.koma.sengo, sengo)
            self.assertEqual(masu.koma.__class__, koma)
            self.assertEqual(masu.koma.nari, nari)

            if masu.y < 3:
                self.assertEqual(masu.koma.sengo, True)
            else:
                self.assertEqual(masu.koma.sengo, False)

    def test_mochigoma(self):
        shogiban = pyshogi.Shogiban()
        self.assertEqual(shogiban.mochigoma(True), [])
        self.assertEqual(shogiban.mochigoma(False), [])

    def test_teban(self):
        shogiban = pyshogi.Shogiban()
        self.assertEqual(shogiban.teban, True)

        with self.assertRaises(pyshogi.TebanError):
            shogiban.masu(1, 2).koma.idou(1, 3)

        shogiban.masu(6, 6).koma.idou(6, 5)
        self.assertEqual(shogiban.teban, False)

if __name__ == '__main__': unittest.main()
