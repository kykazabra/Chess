import numpy as np
from math import sqrt


def tr(a):
    wd = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, '1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
          '6': 5, '7': 6, '8': 7}
    return wd[a]


class Piece(object):
    def __init__(self, h, v, colour):
        self.pos = (h, v)
        self.colour = colour
        self.model = None
        self.times_moved = 0

    def can_move(self, fut, eat):
        return True

    def move(self, fut):
        self.pos = fut
        self.times_moved += 1


class Pawn(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♙'
        if colour == 'Black':
            self.model = '♟'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        if self.colour == 'White':
            if eat:
                if (cur[0] == fut[0] + 1 or cur[0] == fut[0] - 1) and cur[1] == fut[1] + 1:
                    return True
                else:
                    print('Пешки так не атакуют!')
                    return False
            if self.times_moved == 0:
                if cur[1] - fut[1] in (1, 2) and cur[0] == fut[0]:
                    return True
            else:
                if cur[1] - fut[1] == 1 and cur[0] == fut[0]:
                    return True
                elif cur[1] - fut[1] == 2:
                    print('Это не первый ход пешки!')
                    return False

        if self.colour == 'Black':
            if eat:
                if (cur[0] == fut[0] + 1 or cur[0] == fut[0] - 1) and cur[1] == fut[1] - 1:
                    return True
                else:
                    print('Пешки так не атакуют!')
                    return False
            if self.times_moved == 0:
                if fut[1] - cur[1] in (1, 2) and cur[0] == fut[0]:
                    return True
            else:
                if fut[1] - cur[1] == 1 and cur[0] == fut[0]:
                    return True
                elif fut[1] - cur[1] == 2:
                    print('Это не первый ход пешки!')
                    return False

        print('Пешка не может так сходить!')
        return False


class Knight(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♘'
        if colour == 'Black':
            self.model = '♞'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        if (cur[0] - fut[0]) ** 2 + (cur[1] - fut[1]) ** 2 == 5:
            return True
        else:
            print('Конь не может так сходить!')
            return False


class Bishop(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♗'
        if colour == 'Black':
            self.model = '♝'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        if abs(cur[0] - fut[0]) == abs(cur[1] - fut[1]):
            return True
        else:
            print('Слон не может так сходить!')
            return False


class Rook(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♖'
        if colour == 'Black':
            self.model = '♜'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        if cur[0] == fut[0] or cur[1] == fut[1]:
            return True
        else:
            print('Ладья не может так сходить!')
            return False


class Queen(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♕'
        if colour == 'Black':
            self.model = '♛'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        if cur[0] == fut[0] or cur[1] == fut[1] or abs(cur[0] - fut[0]) == abs(cur[1] - fut[1]):
            return True
        else:
            print('Ферзь не может так сходить!')
            return False


class King(Piece):
    def __init__(self, h, v, colour):
        super().__init__(h, v, colour)
        if colour == 'White':
            self.model = '♔'
        if colour == 'Black':
            self.model = '♚'

    def can_move(self, fut, eat):
        cur = (tr(self.pos[0]), tr(self.pos[1]))
        fut = (tr(fut[0]), tr(fut[1]))
        rad = (sqrt((cur[0] - fut[0]) ** 2 + (cur[1] - fut[1]) ** 2) <= sqrt(2))
        if (cur[0] == fut[0] or cur[1] == fut[1] or abs(cur[0] - fut[0]) == abs(cur[1] - fut[1])) and rad:
            return True
        else:
            print('Король не может так сходить!')
            return False


def text_checker(text):
    try:
        a, b = text.split()
    except:
        print('Ошибка ввода!')
        return False
    lets = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    digs = ('1', '2', '3', '4', '5', '6', '7', '8')
    if len(a) != 2 or len(b) != 2:
        print('Ошибка ввода!')
        return False
    elif a[0] not in lets or b[0] not in lets or a[1] not in digs or b[1] not in digs:
        print('Ошибка ввода!')
        return False
    else:
        return True


class Board(object):
    def __init__(self):
        self.pieces = [Pawn('A', '2', 'Black'), Pawn('B', '2', 'Black'), Pawn('C', '2', 'Black'),
                       Pawn('D', '2', 'Black'), Pawn('E', '2', 'Black'), Pawn('F', '2', 'Black'),
                       Pawn('G', '2', 'Black'), Pawn('H', '2', 'Black'), Rook('A', '1', 'Black'),
                       Rook('H', '1', 'Black'), Knight('B', '1', 'Black'), Knight('G', '1', 'Black'),
                       Bishop('C', '1', 'Black'), Bishop('F', '1', 'Black'), King('D', '1', 'Black'),
                       Queen('E', '1', 'Black'), Pawn('A', '7', 'White'), Pawn('B', '7', 'White'),
                       Pawn('C', '7', 'White'), Pawn('D', '7', 'White'), Pawn('E', '7', 'White'),
                       Pawn('F', '7', 'White'), Pawn('G', '7', 'White'), Pawn('H', '7', 'White'),
                       Rook('A', '8', 'White'), Rook('H', '8', 'White'), Knight('B', '8', 'White'),
                       Knight('G', '8', 'White'), Bishop('C', '8', 'White'), Bishop('F', '8', 'White'),
                       King('D', '8', 'White'), Queen('E', '8', 'White')]

        self.turn = 'White'
        self.count = 0

    def turn_changer(self):
        if self.turn == 'White':
            self.turn = 'Black'
        elif self.turn == 'Black':
            self.turn = 'White'

    def finder(self, pos):
        for i in range(len(self.pieces)):
            if self.pieces[i].pos == pos:
                return i
        return 'gg'

    def piece_finder(self, cur, fut, ftype):
        bx = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        by = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
        xmin = min(tr(cur[0]), tr(fut[0]))
        xmax = max(tr(cur[0]), tr(fut[0]))
        ymin = min(tr(cur[1]), tr(fut[1]))
        ymax = max(tr(cur[1]), tr(fut[1]))
        poses = []
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                poses.append((x, y))

        tp = [tr(cur[0]), tr(cur[1])]
        fp = [tr(fut[0]), tr(fut[1])]

        gpos = []
        found = []
        trpos = []
        if ftype == Knight:
            return False

        if ftype == Rook:
            gpos = poses

        if ftype in (Pawn, King):
            if abs(tp[0] - fp[0]) == abs(tp[1] - fp[1]):
                return False
            else:
                gpos = poses

        if ftype == Bishop:
            for i in poses:
                if abs(tp[0] - list(i)[0]) == abs(tp[1] - list(i)[1]):
                    gpos.append(i)

        if ftype == Queen:
            if abs(tp[0] - fp[0]) == abs(tp[1] - fp[1]):
                for i in poses:
                    if abs(tp[0] - list(i)[0]) == abs(tp[1] - list(i)[1]):
                        gpos.append(i)
            else:
                gpos = poses

        for i in gpos:
            trpos.append((bx[i[0]], by[i[1]]))
        trpos.remove(cur)
        trpos.remove(fut)

        for i in trpos:
            found.append(self.finder(i))

        for i in found:
            if i != 'gg':
                return True
        return False

    def checker(self, cur, fut):
        logic = {'Empty beg': False, 'Empty fin': False, 'Piece can': False, 'Same colour': False, 'Move': False,
                 'Del future': False, 'Wrong turn': False}
        idc = self.finder(cur)
        idf = self.finder(fut)
        if idc == 'gg':
            logic['Empty beg'] = True

        if not logic['Empty beg'] and self.pieces[idc].colour != self.turn:
            logic['Wrong turn'] = True

        if not logic['Wrong turn'] and idf == 'gg':
            logic['Empty fin'] = True

        eat = not logic['Empty fin']
        if not logic['Wrong turn'] and not logic['Empty beg'] and self.pieces[idc].can_move(fut, eat):
            if not self.piece_finder(cur, fut, type(self.pieces[idc])):
                logic['Piece can'] = True
            else:
                print('На пути фигуры находится другая!')

        if logic['Piece can'] and not logic['Empty fin']:
            if self.pieces[idc].colour == self.pieces[idf].colour:
                logic['Same colour'] = True

        if logic['Piece can'] and not logic['Same colour']:
            logic['Move'] = True

        if logic['Move'] and not logic['Empty fin']:
            logic['Del future'] = True

        return logic

    def king_is_dead(self):
        kc = 0
        for i in self.pieces:
            if type(i) == King:
                kc += 1
        if kc != 2:
            return True
        else:
            return False

    def move(self, text):
        if text_checker(text):
            current, future = text.split()
            current = (current[0], current[1])
            future = (future[0], future[1])
            idc = self.finder(current)
            idf = self.finder(future)
            logi = self.checker(current, future)
            if logi['Empty beg']:
                print('Начальная позиция пуста!')
            if logi['Wrong turn']:
                print('Сейчас ход другого игрока!')
            if logi['Same colour']:
                print('Фигуры одного цвета!')
            if logi['Move']:
                self.pieces[idc].move(future)
                self.turn_changer()
                self.count += 1
                # self.informater()
            if logi['Del future']:
                self.pieces.pop(idf)

    def show(self):
        field = np.array([['▭'] * 8] * 8)
        for piece in self.pieces:
            field[tr(piece.pos[1])][tr(piece.pos[0])] = piece.model
        h = [[1], [2], [3], [4], [5], [6], [7], [8]]
        v = ['■', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '■']
        v = '  '.join(v)
        field = np.hstack([h, field, h])
        print(v)
        for i in range(8):
            for j in range(10):
                print(field[i][j], end='')
                if j != 9:
                    print('  ', end='')
            print()
        print(v)
        print()


ingame = True
board = Board()
print('Добро пожаловать!')
print('Если хотите остановить игру, введите "stop"')
print('Все ходы вводятся в формате "Начальная позиция пробел Конечная поизция"')
print('Пример: "С7 С5"')
print()
while ingame:
    board.show()
    text = input('Введите ход: ')
    if 'stop' in text:
        break
    board.move(text)
    if board.king_is_dead():
        ingame = False
        board.show()
        print('Игра окончена, король умер!')