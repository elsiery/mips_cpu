"""


Author: Elsie Rezinold Yedida






"""





import sys
import getopt
import re
Registers = {
'$r0' :   0,
'$r1' :   1,
'$r2' :   2,
'$r3' :   3,
'$r4' :   4,	
'$r5' :   5,	
'$r6' :   6,	
'$r7' :   7,	
'$r8' :   8,	
'$r9' :   9,	
'$r10':	 10,
'$r11':  11,       
'$r12':  12,       
'$r13':  13,       
'$r14':	 14,
'$r15':	 15,
'$r16':	 16,
'$r17':	 17,
'$r18':	 18,
'$r19':	 19,
'$r20':  20,       
'$r21':  21,       
'$r22':  22,       
'$r23':  23,       
'$r24':	 24,
'$r25':	 25,
'$r26':	 26,
'$r27':	 27,
'$r28':	 28,
'$r29':	 29,
'$r30':  30,       
'$r31':  31
}

r_format = {
'sll'  : 0,
'srl'  : 2,
'sra'  : 3,
'sllv' : 4,
'srlv' : 6,
'srav' : 7,
'add'  : 32,
'addu' : 33,
'sub'  : 34,
'subu' : 35,
'and'  : 36,
'or'   : 37,
'xor'  : 38,
'nor'  : 39,
'slt'  : 42,
'sltu' : 43
}

i_format = {
'beq'  : 4,
'bne'  : 5,
'blez' : 6,
'bgtz' : 7,
'addi' : 8,
'addiu': 9,
'slti' : 10,
'sltiu': 11,
'andi' : 12,
'ori'  : 13,
'xori' : 14,
'lui'  : 15,
'lb'   : 32,
'lh'   : 33,
'lw'   : 34,
'lbu'  : 36,
'lhu'  : 37,
'sb'   : 40,
'sh'   : 41,
'sw'   : 43
}



def extract():
    argv = sys.argv[1:]

    opt,args = getopt.getopt(argv,"",["asm="])

    for i,j in opt:
        if i in ['--asm']:
            asm = j



    
    return str(asm)

asm = extract()


in_loc = str(asm)

out_loc = str(asm)+"_hexa.txt"

oh = open(out_loc,'w')
with open(in_loc,'r') as ih:
    for line in ih:
        line = line.strip()
        list_in = re.split(',| ',line)
        print(list_in)
        print(list_in[0])
        #r_type
        if list_in[0] in r_format.keys():
            print('r')
            opcode = f'{0:06b}'
            v = r_format[list_in[0]]
            func = f'{v:06b}'
            v1 = Registers[list_in[1]]
            rd = f'{v1:05b}'
            if list_in[0] in ['sll','srl','sra','sllv','srlv','srav']:
                v2 = Registers[list_in[2]]
                rt = f'{v2:05b}'
                if list_in[0] in ['sll','srl','sra']:
                    v3 = list_in[3]
                    shamt = f'{v1:05b}'
                    rs = f'{0:05b}'
                else:
                    v3 = Registers[list_in[3]]
                    shamt = f'{0:05b}'
                    rs = f'{v3:05b}'
            else:
                v2 = Registers[list_in[2]]
                rs = f'{v2:05b}'
                v3 = Registers[list_in[3]]
                rt = f'{v3:05b}'
                shamt = f'{0:05b}'
            print(opcode)
            print(rs)
            print(rt)
            print(rd)
            print(shamt)
            print(func)
            it = opcode+rs+rt+rd+shamt+func
            it = int(str(it),2)
            it = hex(it)
            it = it.strip('0x')
            oh.write(str(it)+"\n")
            
        elif list_in[0] in i_format.keys():
            v = i_format[list_in[0]]
            
            opcode = f'{v:06b}'
            v1 = Registers[list_in[1]]
            rt = f'{v1:05b}'
            if list_in[0] in ['lb','lh','lw','lhu','lbu','sb','sh','sw']:
                new_ls = list_in[2].strip(')')
                new_ls = new_ls.split('(')
                imm_hex = new_ls[0]
                imm_int = int(imm_hex,16)
                imm = f'{imm_int:016b}'
                rs_v = Registers[new_ls[1]]
                rs = f'{rs_v:05b}'
            elif (list_in[0] == 'lui'):
                imm_hex = list_in[2]
                imm_int = int(imm_hex,16)
                imm = f'{imm_int:016b}'
                rs = f'{0:05b}'
            else:
                imm_hex = list_in[3]
                imm_int = int(imm_hex,16)
                imm = f'{imm_int:016b}'

                rs_v = Registers[list_in[2]]
                rs = f'{rs_v:05b}'
            print(opcode)
            print(rs)
            print(rt)
            print(imm)
            it = opcode+rs+rt+imm
            it = int(str(it),2)
            it = hex(it)
            it = it.strip('0x')
            oh.write(str(it)+"\n")

    oh.close()
    ih.close()
                

















