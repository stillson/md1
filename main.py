#!/usr/bin/env python3


optree = {
    0b0000 : 'ADD',
    0b0001 : 'SUB',
    0b0010 : 'AND',
    0b0011 : 'OR',
    0b0100 : 'XOR',
    0b0101 : 'NOT',
    0b0110 : 'LD',
    0b0111 : 'ST',
    0b1000 : 'MOV',
    0b1001 : ['SL', 'SR'],
    0b1010 : 'LIL',
    0b1011 : 'LIH',
    0b1100 : 'JMP',
    0b1101 : 'JRF',
    0b1110 : 'JRB',
    0b1111 : 'HCF'
}

def h_nib(x):
    return (x & 0xf0) >> 4

def l_nib(x):
    return (x & 0xf0)

class Md1:
    def __init__(self, mem):
        self.mem = mem
        self.pc = 128
        self.reg = [0, 0, 0, 0]
        self.input = 0
        self.output = 0


    def cycle(self):
        self.print_reg()
        self.print_op(self.pc)
        self.execute_op(self.pc)


    def print_reg(self):
        print("r0/z", self.reg[0])
        print("r1/a", self.reg[1])
        print("r2/o", self.reg[2])
        print("r3/p", self.reg[3])

    def print_op(self, pc):

        c_high = h_nib(self.mem[pc])

        print(optree[c_high])


    def execute_op(self, pc):

        c_hi = h_nib(self.mem[pc])
        c_lo = l_nib(self.mem[pc])

        def r1(x):
            return (x & 12) >> 2
        def r2(x):
            return x & 3

        if c_hi==0b0000:
            # add
            ra = r1(c_lo)
            rb = r2(c_lo)
            self.reg[ra] += self.reg[rb]


        elif c_hi==0b0001:
            # sub
            pass

        elif c_hi==0b0010:
            # and
            pass

        elif c_hi==0b0011:
            # or
            pass

        elif c_hi==0b0100:
            # xor
            pass

        elif c_hi==0b0101:
            # not
            pass

        if c_hi==0b0110:
            # ld - load
            pass

        if c_hi==0b0111:
            # st - store
            pass

        if c_hi==0b1000:
            # mov <should be synthetic?>
            pass

        if c_hi==0b1001:
            # shift
            pass

        if c_hi==0b1010:
            # lil (load imm)
            pass

        if c_hi==0b1011:
            # lih (load imm high)
            pass

        if c_hi==0b1100:
            # jmp (cond or not)
            pass

        if c_hi==0b1101:
            # jrf (cond)
            pass

        if c_hi==01110:
            # jrb (cond)
            pass

        if c_hi==0b1111:
            # hcf (halt and catch fire)
            pass


def main():

    try:
        mem = [0] * 256
        proc = Md1(mem)
        while True:
            proc.cycle()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()