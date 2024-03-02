"""

Author : Elsie Rezinold Yedida


"""

from random import randrange
import random 
from myhdl import *

@block
def RF(i_clk,i_rst_n,i_reg1,i_reg2,i_wr_reg,i_data_in,i_wr_control,o_data1,o_data2):
    
    mem = [Signal(intbv(0, min=-2**31, max=2**31 -1)) for i in range(32)]
    #print mem


    @always_seq(i_clk.posedge,reset=i_rst_n)
    def logic():
        if i_wr_control == 1:
            mem[int(i_wr_reg)].next = i_data_in
    @always_comb
    def logic_2():
        o_data1.next = mem[int(i_reg1)]
    @always_comb        
    def logic_3():
        o_data2.next = mem[int(i_reg2)]        
        

    return logic,logic_2,logic_3




