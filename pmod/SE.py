"""

Author : Elsie Rezinold Yedida


"""


import random

from myhdl import *

@block
def SE(i_imm16, o_imm32,i_signed):
    
    @always_comb
    def logic():
        if i_signed == 1:
            o_imm32.next = i_imm16.signed()
        else:
            o_imm32.next = concat(intbv(0)[16:],i_imm16)
        

    return logic

