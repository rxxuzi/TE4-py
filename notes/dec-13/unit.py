class UNIT:
    def nand(self, x1, x2):
        x0 = 1
        w0, w1, w2 = -1.5, 1, 1
        return 0 if x0 * w0 + x1 * w1 + x2 * w2 > 0 else 1

    def xor(self, a, b):
        a1 = self.nand(a, self.nand(a, b))
        b2 = self.nand(b, self.nand(a, b))
        return self.nand(a1, b2)

    def or_(self, a, b):
        return self.nand(self.nand(a, a), self.nand(b, b))

    def nor(self, a, b):
        return self.nand(self.or_(a, b), self.or_(a, b))

    def and_(self, a, b):
        return self.nand(self.nand(a, b), self.nand(a, b))


if __name__ == '__main__':
    u = UNIT()
    print(u.xor(0, 0))
    print(u.xor(0, 1))
    print(u.xor(1, 0))
    print(u.xor(1, 1))
