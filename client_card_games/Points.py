from deckCards import *
class Points:
    def __init__(self, args):
        self.card_list = args
        self._point_list = self.__dict_black_jack()
        self.point = self.__count_points()

    def __dict_black_jack(self):
        self._point_list = []
        for i in self.card_list:
            if i.value.isdigit():
                self._point_list.append(int(i.value))
            elif i.value == 'A':
                self._point_list.append((1, 11))
            else:
                self._point_list.append(10)
        return self._point_list

    def __count_points(self):
        point = 0
        self._point_list = sorted(self._point_list, key=lambda x: str(type(x)))
        for i in self._point_list:
            if type(i) == tuple and point + max(i) <= 21:
                point += max(i)
            elif type(i) == tuple and point + max(i) >= 21:
                point += min(i)
            else:
                point += i
        return point


