"""

Author : Elsie Rezinold Yedida


"""


from myhdl import *



@block
def WB(i_rg_wr,i_rg_wr_imm,i_mem_rd,i_rt,i_rd,i_alu_data,i_mem_rd_data,o_wb_addr,o_wb_cntrl,o_wb_data):
    @always_comb
    def cntrl():
        o_wb_cntrl.next =   i_rg_wr | i_mem_rd | i_rg_wr_imm
    @always_comb
    def wb_addr():
        o_wb_addr.next = 0
        if(i_rg_wr==1):
            o_wb_addr.next  =   i_rd
        elif((i_mem_rd==1)|(i_rg_wr_imm==1)):
            o_wb_addr.next  =   i_rt
    @always_comb
    def wb_data():
        o_wb_data.next = 0
        if((i_rg_wr==1)|(i_rg_wr_imm==1)):
            o_wb_data.next  =   i_alu_data
        elif(i_mem_rd==1):
            o_wb_data.next  =   i_mem_rd_data

    return cntrl,wb_addr,wb_data

