"""

Author : Elsie Rezinold Yedida


"""

from myhdl import *



@block
def ID(i_instruction, o_opcode, o_rs,o_rt,o_rd,o_shamt,o_func,o_imm,o_nop):

    @always_comb
    def decode():
        o_opcode.next = int(i_instruction[32:26])
        o_rs.next     = int(i_instruction[26:21])       
        o_rt.next     = int(i_instruction[21:16])      
        o_rd.next     = int(i_instruction[16:11])     
        o_shamt.next  = int(i_instruction[11:6]) 
        o_func.next   = int(i_instruction[6:0])
        if (i_instruction[15]):
            temp = int("1000000000000000",2)
            temp1 = int(i_instruction[15:0])
            o_imm.next    = -temp+temp1
        else:
            o_imm.next = int(i_instruction[16:0])   


        if i_instruction == 0:
            o_nop.next = 1
        else: 
            o_nop.next = 0

    return decode
