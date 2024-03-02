"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *


@block
def SWAP(in1,in2,sel,out):
    @always_comb
    def logic():
        if sel == 1:
            out.next = in1
        else:
            out.next = in2
    return logic