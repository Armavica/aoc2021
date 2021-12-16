import fileinput as fi
from math import prod

OPS = [
    sum,
    prod,
    min,
    max,
    None,
    lambda x: int(x[0] > x[1]),
    lambda x: int(x[0] < x[1]),
    lambda x: int(x[0] == x[1]),
]


class PacketParser:
    def __init__(self, data):
        self.binary = "".join(f"{x:08b}" for x in bytes.fromhex(data))
        self.pos = 0
        self.versions = 0

    def readint(self, n):
        self.pos += n
        return int(self.binary[self.pos - n : self.pos], 2)

    def readpacket(self):
        version = self.readint(3)
        self.versions += version
        typeid = self.readint(3)
        if typeid == 4:
            n = 0
            while True:
                cont = self.readint(1)
                n = (n << 4) + self.readint(4)
                if not cont:
                    return n
        if self.readint(1):
            vals = [self.readpacket() for _ in range(self.readint(11))]
        else:
            # addition order is important because readint modifies pos
            limit = self.readint(15) + self.pos
            vals = []
            while self.pos < limit:
                vals.append(self.readpacket())
        return OPS[typeid](vals)


pp = PacketParser(next(fi.input()))
result = pp.readpacket()
print(pp.versions)
assert pp.versions == 947
print(result)
assert result == 660797830937
