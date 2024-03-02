"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *

@block
def DM(clk,rst_n,i_byte_rd,i_2byte_rd,i_4byte_rd,i_mem_rd,i_se_mem_rd,i_address,o_rd_data,i_byte_wr,
    i_2byte_wr,i_4byte_wr,i_mem_wr,i_wr_data):

    mem = [Signal(intbv(0, min=-(2**31), max=2**31-1)) for i in range(1024)]
    w_rd_data_byte = Signal(intbv(0,min=0,max=2**8 -1))
    w_rd_data_2byte = Signal(intbv(0,min=0,max=2**16 -1))
    w_rd_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    
    @always_seq(clk.posedge,reset=rst_n)
    def write_logic():
        if i_mem_wr == 1:
            if i_byte_wr == 1:
                mem[int(i_address)][8:0].next = i_wr_data[8:0]
            elif i_2byte_wr == 1:
                mem[int(i_address)][16:0].next = i_wr_data[16:0]
            elif i_4byte_wr == 1:
                mem[int(i_address)].next = i_wr_data


    @always_comb
    def read_logic_1():
        w_rd_data_byte.next = 0
        w_rd_data_2byte.next = 0
        w_rd_data.next = 0
        if i_mem_rd == 1:
            if i_byte_rd == 1:
                w_rd_data_byte.next = mem[int(i_address)][8:0]
                if i_se_mem_rd == 1:
                    w_rd_data.next = w_rd_data_byte.signed()
                else:
                    w_rd_data.next = concat(intbv(0)[25:],w_rd_data_byte)
            elif i_2byte_rd == 1:
                w_rd_data_2byte.next = mem[int(i_address)][16:0]
                if i_se_mem_rd == 1:
                    w_rd_data.next = w_rd_data_2byte.signed()
                else:
                    w_rd_data.next = concat(intbv(0)[17:],w_rd_data_2byte)
            elif i_4byte_rd == 1:
                w_rd_data.next = mem[int(i_address)]

    @always_comb
    def read_logic_2():
        o_rd_data.next  =   w_rd_data

                    

    return write_logic,read_logic_1,read_logic_2

