#
#  test_pyshogi_mochi_koma.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012-2013 Jun Kikuchi. All rights reserved.
#

import pyshogi
import unittest

class MochiKomaTestCase:
    def test_ugoki(self):
        self.assertEqual(self.ugoki, self.koma.ugoki())

### Fu
class SenteFu_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Fu', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteFu_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Fu', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Kyosya
class SenteKyosya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Kyosya', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteKyosya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Kyosya', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Keima
class SenteKeima_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Keima', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 0))
            masus.remove(self.ban.masu(x, 1))
        self.ugoki = dict([(masu, None) for masu in masus])

class GoteKeima_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Keima', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]

        masus = set(self.ban)
        for x in range(0, 9):
            masus.remove(self.ban.masu(x, 7))
            masus.remove(self.ban.masu(x, 8))
        self.ugoki = dict([(masu, None) for masu in masus])

# Gin
class SenteGin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Gin', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteGin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Gin', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Kin
class SenteKin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Kin', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteKin_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Kin', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Kaku
class SenteKaku_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Kaku', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteKaku_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Kaku', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

# Hisya
class SenteHisya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(True, 'Hisya', None, False)])
        self.koma  = self.ban.mochigoma(True)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

class GoteHisya_TestCase(unittest.TestCase, MochiKomaTestCase):
    def setUp(self):
        self.ban   = pyshogi.Ban([(False, 'Hisya', None, False)])
        self.koma  = self.ban.mochigoma(False)[0]
        self.ugoki = dict([(masu, None) for masu in self.ban])

if __name__ == '__main__': unittest.main()
