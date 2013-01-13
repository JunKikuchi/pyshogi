#
#  test_pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

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

        for sente, koma, (x, y), narikoma in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__.__name__, koma)
            self.assertEqual(masu.koma.narikoma, narikoma)

            if y < 3:
                self.assertFalse(masu.koma.sente)
            else:
                self.assertTrue(masu.koma.sente)

    def test_kaiten(self):
        self.ban.kaiten()

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

        for sente, koma, (x, y), narikoma in pyshogi.HIRATE:
            masu = self.ban.masu(x, y)
            self.assertIsNotNone(masu.koma)
            self.assertNotEqual(masu.koma.sente, sente)
            self.assertEqual(masu.koma.__class__.__name__, koma)
            self.assertEqual(masu.koma.narikoma, narikoma)

            if y < 3:
                self.assertTrue(masu.koma.sente)
            else:
                self.assertFalse(masu.koma.sente)

    def test_mochigoma(self):
        self.assertEqual(self.ban.mochigoma(True), [])
        self.assertEqual(self.ban.mochigoma(False), [])

if __name__ == '__main__': unittest.main()
