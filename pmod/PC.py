"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *
@block
def PC(i_clk,i_rst_n,i_start,o_pc):
    r_now = Signal(intbv(0)[1:])
    @always_seq(i_clk.posedge,reset=i_rst_n)
    def update():
        if (i_start==0):
            o_pc.next = 0
            r_now.next=0
        elif ((i_start==1)&(r_now == 0)):
            o_pc.next = 0
            r_now.next = 1
        elif ((i_start==1)&(r_now==1)):
            o_pc.next = o_pc+1


    return update

