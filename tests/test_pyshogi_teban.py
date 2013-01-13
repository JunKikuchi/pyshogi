#
#  test_pyshogi_mochi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class TebanTestCase(unittest.TestCase):
    def test_teban(self):
        ban = pyshogi.Ban()
        self.assertEqual(ban.teban, True)

        with self.assertRaises(pyshogi.TebanError):
            ban.masu(1, 2).koma.move(ban.masu(1, 3))

        ban.masu(6, 6).koma.move(ban.masu(6, 5))
        self.assertEqual(ban.teban, False)

if __name__ == '__main__': unittest.main()
