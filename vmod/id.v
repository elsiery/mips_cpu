/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////









module id (
    i_instruction,
    o_opcode,
    o_rs,
    o_rt,
    o_rd,
    o_shamt,
    o_func,
    o_imm,
    o_nop
);


input [31:0] i_instruction;
output [5:0] o_opcode;

output [4:0] o_rs;

output [4:0] o_rt;

output [4:0] o_rd;

output [4:0] o_shamt;

output [5:0] o_func;

output [15:0] o_imm;

output [0:0] o_nop;






assign    o_opcode = i_instruction[32-1:26];
assign    o_rs = i_instruction[26-1:21];
assign    o_rt = i_instruction[21-1:16];
assign    o_rd = i_instruction[16-1:11];
assign    o_shamt = i_instruction[11-1:6];
assign    o_func = i_instruction[6-1:0];
assign    o_imm = i_instruction[16-1:0];
assign    o_nop = (i_instruction==0) ? 1'b1 : 1'b0;


endmodule
