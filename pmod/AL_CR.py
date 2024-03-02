"""

Author : Elsie Rezinold Yedida


"""


import random
from random import randrange
from myhdl import *


@block
def AL_CR(i_op_code,i_funct_field,o_alu_op):
    

    @always_comb
    def logic():
        if (((i_funct_field == 0) | (i_funct_field == 4))&(i_op_code==0)):
            o_alu_op.next = 0
        elif (((i_funct_field == 2) | (i_funct_field == 6))&(i_op_code ==0)):
            o_alu_op.next = 1
        elif (((i_funct_field == 3) | (i_funct_field == 7))&(i_op_code==0)):
            o_alu_op.next = 2
        elif (((i_funct_field == 32)&(i_op_code==0))|(i_op_code==8)):
            o_alu_op.next = 3
        elif (((i_funct_field == 33)&(i_op_code==0))|(i_op_code == 9)|((i_op_code>=32)&(i_op_code<=37))|(i_op_code==40)|(i_op_code==41)|(i_op_code==43)):
            o_alu_op.next = 4
        elif ((i_funct_field == 34)&(i_op_code==0)):
            o_alu_op.next = 5
        elif ((i_funct_field == 35)&(i_op_code==0)):
            o_alu_op.next = 6
        elif (((i_funct_field == 36)&(i_op_code==0))|(i_op_code==12)):
            o_alu_op.next = 7
        elif (((i_funct_field == 37)&(i_op_code==0))|(i_op_code==13)):
            o_alu_op.next = 8
        elif (((i_funct_field == 38)&(i_op_code==0))|(i_op_code==14)):
            o_alu_op.next = 9
        elif ((i_funct_field == 39)&(i_op_code==0)):
            o_alu_op.next = 10
        elif (((i_funct_field == 42)&(i_op_code==0))|(i_op_code==10)):
            o_alu_op.next = 11
        elif (((i_funct_field == 43)&(i_op_code==0))|(i_op_code==11)):
            o_alu_op.next = 12
        elif (i_op_code==15):
            o_alu_op.next = 13
        else:
            o_alu_op.next = 14
    return logic
          

