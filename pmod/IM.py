"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *




@block
def IM(i_pc,o_instruction,file):

    def load_program(ROM):
        
        program= file
        index = 0
        for line in open(program):
            if (line[0] == 1):
                temp = int(line[1:],2)
                temp1 = "10000000000000000000000000000000"
                temp1 = int(temp1,2)
                ROM[index] = -temp1+temp
            else:
                ROM[index] = int(line,2)
            index += 1

        return tuple(ROM)

    ROM = load_program([0] * 300)

    @always_comb
    def logic():
            o_instruction.next = ROM[int(i_pc)]
    return logic

