class ksort:

    def __init__(self):
        self.items = [0] * 107  # создаем итоговый архив с нанами
        self.letter_hash = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.ten_hash = {'0': 0, '1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80, '9': 90}
        self.one_hash = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def index(self, s):
        if len(s) > 3 or len(s) < 3:
            return -1
        count_hach = 0
        res = 0
        for i in s:
            count_hach += 1
            if i not in self.letter_hash and count_hach == 1:
                return -1
            if count_hach == 1:
                res = self.letter_hash[i]
            if i not in self.ten_hash and count_hach == 2:
                return -1
            if count_hach == 2:
                res += self.ten_hash[i]
            if i not in self.one_hash and count_hach == 3:
                return -1
            if count_hach == 3:
                res += self.one_hash[i]

        return res

    def add(self, s):
        if self.index(s) == -1:
            return False
        else:
            self.items[self.index(s)] = s
        return True


k = ksort()
uncorrect_values = ['a01', 'a02', 'a03', 'b33', 'c78', 'e45', 'f56', 'g89', 'h22']
res = []
for i in uncorrect_values:
    if k.add(i) == True:
        res.append(i)
print(res)
