"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *


@block
def FLOP(clk,rst_n,w,d):
    @always_seq(clk.posedge,reset=rst_n)
    def logic():
        d.next = w
    return logic


