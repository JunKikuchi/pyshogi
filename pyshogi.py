#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

class Koma:
    MOVABLES = frozenset([])
    narikoma = False

    def __init__(self, ban, sente, masu):
        self.ban   = ban
        self.masu  = masu
        self.sente = sente

        if self.masu: masu.koma = self

    def __str__(self):
        return "%s:%s" % (self.__class__.__name__, self.sente)

    def is_movable(self, x, y):
        masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
        if masu and (masu.koma is None or masu.koma.sente <> self.sente):
            return masu
        return None;

    def movable_masus(self):
        masus = []

        if not self.sente: self.masu.ban.round()

        if self.narikoma:
            movables = self.MOVABLES | Kin.MOVABLES
        else:
            movables = self.MOVABLES

        for x, y in movables:
            masu = self.is_movable(x, y)
            if masu:
                masus.append(masu)

        if not self.sente: self.masu.ban.round()

        return frozenset(masus)

class HashiriGoma(Koma):
    def movable_masus(self):
        masus = []

        if not self.sente: self.masu.ban.round()

        for mx, my in self.MOVABLES:
            x, y = mx, my
            masu = self.is_movable(x, y)
            while(masu):
                masus.append(masu)
                if masu.koma and masu.koma.sente <> self.sente: break
                x += mx
                y += my
                masu = self.is_movable(x, y)

        if self.narikoma:
            for x, y in Kin.MOVABLES:
                masu = self.is_movable(x, y)
                if masu:
                    masus.append(masu)

        if not self.sente: self.masu.ban.round()

        return frozenset(masus)

class Fu(Koma):
    MOVABLES = frozenset([(0, -1)])

class Kyosya(HashiriGoma):
    MOVABLES = frozenset([(0, -1)])

class Keima(Koma):
    MOVABLES = frozenset([(-1, -2), (1, -2)])

class Gin(Koma):
    MOVABLES = frozenset([(1, -1), (0, -1), (-1, -1), (1, 1), (-1, 1)])

class Kin(Koma):
    MOVABLES = frozenset([(1, -1), (0, -1), (-1, -1), (1, 0), (-1, 0), (0, 1)])

class Kaku(HashiriGoma):
    MOVABLES = frozenset([(1, -1), (-1, -1), (-1, 1), (1, 1)])

class Hisya(HashiriGoma):
    MOVABLES = frozenset([(0, -1), (0, 1), (-1, 0), (1, 0)])

class Gyoku(Koma):
    MOVABLES = frozenset([(1, -1), (0, -1), (-1, -1), (1, 0), (-1, 0), (1, 1), (0, 1), (-1, 1)])

class Masu:
    koma = None

    def __init__(self, ban, x, y):
        self.ban = ban
        self.x = x
        self.y = y

    def __str__(self):
        return "%d,%d,%s" % (self.x, self.y, self.koma)

    def round(self):
        self.x = 8 - self.x
        self.y = 8 - self.y

HIRATE = [
    ((8, 0), Kyosya, False),
    ((7, 0), Keima,  False),
    ((6, 0), Gin,    False),
    ((5, 0), Kin,    False),
    ((4, 0), Gyoku,  False),
    ((3, 0), Kin,    False),
    ((2, 0), Gin,    False),
    ((1, 0), Keima,  False),
    ((0, 0), Kyosya, False),
    ((7, 1), Hisya,  False),
    ((1, 1), Kaku,   False),
    ((8, 2), Fu,     False),
    ((7, 2), Fu,     False),
    ((6, 2), Fu,     False),
    ((5, 2), Fu,     False),
    ((4, 2), Fu,     False),
    ((3, 2), Fu,     False),
    ((2, 2), Fu,     False),
    ((1, 2), Fu,     False),
    ((0, 2), Fu,     False),
    ((8, 6), Fu,     True),
    ((7, 6), Fu,     True),
    ((6, 6), Fu,     True),
    ((5, 6), Fu,     True),
    ((4, 6), Fu,     True),
    ((3, 6), Fu,     True),
    ((2, 6), Fu,     True),
    ((1, 6), Fu,     True),
    ((0, 6), Fu,     True),
    ((7, 7), Kaku,   True),
    ((1, 7), Hisya,  True),
    ((8, 8), Kyosya, True),
    ((7, 8), Keima,  True),
    ((6, 8), Gin,    True),
    ((5, 8), Kin,    True),
    ((4, 8), Gyoku,  True),
    ((3, 8), Kin,    True),
    ((2, 8), Gin,    True),
    ((1, 8), Keima,  True),
    ((0, 8), Kyosya, True),
]

# 8 7 6 5 4 3 2 1 0
#                 1
#                 2
#                 3
#                 4
#                 5
#                 6
#                 7
#                 8

class Ban:
    def __init__(self, data=HIRATE):
        self.masus = [[Masu(self, x, y) for y in range(0, 9)] for x in range(0, 9)]
        self.komas = []
        for masu, koma, sente in data:
            if masu:
                x, y = masu
                masu = self.masus[x][y]
            self.komas.append(koma(self, sente, masu))

    def __iter__(self):
        for x in range(0, 9):
            for y in range(0, 9):
                yield self.masus[x][y]

    def __str__(self):
        return "\n".join([" ".join([str(self.masus[x][y]) for x in range(8, -1, -1)])for y in range(0, 9)])

    def masu(self, x, y):
        if 0 <= x <= 8 and 0 <= y <= 8:
            return self.masus[x][y]
        else:
            return None

    def round(self):
        for xs in self.masus:
            xs.reverse()
            for masu in xs:
                masu.round()
        self.masus.reverse()

