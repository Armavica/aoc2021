import fileinput as fi

class Packet:
    def __init__(self, version, typeid, contents):
        self.version = version
        self.type = ['+', '*', 'min', 'max', 'int', '>', '<', '=='][typeid]
        self.contents = contents

    def eval(self):
        if self.type == '+':
            return sum(p.eval() for p in self.contents)
        elif self.type == '*':
            n = 1
            for p in self.contents:
                n *= p.eval()
            return n
        elif self.type == 'min':
            return min(p.eval() for p in self.contents)
        elif self.type == 'max':
            return max(p.eval() for p in self.contents)
        elif self.type == 'int':
            return self.contents
        elif self.type == '>':
            return int(self.contents[0].eval() > self.contents[1].eval())
        elif self.type == '<':
            return int(self.contents[0].eval() < self.contents[1].eval())
        elif self.type == '==':
            return int(self.contents[0].eval() == self.contents[1].eval())

    def from_bytes(bts):
        version = int(bts[:3], 2)
        typeid = int(bts[3:6], 2)
        if typeid == 4:
            # literal
            i = 6
            n = int(bts[i+1:i+5], 2)
            while bts[i] == '1':
                i += 5
                n = 16 * n + int(bts[i+1:i+5], 2)
            return bts[i+5:], Packet(version, typeid, n)
        # operator
        lengthtypeid = bts[6]
        if lengthtypeid == '0':
            length = int(bts[7:22], 2)
            subpackets = []
            bts = bts[22:]
            oglength = len(bts)
            while len(bts) + length > oglength:
                bts, p = Packet.from_bytes(bts)
                subpackets.append(p)
            return bts, Packet(version, typeid, subpackets)
        else:
            number = int(bts[7:18], 2)
            subpackets = []
            bts = bts[18:]
            for _ in range(number):
                bts, p = Packet.from_bytes(bts)
                subpackets.append(p)
            return bts, Packet(version, typeid, subpackets)

def sum_versions(p):
    if p.type == 'int':
        return p.version
    return p.version + sum(sum_versions(p) for p in p.contents)


_, res = Packet.from_bytes(''.join(f'{x:08b}' for x in bytes.fromhex(next(fi.input()))))

print(sum_versions(res))
print(res.eval())

