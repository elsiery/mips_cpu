"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *

@block
def CR_DEC(i_opcode,i_funct,i_nop,o_swap_rs_sh,o_swap_rs_rt,o_swap_rt_imm,o_signed_ext,o_mem_rd,o_rg_write,o_byte_rd,o_signed_mem_rd
       ,o_2byte_rd,o_4byte_rd,o_mem_wr,o_byte_wr,o_2byte_wr,o_4byte_wr,o_opcode,o_funct,o_rg_write_imm):
    @always_comb
    def logic():
        o_swap_rs_sh.next = 0       #replace rs with shamt
        o_swap_rs_rt.next = 0       #swap rs and rt
        o_swap_rt_imm.next = 0      #swap rt with imm
        o_signed_ext.next = 0       #sign extend imm
        o_mem_rd.next = 0           #reading from memory
        o_rg_write.next = 0         #writing back to registers
        o_byte_rd.next = 0          #read just a byte
        o_signed_mem_rd.next = 0    #sign extend the mem_read
        o_2byte_rd.next = 0         #read 2 byte
        o_4byte_rd.next = 0         #read 4 byte
        o_mem_wr.next = 0           #writing to mem
        o_byte_wr.next = 0          #writing a byte
        o_2byte_wr.next = 0         #writing 2 byte
        o_4byte_wr.next = 0         #writing 4 byte
        o_rg_write_imm.next = 0

        if i_nop == 1:
            o_swap_rs_sh.next = 0
            o_swap_rs_rt.next = 0
            o_swap_rt_imm.next = 0
            o_signed_ext.next = 0
            o_mem_rd.next = 0
            o_rg_write.next = 0
            o_byte_rd.next = 0
            o_signed_mem_rd.next = 0
            o_2byte_rd.next = 0
            o_4byte_rd.next = 0
            o_mem_wr.next = 0
            o_byte_wr.next = 0
            o_2byte_wr.next = 0
            o_4byte_wr.next = 0
            o_rg_write_imm.next = 0
        elif (i_opcode == 0): #r-format
            o_rg_write.next = 1
            if ((i_funct == 0) | (i_funct == 2) | (i_funct == 3)):
                o_swap_rs_sh.next = 1
                o_swap_rs_rt.next = 1
            elif ((i_funct == 4) | (i_funct == 6) | (i_funct == 7)):
                o_swap_rs_sh.next = 0
                o_swap_rs_rt.next = 1
        elif ((i_opcode >= 8) & (i_opcode <= 15)): #i-format 
            o_swap_rt_imm.next = 1
            o_rg_write_imm.next = 1
            if ((i_opcode == 12)|(i_opcode==13)|(i_opcode==14)):
                o_signed_ext.next = 0
            else:
                o_signed_ext.next = 1
        elif ((i_opcode >= 32) & (i_opcode <= 37) & (i_opcode != 35)):   #i_format load
            o_swap_rt_imm.next = 1
            o_signed_ext.next = 1
            o_mem_rd.next = 1
            #o_rg_write.next = 1
            if (i_opcode == 32):
                o_byte_rd.next = 1
                o_signed_mem_rd.next = 1
            elif (i_opcode==33):
                o_2byte_rd.next = 1
                o_signed_mem_rd.next = 1
            elif (i_opcode==34):
                o_4byte_rd.next = 1
                o_signed_mem_rd.next = 1
            elif (i_opcode == 36):
                o_byte_rd.next = 1
                o_signed_mem_rd.next = 0
            elif (i_opcode==37):
                o_2byte_rd.next = 1
                o_signed_mem_rd.next = 0
        elif ((i_opcode==40)|(i_opcode==41)|(i_opcode==43)): #i_format store
            o_swap_rt_imm.next = 1
            o_signed_ext.next = 1
            o_mem_wr.next = 1
            if (i_opcode == 40):
                o_byte_wr.next = 1
            elif (i_opcode==41):
                o_2byte_wr.next = 1
            elif (i_opcode==43):
                o_4byte_wr.next = 1


    @always_comb
    def pass_logic():
        o_opcode.next   =   i_opcode
        o_funct.next    =   i_funct

    return logic,pass_logic

            

