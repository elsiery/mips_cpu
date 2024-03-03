# mips_cpu

* A five staged, pipelined mips cpu has been implemented in both python and verilog.
* In python "Myhdl" library has been used to implement the cpu.
* Even though "myhdl" is a hardware descriptive language similar to verilog. It also comes with advantages of the python language.
* Even though I'm a hardware engineer whose primary working language is Verilog HDL, I've found it comfortable to visualize the hardware first in python.
* This is my first time writing hdl in python, and I've noticed that writing TB's gets easier in python.
* First I've implemented mips cpu in python's myhdl and also tested it in python.
* Then next I've designed it in Verilog HDL and also tested it in verilog.
* Though there is a provision in myhdl to convert python to verilog, i was not satisfied with the generated verilog. so i coded the whole thing in verilog seperately.
* Functionality of models both in python and verilog is same.
* This cpu supports R-type and I-type instructions only.
* All instructions are 32-bit, there are 32, 32-bit registers in the register file.
* Data memory is of 32-bit with 1024 depth.
* Below is the R-format instruction outline.

|   Opcode  |   rs   |  rt   |  rd   |  shamt   |   func    |
|-----------|--------|-------|-------|----------|-----------|
|   6 bits  | 5 bits | 5 bits| 5 bits|   5 bits |   6 bits  |
| 31 -   26 | 25 - 21| 20 -16| 15 -11| 10 - 6   | 5 - 0     |  

* In R-type instructions the following instructions are supported.
* Opcode is 0 for all R-type instructions.
* this type of instruction is decoded by "func" field.

|   instrunction    |   func    |   example          |    impl                |   comments    |
|-------------------|-----------|--------------------|------------------------|---------------|
|   sll             |   0       |sll $rd,  $rt, shamt| R[$rd] <- R[$rt]<<shamt| left shift    |
|   srl             |   2       |srl $rd,  $rt, shamt| R[$rd] <- R[$rt]>>shamt| rt logical sft|
|   sra             |   3       |sra $rd,  $rt, shamt| R[$rd] <- R[$rt]>>shamt| rt arthi sft  |
|   sllv            |   4       |sllv $rd,  $rt, $rs | R[$rd] <-R[$rt]<<R[$rs]| left shift    |
|   srlv            |   6       |srlv $rd,  $rt, $rs | R[$rd] <-R[$rt]>>R[$rs]| rt logical sft|
|   srav            |   7       |srav $rd,  $rt, $rs | R[$rd] <-R[$rt]>>R[$rs]| rt arthi sft  |
|   add             |   32      |add  $rd, $rs, $rt  | R[$rd]<-R[$rs]+R[$rt]  | signed,exception on ovf|
|   addu            |   33      |addu $rd, $rs, $rt  | R[$rd]<-R[$rs]+R[$rt]  | unsigned      |
|   sub             |   34      |sub  $rd, $rs, $rt  | R[$rd]<-R[$rs]-R[$rt]  | signed,exception on ovf|
|   subu            |   35      |subu $rd, $rs, $rt  | R[$rd]<-R[$rs]-R[$rt]  | unsigned      |
|   and             |   36      |and  $rd, $rs, $rt  | R[$rd]<-R[$rs]&R[$rt]  |               |
|   or              |   37      |or   $rd, $rs, $rt  | R[$rd]<-R[$rs]\|R[$rt] |               |
|   xor             |   38      |xor  $rd, $rs, $rt  | R[$rd]<-R[$rs]^R[$rt]  |               |
|   nor             |   39      |nor  $rd, $rs, $rt  |R[$rd]<-~(R[$rs]\|R[$rt])|               |
|   slt             |   42      |slt  $rd, $rs, $rt  | R[$rd]<-R[$rs]<R[$rt]  |signed         |
|   sltu            |   43      |sltu $rd, $rs, $rt  | R[$rd]<-R[$rs]<R[$rt]  |unsigned       |


* Below is the I-format instruction outline.

|   Opcode  |   rs   |  rt   |  imm   |
|-----------|--------|-------|--------|
|   6 bits  | 5 bits | 5 bits| 16 bits|
| 31 -   26 | 25 - 21| 20 -16| 15 - 0 |  

* In R-type instructions the following instructions are supported.
* Opcode is > 0 for all I-type instructions.
* this type of instruction is decoded by "opcode" field.

|   instrunction    |   opcode  |   example        |    impl                                |   comments    |
|-------------------|-----------|------------------|----------------------------------------|---------------|
|   addi            |   8       |addi  $rt, $rs,imm| R[$rt] <-R[$rs]+SE(imm)                | signed,exception on ovf|
|   addiu           |   9       |addiu $rt, $rs,imm| R[$rt] <-R[$rs]+SE(imm)                | unsigned      |
|   slti            |  10       |slti  $rt, $rs,imm| R[$rt] <-R[$rs]<SE(imm)                | signed        |
|   sltiu           |  11       |sltiu $rt, $rs,imm| R[$rt] <-R[$rs]<SE(imm)                | unsigned      |
|   andi            |  12       |andi  $rt, $rs,imm| R[$rt] <-R[$rs]&ZP(imm)                |               |
|   ori             |  13       |ori   $rt, $rs,imm| R[$rt] <-R[$rs]\|ZP(imm)               |               |
|   xori            |  14       |xori  $rt, $rs,imm| R[$rt] <-R[$rs]^ZP(imm)                |               |
|   lui             |  15       |lui   $rt, imm    | R[$rt]<-{imm,16'd0}                    |               |
|   lb              |  32       |lb    $rt,imm($rs)| R[$rt]<-SE(M(R[$rs]+SE(imm))[7:0])     |               | 
|   lh              |  33       |lh    $rt,imm($rs)| R[$rt]<-SE(M(R[$rs]+SE(imm))[15:0])    |               |
|   lw              |  34       |lw    $rt,imm($rs)| R[$rt]<-M(R[$rs]+SE(imm))              |               |  
|   lbu             |  36       |lbu   $rt,imm($rs)| R[$rt]<-{24'd0,M(R[$rs]+SE(imm))[7:0]} |               |    
|   lhu             |  37       |lhu   $rt,imm($rs)| R[$rt]<-{16'd0,M(R[$rs]+SE(imm))[15:0]}|               |    
|   sb              |  40       |sb    $rt,imm($rs)| M(R[$rs]+SE(imm))[7:0] <- R[$rt][7:0]  |               |
|   sh              |  41       |sh    $rt,imm($rs)| M(R[$rs]+SE(imm))[15:0]<- R[$rt][15:0] |               |
|   sw              |  43       |sw    $rt,imm($rs)| M(R[$rs]+SE(imm))[15:0]<- R[$rt][15:0] |               |

* SE means "sign extention"
* ZP means "zero padding"
* R[\*] means data from reg file
* M[\*] means data memory
* The locations of pipes are as follows 
    1. between fetch and decode stages.
    2. between decode and alu stages.
    3. between alu and mem_rd_wr stages.
    4. between mem_rd_wr and wb stages.

* "pmod" directory contains python files.
* "vmod" directory contains verilog files.
* "tests" directory contains test programs used to test python model and verilog model.
## NOTE
* Data hazards and control hazards are not taken care in this release.
### TODO
- [ ] Hazard detection implementation
- [ ] Data forwarding implementation
- [ ] Branch instructions support
- [ ] j-type instruction support



