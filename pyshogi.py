#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012 Jun Kikuchi. All rights reserved.
#

class Koma:
    UGOKI = [None, None]
    narikoma = False

    def __init__(self, ban, masu, sente):
        self.ban   = ban
        self.masu  = masu
        self.sente = sente

        if self.masu: masu.koma = self

    def __str__(self):
        return "%s:%s" % (self.__class__.__name__, self.sente)

    def naru(self):
        if self.UGOKI[1]: self.narikoma = True

    def is_movable(self, x, y):
        masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
        if masu and (masu.koma is None or masu.koma.sente <> self.sente):
            return masu
        return None;

    def movables(self):
        masus = []

        if not self.sente: self.masu.ban.round()

        if self.narikoma:
            ugokis = self.UGOKI[1]
        else:
            ugokis = self.UGOKI[0]

        for hashiru, ugoki in ugokis:
            for mx, my in ugoki:
                x, y = mx, my
                masu = self.is_movable(x, y)
                if hashiru:
                    while(masu):
                        masus.append(masu)
                        if masu.koma and masu.koma.sente <> self.sente: break
                        x += mx
                        y += my
                        masu = self.is_movable(x, y)
                else:
                    masus.append(masu)

        if not self.sente: self.masu.ban.round()

        return frozenset(masus)

# 8 7 6 5 4 3 2 1 0
#                 1
#                 2
#                 3
#                 4
#                 5
#                 6
#                 7
#                 8

class Gyoku(Koma):
    UGOKI = [
        [
            (False, frozenset([
                (1, -1), (0, -1), (-1, -1),
                (1,  0),          (-1,  0),
                (1,  1), (0,  1), (-1,  1),
            ]))
        ],
        None
    ]

class Hisya(Koma):
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ]))
        ],
        [
            (True, frozenset([
                         (0, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ])),
            (False, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1),
            ]))
        ]
    ]

class Kaku(Koma):
    UGOKI = [
        [
            (True, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1)
            ]))
        ],
        [
            (True, frozenset([
                (1, -1),          (-1, -1),

                (1,  1),          (-1,  1)
            ])),
            (False, frozenset([
                         (0, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ])),
        ]
    ]

class Kin(Koma):
    UGOKI = [
        [
            (False, frozenset([
                (1, -1), (0, -1), (-1, -1),
                (1,  0),          (-1,  0),
                         (0,  1)
            ]))
        ],
        None
    ]

class Gin(Koma):
    UGOKI = [
        [
            (False, frozenset([
                (1, -1), (0, -1), (-1, -1),

                (1,  1),          (-1,  1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Keima(Koma):
    UGOKI = [
        [
            (False, frozenset([
                (1, -2),          (-1, -2)


            ]))
        ],
        Kin.UGOKI[0]
    ]

class Kyosya(Koma):
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Fu(Koma):
    UGOKI = [
        [
            (False, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

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

class Ban:
    def __init__(self, data=HIRATE):
        self.masus = [
            [
                Masu(self, x, y) for y in range(0, 9)
            ] for x in range(0, 9)
        ]
        self.komas = []
        for masu, koma, sente in data:
            if masu:
                x, y = masu
                masu = self.masus[x][y]
            self.komas.append(koma(self, masu, sente))

    def __iter__(self):
        for x in range(0, 9):
            for y in range(0, 9):
                yield self.masus[x][y]

    def __str__(self):
        return "\n".join(
            [
                " ".join(
                    [
                        str(self.masus[x][y]) for x in range(8, -1, -1)
                    ]
                ) for y in range(0, 9)
            ]
        )

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

