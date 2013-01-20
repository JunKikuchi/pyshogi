# -*- coding: utf-8 -*-
#
#  pyshogi.py
#
#  Created by Jun Kikuchi
#  Copyright (c) 2012-2013 Jun Kikuchi. All rights reserved.
#

class Error(Exception):
    pass

class CanNotPlaceKomaError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

    def __str__(self):
        return "%s %s %s" % (self.__class__.__name__, self.koma, self.masu)

class TebanError(Error):
    def __init__(self, koma, masu):
        self.koma = koma
        self.masu = masu

    def __str__(self):
        return "%s %s %s" % (self.__class__.__name__, self.koma, self.masu)

class Koma:
    KACHI = None
    YOMI  = [None, None]
    UGOKI = [None, None]

    def __init__(self, ban, sente, masu=None, narikoma=False):
        self.ban   = ban
        self.sente = sente

        if masu:
            if narikoma:
                ugoki = frozenset([m for m in self.ban if masu.koma is None])
            else:
                if not self.sente: self.ban.kaiten()
                ugoki = self._tegoma_ugoki()
                if not self.sente: self.ban.kaiten()
            if masu not in ugoki:
                raise CanNotPlaceKomaError(self, masu)
            masu.koma = self

        self.masu     = masu
        self.narikoma = narikoma
        self.index    = None

    def __str__(self):
        if self.narikoma:
            yomi = self.YOMI[1]
        else:
            yomi = self.YOMI[0]

        if self.sente:
            xs = ('[', yomi, ']')
        else:
            xs = ('(', yomi, ')')

        return '%s%s%s' % xs

    def __cmp__(self, other):
        return cmp(self.KACHI, other.KACHI)

    def dump(self):
        if self.masu:
            masu = self.masu.dump()
        else:
            masu = None
        return (self.sente, self.__class__.__name__, masu, self.narikoma)

    def kiki(self):
        if not self.sente: self.ban.kaiten()
        kiki = self._banjyo_ugoki(True)
        if not self.sente: self.ban.kaiten()

        return kiki

    def ugoki(self):
        if not self.sente: self.ban.kaiten()
        if self.masu:
            ugoki = self._banjyo_ugoki()
        else:
            ugoki = self._tegoma_ugoki()
        if not self.sente: self.ban.kaiten()

        oute = set()
        for masu in ugoki:
            ban = self.ban.clone()
            ban.sakiyomi = True
            koma = ban.komas[self.index]
            koma.move(ban.masu(masu.x, masu.y))
            ban.teban = self.ban.teban
            if ban.oute():
                oute.add(masu)

        return ugoki.difference(oute)

    def move(self, masu, naru=False):
        if self.sente <> self.ban.teban:
            raise TebanError(self, masu)

        if (not self.ban.sakiyomi) and (masu not in self.ugoki()):
            raise CanNotPlaceKomaError(self, masu)

        if self.masu and self.masu.koma:
            self.masu.koma = None

        koma = masu.koma
        if koma:
            koma.masu     = None
            koma.sente    = self.sente
            koma.narikoma = False

        masu.koma = self
        self.masu = masu

        if naru and self.UGOKI[1]:
            self.narikoma = True

        self.ban.teban = not self.ban.teban

    def _banjyo_ugoki(self, kiki=False):
        masus = []

        if self.narikoma:
            ugokis = self.UGOKI[1]
        else:
            ugokis = self.UGOKI[0]

        for hashiru, ugoki in ugokis:
            for mx, my in ugoki:
                x, y = mx, my
                masu = self._banjyo_ugoki_check(x, y, kiki)
                if hashiru:
                    while(masu):
                        masus.append(masu)
                        if masu.koma and masu.koma.sente <> self.sente: break
                        x += mx
                        y += my
                        masu = self._banjyo_ugoki_check(x, y, kiki)
                else:
                    if masu:
                        masus.append(masu)

        return frozenset(masus)

    def _tegoma_ugoki(self):
        return frozenset([masu for masu in self.ban if masu.koma is None])

    def _banjyo_ugoki_check(self, x, y, kiki=False):
        if self.masu:
            masu = self.ban.masu(self.masu.x + x, self.masu.y + y)
            if masu:
                if kiki:
                    return masu
                if (masu.koma is None or masu.koma.sente <> self.sente):
                    return masu
        return None;

    def narikomi(self, masu):
        if not self.sente: self.ban.kaiten()

        if self.narikoma or self.masu is None or self.UGOKI[1] is None:
            narikomi = None
        else:
            narikomi = self._narikomi_check(masu)

        if not self.sente: self.ban.kaiten()

        return narikomi

    def _narikomi_check(self, masu):
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

# 0 1 2 3 4 5 6 7 8
#                 1
#                 2
#                 3
#                 4
#                 5
#                 6
#                 7
#                 8

class Gyoku(Koma):
    KACHI = 1
    YOMI  = ['王将', None]
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1),
            ]))
        ],
        None
    ]

class Hisya(Koma):
    KACHI = 2
    YOMI  = ['飛車', '竜王']
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ]))
        ],
        [
            (True, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ])),
            (False, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1),
            ]))
        ]
    ]

class Kaku(Koma):
    KACHI = 3
    YOMI  = ['角行', '竜馬']
    UGOKI = [
        [
            (True, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1)
            ]))
        ],
        [
            (True, frozenset([
                (-1, -1),          (1, -1),

                (-1,  1),          (1,  1)
            ])),
            (False, frozenset([
                         (0, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ])),
        ]
    ]

class Kin(Koma):
    KACHI = 4
    YOMI  = ['金将', None]
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                         (0,  1)
            ]))
        ],
        None
    ]

class Gin(Koma):
    KACHI = 5
    YOMI  = ['銀将', '成銀']
    UGOKI = [
        [
            (False, frozenset([
                (-1, -1), (0, -1), (1, -1),

                (-1,  1),          (1,  1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

class Keima(Koma):
    KACHI = 6
    YOMI  = ['桂馬', '成桂']
    UGOKI = [
        [
            (False, frozenset([
                (-1, -2),          (1, -2)


            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        return frozenset([
            masu for masu in self.ban if masu.koma is None and masu.y > 1])

    def _narikomi_check(self, masu):
        if masu.y < 2:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

class Kyosya(Koma):
    KACHI = 7
    YOMI  = ['香車', '成香']
    UGOKI = [
        [
            (True, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        return frozenset([
            masu for masu in self.ban if masu.koma is None and masu.y > 0])

    def _narikomi_check(self, masu):
        if masu.y == 0:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

class Fu(Koma):
    KACHI = 8
    YOMI  = ['歩兵', 'と金']
    UGOKI = [
        [
            (False, frozenset([
                         (0, -1),
            ]))
        ],
        Kin.UGOKI[0]
    ]

    def _tegoma_ugoki(self):
        fu_x = set([
            masu.x for masu in self.ban
                if masu.koma and
                   masu.koma.sente == self.sente and
                   isinstance(masu.koma, self.__class__)])
        return frozenset([
            masu for masu in self.ban
                if masu.koma is None and
                   masu.y > 0 and
                   masu.x not in fu_x])

    def _narikomi_check(self, masu):
        if masu.y == 0:
            return [True]
        if self.masu.y < 3 or masu.y < 3:
            return [False, True]
        return None

class Masu:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.koma = None

    def __str__(self):
        return "(%d,%d):%s" % (self.x, self.y, self.koma)

    def dump(self):
        return (self.x, self.y)

    def kaiten(self):
        self.x = 8 - self.x
        self.y = 8 - self.y

HIRATE = [
    (False, 'Kyosya', (0, 0), False),
    (False, 'Keima',  (1, 0), False),
    (False, 'Gin',    (2, 0), False),
    (False, 'Kin',    (3, 0), False),
    (False, 'Gyoku',  (4, 0), False),
    (False, 'Kin',    (5, 0), False),
    (False, 'Gin',    (6, 0), False),
    (False, 'Keima',  (7, 0), False),
    (False, 'Kyosya', (8, 0), False),
    (False, 'Hisya',  (1, 1), False),
    (False, 'Kaku',   (7, 1), False),
    (False, 'Fu',     (0, 2), False),
    (False, 'Fu',     (1, 2), False),
    (False, 'Fu',     (2, 2), False),
    (False, 'Fu',     (3, 2), False),
    (False, 'Fu',     (4, 2), False),
    (False, 'Fu',     (5, 2), False),
    (False, 'Fu',     (6, 2), False),
    (False, 'Fu',     (7, 2), False),
    (False, 'Fu',     (8, 2), False),
    (True,  'Fu',     (0, 6), False),
    (True,  'Fu',     (1, 6), False),
    (True,  'Fu',     (2, 6), False),
    (True,  'Fu',     (3, 6), False),
    (True,  'Fu',     (4, 6), False),
    (True,  'Fu',     (5, 6), False),
    (True,  'Fu',     (6, 6), False),
    (True,  'Fu',     (7, 6), False),
    (True,  'Fu',     (8, 6), False),
    (True,  'Kaku',   (1, 7), False),
    (True,  'Hisya',  (7, 7), False),
    (True,  'Kyosya', (0, 8), False),
    (True,  'Keima',  (1, 8), False),
    (True,  'Gin',    (2, 8), False),
    (True,  'Kin',    (3, 8), False),
    (True,  'Gyoku',  (4, 8), False),
    (True,  'Kin',    (5, 8), False),
    (True,  'Gin',    (6, 8), False),
    (True,  'Keima',  (7, 8), False),
    (True,  'Kyosya', (8, 8), False),
]

class Ban:
    def __init__(self, data=HIRATE):
        if isinstance(data, list):
            data = {'TEBAN': True, 'KOMA':  data}

        self.sakiyomi = False
        self.teban    = data['TEBAN']
        self.masus    = [[Masu(x, y) for y in range(9)] for x in range(9)]
        self.komas    = []
        self.gyokus   = {}

        koma_data = zip(data['KOMA'], range(0, len(data['KOMA'])))
        for (sente, koma_class, masu, narikoma), (i) in koma_data:
            if masu:
                x, y = masu
                masu = self.masus[x][y]
            koma = eval(koma_class)(self, sente, masu, narikoma)
            koma.index = i
            self.komas.append(koma)
            if koma_class == 'Gyoku':
                self.gyokus[koma.sente] = koma

    def __iter__(self):
        for x in range(9):
            for y in range(9):
                yield self.masus[x][y]

    def __str__(self):
        teban = {True: '', False: ''}
        if self.teban:
            teban[self.teban] = '先手番'
        else:
            teban[self.teban] = '後手番'

        gote  = '(後手)：' + ' '.join([str(a) for a in self.mochigoma(False)])
        sente = '[先手]：' + ' '.join([str(a) for a in self.mochigoma(True)])

        '''
        col = ' '.join([
            '  %s  ' % (n)
                for n in ['９', '８', '７', '６', '５', '４', '３', '２', '１']
        ])
        row = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
        '''

        col = ' '.join(['   %s  ' % (n) for n in range(0, 9)])
        row = [str(n) for n in range(0, 9)]

        ban = [
            ' '.join([
                str(self.masus[x][y].koma or ' ____ ') for x in range(0, 9)
            ]) + ' ' + row[y] for y in range(9)
        ]

        return "\n".join(
            [teban[False]] + [gote] + [col] + ban + [sente] + [teban[True]]
        ) + "\n"

    def dump(self):
        return {
            'TEBAN': self.teban,
            'KOMA':  [koma.dump() for koma in self.komas],
        }

    def clone(self):
        return self.__class__(self.dump())

    def masu(self, x, y):
        if 0 <= x <= 8 and 0 <= y <= 8:
            return self.masus[x][y]
        else:
            return None

    def kaiten(self):
        for xs in self.masus:
            xs.reverse()
            for masu in xs:
                masu.kaiten()
        self.masus.reverse()

    def mochigoma(self, sente):
        xs = [a for a in self.komas if a.sente == sente and a.masu is None]
        xs.sort()
        return xs

    def kiki(self, sente):
        kiki = []
        for koma in [a for a in self.komas if a.sente == sente]:
            kiki += koma.kiki()
        return frozenset(kiki)

    def oute(self):
        if self.teban not in self.gyokus:
            return None

        gyoku = self.gyokus[self.teban]
        return gyoku.masu in self.kiki(not self.teban)

    def tsumi(self):
        if self.teban not in self.gyokus:
            return None

        gyoku = self.gyokus[self.teban]
        return self.oute() and gyoku.ugoki().issubset(self.kiki(not self.teban))
