"""

Author : Elsie Rezinold Yedida


"""

import random
from myhdl import *
@block
def ALU(i_op_1, i_op_2, i_alu_op,o_exception, o_result):
    
    w_result = Signal(intbv(0,min = -2**31,max=2**31 -1))
    w_concat_1 = Signal(intbv(0,min=-2**15,max=2**15 -1))
    w_concat = Signal(intbv(0)[17:])
    @always_comb
    def logic():
        if (i_alu_op==0):
            if (i_op_2 >0):                    #((i_alu_op == 0) | (i_alu_op == 4)):
                w_result.next = i_op_1 << i_op_2
        elif (i_alu_op==1):                     #((i_alu_op == 2) | (i_alu_op == 6)):
            if (i_op_2 >0):
                w_result.next = i_op_1 >> i_op_2
        elif (i_alu_op==2):                     #((i_alu_op == 3) | (i_alu_op == 7)):
            if (i_op_2 >0):
                w_result.next = i_op_1.signed() >> i_op_2
        elif (i_alu_op==3):                     #((i_alu_op == 32)|(i_op_code==8)):
            w_result.next = i_op_1.signed() + i_op_2.signed()
        elif (i_alu_op==4):                     #((i_alu_op == 33)|(i_op_code == 9)|(i_op_code==32)|(i_op_code==33)|(i_op_code==34)|(i_op_code==36)|(i_op_code==37)|(i_op_code==40)|(i_op_code==41)|(i_op_code==43)):
            w_result.next = i_op_1 + i_op_2
        elif (i_alu_op==5):                     #i_alu_op == 34:
            w_result.next = i_op_1.signed() - i_op_2.signed()
        elif (i_alu_op==6):                     #i_alu_op == 35:
            w_result.next = i_op_1 - i_op_2
        elif (i_alu_op==7):                     #((i_alu_op == 36)|(i_op_code==12)):
            w_result.next = i_op_1 & i_op_2
        elif (i_alu_op==8):                     #((i_alu_op == 37)|(i_op_code==13)):
            w_result.next = i_op_1 | i_op_2
        elif (i_alu_op==9):                     #((i_alu_op == 38)|(i_op_code==14)):
            w_result.next = i_op_1 ^ i_op_2
        elif (i_alu_op==10):                    #i_alu_op == 39:
            w_result.next = ~(i_op_1 | i_op_2)
        elif (i_alu_op==11):                    #((i_alu_op == 42)|(i_op_code==10)):
            if i_op_1.signed() < i_op_2.signed():
                w_result.next = 1
            else:
                w_result.next = 0
        elif (i_alu_op==12):                    #((i_alu_op == 43)|(i_op_code==11)):
            if i_op_1 < i_op_2:
                w_result.next = 1
            else:
                w_result.next = 0
        elif(i_alu_op==13):                     #(i_op_code==15):
            w_result.next = i_op_2 << 16
        else:
            w_result.next = 0 


    @always_comb
    def exception_detect():
        if ((i_alu_op == 3)):
            if((i_op_1.signed()+i_op_2.signed() > 2147483647) | (i_op_1.signed()+i_op_2.signed() < -2147483648)):
                o_exception.next = 1
            else:
                o_exception.next = 0
        elif ((i_alu_op == 5)):
            if((i_op_1.signed()-i_op_2.signed() > 2147483647) | (i_op_1.signed()-i_op_2.signed() < -2147483648)):
                o_exception.next = 1
            else:
                o_exception.next = 0
        else:
            o_exception.next = 0

    @always_comb
    def final_result():
        o_result.next = w_result

    return logic,exception_detect,final_result

