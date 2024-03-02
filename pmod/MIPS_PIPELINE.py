"""

Author : Elsie Rezinold Yedida


"""











from myhdl import *
from PC import PC
from IM import IM
from RF import RF
from CR_DEC import CR_DEC
from ID import ID
from AL_CR import AL_CR
from ALU import ALU
from DM import DM
from FLOP import FLOP
from SWAP import SWAP
from SE import SE
from WB import WB
pc = Signal(intbv(0)[10:])
w_instruction = Signal(intbv(0)[32:])
d_instruction = Signal(intbv(0)[32:])
opcode = Signal(intbv(0)[7:])
rs = Signal(intbv(0)[6:])
rt = Signal(intbv(0)[6:])
w_wb_wr_addr = Signal(intbv(0)[6:])
rd = Signal(intbv(0)[6:])
d_rt = Signal(intbv(0)[6:])
d_rd = Signal(intbv(0)[6:])
d2_rt = Signal(intbv(0)[6:])
d2_rd = Signal(intbv(0)[6:])
d3_rt = Signal(intbv(0)[6:])
d3_rd = Signal(intbv(0)[6:])


shamt = Signal(intbv(0)[6:])
func = Signal(intbv(0)[7:])
imm = Signal(intbv(0,min=-2**15,max=2**15 -1))
imm_32 = Signal(intbv(0,min=-2**31,max=2**31 -1))
nop = Signal(intbv(0)[1:])
w_opcode = Signal(intbv(0)[7:])
w_funct = Signal(intbv(0)[7:])
d_opcode = Signal(intbv(0)[7:])
d_funct = Signal(intbv(0)[7:])
w_alu_op = Signal(intbv(0,min=0,max=15))
w_rs_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_rt_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_rt_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d2_rt_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_wb_wr_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_mem_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_mem_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_wb_wr_enable = Signal(intbv(0)[1:])
w_rs_or_shamt_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_op1_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_op2_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_op1_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_op2_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d2_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
w_exception = Signal(intbv(0)[1:])
w_rt_or_imm_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
d_issue = Signal(intbv(0)[1:])



w_swap_rs_sh,w_swap_rs_rt,w_swap_rt_imm,w_signed_ext,w_mem_rd,w_rg_write,w_byte_rd,w_signed_mem_rd,w_2byte_rd,w_4byte_rd,w_mem_wr,w_byte_wr,w_2byte_wr,w_4byte_wr = [Signal(intbv(0)[1:]) for i in range(14)]

d_mem_rd,d_rg_write,d_byte_rd,d_signed_mem_rd,d_2byte_rd,d_4byte_rd,d_mem_wr,d_byte_wr,d_2byte_wr,d_4byte_wr = [Signal(intbv(0)[1:]) for i in range(10)]
d2_mem_rd,d2_rg_write,d2_byte_rd,d2_signed_mem_rd,d2_2byte_rd,d2_4byte_rd,d2_mem_wr,d2_byte_wr,d2_2byte_wr,d2_4byte_wr = [Signal(intbv(0)[1:]) for i in range(10)]
d3_rg_write= Signal(intbv(0)[1:])
w_rg_write_imm = Signal(intbv(0)[1:])
d_rg_write_imm = Signal(intbv(0)[1:])
d2_rg_write_imm = Signal(intbv(0)[1:])
d3_rg_write_imm = Signal(intbv(0)[1:])
d3_mem_rd = Signal(intbv(0)[1:])

@block
def MIPS(clk,rst_n,issue,start,program=None):
    """
    pc = Signal(intbv(0)[7:])
    w_instruction = Signal(intbv(0)[32:])
    d_instruction = Signal(intbv(0)[32:])
    opcode = Signal(intbv(0)[7:])
    rs = Signal(intbv(0)[6:])
    rt = Signal(intbv(0)[6:])
    w_wb_wr_addr = Signal(intbv(0)[6:])
    rd = Signal(intbv(0)[6:])
    d_rt = Signal(intbv(0)[6:])
    d_rd = Signal(intbv(0)[6:])
    d2_rt = Signal(intbv(0)[6:])
    d2_rd = Signal(intbv(0)[6:])
    d3_rt = Signal(intbv(0)[6:])
    d3_rd = Signal(intbv(0)[6:])


    shamt = Signal(intbv(0)[6:])
    func = Signal(intbv(0)[7:])
    imm = Signal(intbv(0)[16:])
    imm_32 = Signal(intbv(0)[32:])
    nop = Signal(intbv(0)[1:])
    w_opcode = Signal(intbv(0)[7:])
    w_funct = Signal(intbv(0)[7:])
    d_opcode = Signal(intbv(0)[7:])
    d_funct = Signal(intbv(0)[7:])
    w_alu_op = Signal(intbv(0,min=0,max=15))
    w_rs_data = Signal(intbv(0)[32:])
    w_rt_data = Signal(intbv(0)[32:])
    d_rt_data = Signal(intbv(0)[32:])
    d2_rt_data = Signal(intbv(0)[32:])
    w_wb_wr_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    w_mem_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    d_mem_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    w_wb_wr_enable = Signal(intbv(0)[1:])
    w_rs_or_shamt_data = Signal(intbv(0)[32:])
    w_op1_data = Signal(intbv(0)[32:])
    w_op2_data = Signal(intbv(0)[32:])
    d_op1_data = Signal(intbv(0)[32:])
    d_op2_data = Signal(intbv(0)[32:])
    w_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    d_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    d2_alu_out_data = Signal(intbv(0,min=-2**31,max=2**31 -1))
    w_exception = Signal(intbv(0)[1:])
    w_rt_or_imm_data = Signal(intbv(0)[32:])
    d_issue = Signal(intbv(0)[1:])
    


    w_swap_rs_sh,w_swap_rs_rt,w_swap_rt_imm,w_signed_ext,w_mem_rd,w_rg_write,w_byte_rd,w_signed_mem_rd,w_2byte_rd,w_4byte_rd,w_mem_wr,w_byte_wr,w_2byte_wr,w_4byte_wr = [Signal(intbv(0)[1:]) for i in range(14)]
   
    d_mem_rd,d_rg_write,d_byte_rd,d_signed_mem_rd,d_2byte_rd,d_4byte_rd,d_mem_wr,d_byte_wr,d_2byte_wr,d_4byte_wr = [Signal(intbv(0)[1:]) for i in range(10)]
    d2_mem_rd,d2_rg_write,d2_byte_rd,d2_signed_mem_rd,d2_2byte_rd,d2_4byte_rd,d2_mem_wr,d2_byte_wr,d2_2byte_wr,d2_4byte_wr = [Signal(intbv(0)[1:]) for i in range(10)]
    d3_rg_write= Signal(intbv(0)[1:])
    w_rg_write_imm = Signal(intbv(0)[1:])
    d_rg_write_imm = Signal(intbv(0)[1:])
    d2_rg_write_imm = Signal(intbv(0)[1:])
    d3_rg_write_imm = Signal(intbv(0)[1:])
    d3_mem_rd = Signal(intbv(0)[1:])
    """
    #Fetch stage
    program_counter         = PC(clk,rst_n,start,pc)
    instruction_memory      = IM(pc,w_instruction,program)
    ##pipe1##
    if_pipe                 = FLOP(clk,rst_n,w_instruction,d_instruction)
    #Decode and control stage 
    decode                  = ID(d_instruction,opcode,rs,rt,rd,shamt,func,imm,nop)
    rf                      = RF(clk,rst_n,rs,rt,w_wb_wr_addr,w_wb_wr_data,w_wb_wr_enable,w_rs_data,w_rt_data)
    decode_control          = CR_DEC(opcode,func,nop,w_swap_rs_sh,w_swap_rs_rt,w_swap_rt_imm,w_signed_ext,w_mem_rd,w_rg_write,w_byte_rd,w_signed_mem_rd
    ,w_2byte_rd,w_4byte_rd,w_mem_wr,w_byte_wr,w_2byte_wr,w_4byte_wr,w_opcode,w_funct,w_rg_write_imm)
    swap1                   = SWAP(shamt,w_rs_data,w_swap_rs_sh,w_rs_or_shamt_data)
    sign_extented_imm       = SE(imm,imm_32,w_signed_ext)
    swap2                   = SWAP(imm_32,w_rt_data,w_swap_rt_imm,w_rt_or_imm_data)
    swap3                   = SWAP(w_rt_or_imm_data,w_rs_or_shamt_data,w_swap_rs_rt,w_op1_data)
    swap4                   = SWAP(w_rs_or_shamt_data,w_rt_or_imm_data,w_swap_rs_rt,w_op2_data)
    ##pipe2##
    id_pipe1                = FLOP(clk,rst_n,w_opcode,d_opcode)
    id_pipe2                = FLOP(clk,rst_n,w_funct,d_funct)
    id_pipe3                = FLOP(clk,rst_n,w_op1_data,d_op1_data)
    id_pipe4                = FLOP(clk,rst_n,w_op2_data,d_op2_data)
    id_pipe5                = FLOP(clk,rst_n,w_byte_rd,d_byte_rd)
    id_pipe6                = FLOP(clk,rst_n,w_2byte_rd,d_2byte_rd)
    id_pipe7                = FLOP(clk,rst_n,w_4byte_rd,d_4byte_rd)
    id_pipe8                = FLOP(clk,rst_n,w_byte_wr,d_byte_wr)
    id_pipe9                = FLOP(clk,rst_n,w_2byte_wr,d_2byte_wr)
    id_pipe10               = FLOP(clk,rst_n,w_4byte_wr,d_4byte_wr)
    id_pipe11               = FLOP(clk,rst_n,w_mem_rd,d_mem_rd)
    id_pipe12               = FLOP(clk,rst_n,w_signed_mem_rd,d_signed_mem_rd)
    id_pipe13               = FLOP(clk,rst_n,w_mem_wr,d_mem_wr)
    id_pipe14               = FLOP(clk,rst_n,w_rt_data,d_rt_data)
    id_pipe15               = FLOP(clk,rst_n,w_rg_write,d_rg_write)
    id_pipe16               = FLOP(clk,rst_n,rt,d_rt)
    id_pipe17               = FLOP(clk,rst_n,rd,d_rd)
    id_pipe18               = FLOP(clk,rst_n,w_rg_write_imm,d_rg_write_imm)


    ##Alu stage
    alu_control             = AL_CR(d_opcode,d_funct,w_alu_op)
    alu                     = ALU(d_op1_data, d_op2_data, w_alu_op,w_exception, w_alu_out_data)
    ##pipe3##
    exe_pipe1               = FLOP(clk,rst_n,w_alu_out_data,d_alu_out_data)
    exe_pipe2               = FLOP(clk,rst_n,d_byte_rd,d2_byte_rd)
    exe_pipe3               = FLOP(clk,rst_n,d_2byte_rd,d2_2byte_rd)
    exe_pipe4               = FLOP(clk,rst_n,d_4byte_rd,d2_4byte_rd)
    exe_pipe5               = FLOP(clk,rst_n,d_byte_wr,d2_byte_wr)
    exe_pipe6               = FLOP(clk,rst_n,d_2byte_wr,d2_2byte_wr)
    exe_pipe7               = FLOP(clk,rst_n,d_4byte_wr,d2_4byte_wr)
    exe_pipe8               = FLOP(clk,rst_n,d_mem_rd,d2_mem_rd)
    exe_pipe9               = FLOP(clk,rst_n,d_signed_mem_rd,d2_signed_mem_rd)
    exe_pipe10              = FLOP(clk,rst_n,d_mem_wr,d2_mem_wr)
    exe_pipe11              = FLOP(clk,rst_n,d_rt_data,d2_rt_data)
    exe_pipe12              = FLOP(clk,rst_n,d_rg_write,d2_rg_write)
    exe_pipe13               = FLOP(clk,rst_n,d_rt,d2_rt)
    exe_pipe14               = FLOP(clk,rst_n,d_rd,d2_rd)
    exe_pipe15              = FLOP(clk,rst_n,w_exception,d_issue)
    exe_pipe16              = FLOP(clk,rst_n,d_rg_write_imm,d2_rg_write_imm)


    #datamem
    dm                      = DM(clk,rst_n,d2_byte_rd,d2_2byte_rd,d2_4byte_rd,d2_mem_rd,d2_signed_mem_rd,d_alu_out_data,w_mem_out_data,d2_byte_wr,
    d2_2byte_wr,d2_4byte_wr,d2_mem_wr,d2_rt_data)
    ##pipe4##
    mem_pipe1               = FLOP(clk,rst_n,w_mem_out_data,d_mem_out_data)
    mem_pipe2               = FLOP(clk,rst_n,d_alu_out_data,d2_alu_out_data)
    mem_pipe3               = FLOP(clk,rst_n,d2_rg_write,d3_rg_write)
    mem_pipe4               = FLOP(clk,rst_n,d2_mem_rd,d3_mem_rd)
    mem_pipe5               = FLOP(clk,rst_n,d2_rt,d3_rt)
    mem_pipe6               = FLOP(clk,rst_n,d2_rd,d3_rd)
    mem_pipe7               = FLOP(clk,rst_n,d_issue,issue)
    mem_pipe8               = FLOP(clk,rst_n,d2_rg_write_imm,d3_rg_write_imm)

    #writeback
    
    wb                      = WB(d3_rg_write,d3_rg_write_imm,d3_mem_rd,d3_rt,d3_rd,d2_alu_out_data,d_mem_out_data,w_wb_wr_addr,w_wb_wr_enable,w_wb_wr_data)
    
    return instances()
import sys
import getopt
import re
def extract():
    argv = sys.argv[1:]

    opt,args = getopt.getopt(argv,"",["input="])

    for i,j in opt:
        if i in ['--input']:
            input = j



    
    return str(input)

input = extract()

@block
def stb_convert():
    clk = Signal(intbv(0)[1:])
    issue = Signal(intbv(0)[1:])
    rst_n = ResetSignal(val=0,active=0,isasync=True)
    start = Signal(intbv(0)[1:])
    mips_inst = MIPS(clk,rst_n,issue,start,str(input)+"_binary.txt")
    
    #mips_inst.convert(hdl='Verilog',name='mips')
    @always(delay(5))
    def clk_gen():
        clk.next = not clk
    fh = open(str(input)+"_binary.txt")
    oh = open(str(input)+"_out.rpt",'w')
    instruction_lines = fh.readlines()
    ins_num = len(instruction_lines)
    r_file = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10: 0,
        11 : 0,
        12 : 0,
        13 : 0,
        14 : 0,
        15 : 0,
        16 : 0,
        17 : 0,
        18 : 0,
        19 : 0,
        20 : 0,
        21 : 0,
        22 : 0,
        23 : 0,
        24 : 0,
        25 : 0,
        26 : 0,
        27 : 0,
        28 : 0,
        29 : 0,
        30 : 0,
        31 : 0
    }
    mem_file = {}
    for i in range(1024):
        mem_file[i] = 0
    def alu(i):
        line = instruction_lines[i]
        line = line.strip()
        t_opcode = line[0:6]
        t_rs = line[6:11]
        t_rt = line[11:16]
        t_rd = line[16:21]
        t_shamt = line[21:26]
        t_func = line[26:32]
        t_imm = line[16:32]
        t_opcode = int(str(t_opcode),2)
        t_rs = int(str(t_rs),2)
        t_rt = int(str(t_rt),2)
        t_rd = int(str(t_rd),2)
        t_shamt = int(str(t_shamt),2)
        t_func = int(str(t_func),2)
        if (int(line[16])==1):
            temp = int("1000000000000000",2)
            temp1 = int(str(line[17:32]),2)
            t_imm    = -temp+temp1
            #oh.write("t_imm = "+str(t_imm)+"\n")   

        else:
            t_imm = int(str(t_imm),2)   
        if (t_opcode==0):
            if(t_func in [0,2,3]):
                t_op1_data = r_file[t_rt]
                t_op2_data = t_shamt
            elif(t_func in [4,6,7]):
                t_op1_data = r_file[t_rt]
                t_op2_data = r_file[t_rs]
            else:
                t_op1_data = r_file[t_rs]
                t_op2_data = r_file[t_rt]
        elif (t_opcode >= 8):
            if ((8<=t_opcode<=11)|(32<=t_opcode<=43)):
                t_op1_data = r_file[t_rs]
                if (int(line[16])==1):
                    temp_1 = "0111111111111111" + line[16:32]
                    temp_2 = "1000000000000000" + "0000000000000000"
                    temp_1_int = int(str(temp_1),2)
                    temp_2_int = int(str(temp_2),2)
                    t_op2_data = -temp_2_int + temp_1_int
                else:
                    t_op2_data = t_imm
                #oh.write(str(t_opcode)+"\n")
                #oh.write(str(line[16])+"\n")
                #oh.write(str(t_op2_data)+"\n")
            elif (12<=t_opcode<=14):
                t_op1_data = r_file[t_rs]
                temp_1 = "0000000000000000" + line[16:32]
                t_op2_data = int(str(temp_1),2)
            elif (t_opcode==15):
                t_op1_data = 0
                t_op2_data= t_imm
        else:
            t_op1_data=0
            t_op2_data=0
        if (((t_opcode==0)&(t_func in [32,33]))|(t_opcode in [8,9,32,33,34,36,37,40,41,43])):
            t_alu_out = t_op1_data+t_op2_data
        elif ((t_opcode==0)&(t_func in [34,35])):
            t_alu_out = t_op1_data-t_op2_data
        elif (((t_opcode==0)&(t_func ==36))|(t_opcode==12)):
            t_alu_out = t_op1_data&t_op2_data
        elif (((t_opcode==0)&(t_func ==37))|(t_opcode==13)):
            t_alu_out = t_op1_data | t_op2_data
        elif (((t_opcode==0)&(t_func ==38))|(t_opcode==14)):
            t_alu_out = t_op1_data ^ t_op2_data
        elif ((t_opcode==0)&(t_func ==39)):
            t_alu_out = ~(t_op1_data|t_op2_data)
        elif (((t_opcode==0)&(t_func in [42,43]))|(t_opcode in [10,11])):
            if (t_op1_data<t_op2_data):
                t_alu_out = 1
            else:
                t_alu_out = 0
        elif (t_opcode==15):
            if (int(line[16])==1):
                temp   = "0"+line[17:32]+"0000000000000000"
                temp_1 = "1000000000000000"+"0000000000000000"
                temp = int(temp,2)
                temp_1 = int(temp_1,2)
                t_alu_out = temp-temp_1
            else:
                t_alu_out = line[16:32]+"0000000000000000"
                t_alu_out = int(str(t_alu_out),2)
        elif ((t_opcode==0)&(t_func in [0,4])):
            t_alu_out = t_op1_data << t_op2_data
        elif ((t_opcode==0)&(t_func in [2,6])):
            t_alu_out = t_op1_data >> t_op2_data
        else:
            t_alu_out=0
        return t_alu_out,t_op1_data,t_op2_data,t_opcode,t_rt,t_rd
    def mem_access(t_alu_out,t_opcode,t_rt):
        if (t_opcode in [32,33,34,36,37]):
            temp = mem_file[t_alu_out]
        else:
            temp=0
        temp = f'{temp:032b}'
        if (t_opcode==32):
            temp_1 = temp[24:32]
            if (temp_1[0] == 1):
                temp_3 = "0111111111111111"+"11111111"+temp_1
                temp_4 = "1000000000000000"+"00000000"+"00000000"
                temp_2 = -int(str(temp_4),2)+int(str(temp_3),2)
            else:
                temp_2 = "0000000000000000"+temp_1
                temp_2 = int(str(temp_2),2)
            t_mem_out = temp_2
        elif (t_opcode==33):
            temp_1 = temp[16:32]
            if (temp_1[0] == 1):
                temp_3 = "0111111111111111"+temp_1
                temp_4 = "1000000000000000"+"00000000"+"00000000"
                temp_2 = -int(str(temp_4),2)+int(str(temp_3),2)
            else:
                temp_2 = "0000000000000000"+temp_1
                temp_2 = int(str(temp_2),2)
            t_mem_out = temp_2
        elif (t_opcode==34):
            temp_1 = temp
            temp_2 = temp_1
            t_mem_out = int(str(temp_2),2)
        elif (t_opcode==36):
            temp_1 = temp[24:32]
            temp_2 = "0000000000000000"+"00000000"+temp_1
            temp_2 = int(str(temp_2),2)
            t_mem_out = temp_2
        elif (t_opcode==37):
            temp_1 = temp[16:32]
            temp_2 = "0000000000000000"+"00000000"+temp_1
            temp_2 = int(str(temp_2),2)
            t_mem_out = temp_2
        else:
            t_mem_out=0

        return t_mem_out
    @instance
    def rst_gen():
        yield delay(10)
        rst_n.next = 0
        yield delay(5)
        rst_n.next = 1
    @instance
    def start_gen():
        yield clk.posedge
        yield clk.posedge
        start.next = 1
    
    @instance
    def if_debug():
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield delay(1)
        if (start==1):
            for i in range(ins_num):
                line = instruction_lines[i]
                line = line.strip()

                yield clk.negedge
                if ((pc == i)&((int(str(line),2) == w_instruction))):
                    print("Fetch is accurate for instruction %i" %(i))
                    oh.write("Fetch is accurate for instruction %i\n" %(i))
                    if_flag = 1
                else:
                    print("Fetch is not accurate for instruction %i" %(i))
                    oh.write("Fetch is not accurate for instruction %i\n" %(i))
                    if_flag = 0
    @instance
    def id_debug():
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield delay(1)
        for i in range(ins_num):
            line = instruction_lines[i]
            line = line.strip()
            t_opcode = line[0:6]
            t_rs = line[6:11]
            t_rt = line[11:16]
            t_rd = line[16:21]
            t_shamt = line[21:26]
            t_func = line[26:32]
            t_imm = line[16:32]
            if (line == 0):
                t_nop = 1
            else:
                t_nop=0
            t_opcode = int(str(t_opcode),2)
            t_rs = int(str(t_rs),2)
            t_rt = int(str(t_rt),2)
            t_rd = int(str(t_rd),2)
            t_shamt = int(str(t_shamt),2)
            t_func = int(str(t_func),2)
            if (int(line[16]) == 1):
                temp = int("1000000000000000",2)
                temp1 = int(str(line[17:32]),2)
                t_imm    = -temp+temp1
            else:
                t_imm = int(str(t_imm),2)   
            yield clk.negedge
            yield delay(1)
            if ((opcode==t_opcode) &
                (rs == t_rs) &
                (rt == t_rt) &
                (rd == t_rd) &
                (shamt == t_shamt) &
                (func == t_func) &
                (nop == t_nop)):
                if (t_opcode > 0):
                    if (t_imm==imm):
                        print("Decoder is accurate for instruction %i" %(i))
                        oh.write("Decoder is accurate for instruction %i\n" %(i))
                    else:
                        print("Decoder is not accurate for instruction %i"%(i))
                        print ("%i %i" %(opcode,t_opcode))
                        print ("%i %i" %(rs,t_rs))
                        print ("%i %i" %(rt,t_rt))
                        print ("%i %i" %(rd,t_rd))
                        print ("%i %i" %(shamt,t_shamt))
                        print ("%i %i" %(func,t_func))
                        print ("%i %i" %(imm,t_imm))
                        print ("%i %i" %(nop,t_nop))
                        oh.write("Decoder is not accurate for instruction %i\n"%(i))
                        oh.write ("%i %i\n" %(opcode,t_opcode))
                        oh.write ("%i %i\n" %(rs,t_rs))
                        oh.write ("%i %i\n" %(rt,t_rt))
                        oh.write ("%i %i\n" %(rd,t_rd))
                        oh.write ("%i %i\n" %(shamt,t_shamt))
                        oh.write ("%i %i\n" %(func,t_func))
                        oh.write ("%i %i\n" %(imm,t_imm))
                        oh.write ("%i %i\n" %(nop,t_nop))

                else:
                    print("Decoder is accurate for instruction %i" %(i))
                    oh.write("Decoder is accurate for instruction %i\n" %(i))

                id_flag = 1

            else:
                print("Decoder is not accurate for instruction %i"%(i))
                print ("%i %i" %(opcode,t_opcode))
                print ("%i %i" %(rs,t_rs))
                print ("%i %i" %(rt,t_rt))
                print ("%i %i" %(rd,t_rd))
                print ("%i %i" %(shamt,t_shamt))
                print ("%i %i" %(func,t_func))
                print ("%i %i" %(imm,t_imm))
                print ("%i %i" %(nop,t_nop))
                oh.write("Decoder is not accurate for instruction %i\n"%(i))
                oh.write ("%i %i\n" %(opcode,t_opcode))
                oh.write ("%i %i\n" %(rs,t_rs))
                oh.write ("%i %i\n" %(rt,t_rt))
                oh.write ("%i %i\n" %(rd,t_rd))
                oh.write ("%i %i\n" %(shamt,t_shamt))
                oh.write ("%i %i\n" %(func,t_func))
                oh.write ("%i %i\n" %(imm,t_imm))
                oh.write ("%i %i\n" %(nop,t_nop))
                id_flag = 0

    @instance
    def execution_debug():
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield delay(1)
        for i in range(ins_num):
            t_alu_out,t_op1_data,t_op2_data,t_opcode,t_rt,t_rd = alu(i)
            yield clk.negedge
            yield delay(2)
            if ((w_alu_out_data==t_alu_out)):
                print("Alu is accurate for instruction %i" %(i))
                oh.write("Alu is accurate for instruction %i\n" %(i))
                #oh.write ("%i %i\n" %(w_alu_out_data,t_alu_out))
                #oh.write ("%i %i\n" %(d_op1_data,t_op1_data))
                #oh.write ("%i %i\n" %(d_op2_data,t_op2_data))
                ex_flag = 1

            else:
                print("Alu is not accurate for instruction %i"%(i))
                print ("%i %i" %(w_alu_out_data,t_alu_out))
                print ("%i %i" %(d_op1_data,t_op1_data))
                print ("%i %i" %(d_op2_data,t_op2_data))
                oh.write("Alu is not accurate for instruction %i\n"%(i))
                oh.write ("%i %i\n" %(w_alu_out_data,t_alu_out))
                oh.write ("%i %i\n" %(d_op1_data,t_op1_data))
                oh.write ("%i %i\n" %(d_op2_data,t_op2_data))
                ex_flag = 0
    
    @instance
    def memory_read_write_debug():
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield delay(1)
        for i in range(ins_num):
            t_alu_out,t_op1_data,t_op2_data,t_opcode,t_rt,t_rd = alu(i)
            t_mem_out = mem_access(t_alu_out,t_opcode,t_rt)
            if (t_opcode==40):
                temp_3 = r_file[t_rt]
                temp_4 = f'{temp_3:032b}'
                temp_1 = temp_4[24:32]
                temp_2 = int(str(temp_1),2)
                mem_file[t_alu_out] = temp_2
            elif (t_opcode==41):
                temp_3 = r_file[t_rt]
                temp_4 = f'{temp_3:032b}'
                temp_1 = temp_4[16:32]
                temp_2 = int(str(temp_1),2)
                mem_file[t_alu_out] = temp_2
            elif (t_opcode==43):
                temp_3 = r_file[t_rt]
                temp_4 = f'{temp_3:032b}'
                temp_1 = temp_4
                temp_2 = int(str(temp_1),2)
                mem_file[t_alu_out] = temp_2

            yield clk.negedge
            delay(3)
            if(t_opcode in [32,33,34,36,37]):
                if(w_mem_out_data==t_mem_out):
                    print ("memory rd/wr is accurate for instruction %i"%(i))
                    oh.write ("memory rd/wr is accurate for instruction %i\n"%(i))
                    #print ("%i  %i"%(w_mem_out_data,t_mem_out))
                    #oh.write ("%i  %i\n"%(w_mem_out_data,t_mem_out))
                    mem_flag = 1

                else:
                    print ("memory rd/wr is not accurate for instruction %i"%(i))
                    print ("%i  %i"%(w_mem_out_data,t_mem_out))
                    oh.write ("memory rd/wr is not accurate for instruction %i\n"%(i))
                    oh.write ("%i  %i\n"%(w_mem_out_data,t_mem_out))
                    mem_flag = 0
            else:
                mem_flag = 1
    @instance
    def write_back_debug():
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield clk.posedge
        yield delay(1)
        for i in range(ins_num):
            t_alu_out,t_op1_data,t_op2_data,t_opcode,t_rt,t_rd = alu(i)
            t_mem_out = mem_access(t_alu_out,t_opcode,t_rt)
            if (t_opcode==0):
                addr = t_rd
                r_file[addr] = t_alu_out
                comp = t_alu_out
                comp_addr = addr
            elif((t_opcode>=8)&(t_opcode<=15)):
                addr = t_rt
                r_file[addr] = t_alu_out
                comp = t_alu_out
                comp_addr = addr
            elif((t_opcode in [32,33,34,36,37])):
                addr = t_rt
                r_file[addr] = t_mem_out
                comp = t_mem_out
                comp_addr = addr
            yield clk.negedge
            yield delay(4)
            if t_opcode in [0,8,9,10,11,12,13,14,15,32,33,34,36,37]:
                if ((comp==w_wb_wr_data)&(comp_addr==w_wb_wr_addr)):
                    print  ("WB is accurate for instruction %i" %(i))
                    oh.write  ("WB is accurate for instruction %i\n" %(i))
                    wb_flag = 1

                else:
                    print  ("WB is not accurate for %i"%(i))
                    print ("%i %i"%(comp,w_wb_wr_data))
                    print ("%i %i"%(comp_addr,w_wb_wr_addr))
                    oh.write  ("WB is not accurate for %i\n"%(i))
                    oh.write ("%i %i\n"%(comp,w_wb_wr_data))
                    oh.write ("%i %i\n"%(comp_addr,w_wb_wr_addr))
                    wb_flag = 0
            #        oh.write ("d3_rg_write %i ,d3_rg_write_imm %i ,d3_mem_rd %i ,d3_rt %i ,d3_rd %i ,d2_alu_out_data %i ,d_mem_out_data %i"%(d3_rg_write,d3_rg_write_imm,d3_mem_rd,d3_rt,d3_rd,d2_alu_out_data,d_mem_out_data))
            #for i in range(15):
            #    print ("r_file[%i] = %i, mem_file[%i] = %i" %(i,r_file[i],i,mem_file[i]))
            #    oh.write ("r_file[%i] = %i, mem_file[%i] = %i\n" %(i,r_file[i],i,mem_file[i]))
            else:
                wb_flag = 1

        oh.close()
            
    fh.close()
    return mips_inst,clk_gen,rst_gen,start_gen,if_debug,id_debug,execution_debug,memory_read_write_debug,write_back_debug



    
simInst = stb_convert()
simInst.config_sim(trace=True)
simInst.run_sim(2500)
