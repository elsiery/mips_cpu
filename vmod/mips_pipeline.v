/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////







`include "pcounter.v"
`include "if_fetch.v"
`include "id.v"
`include "id_rf.v"
`include "id_cr.v"
`include "alu_cr.v"
`include "alu.v"
`include "dm.v"
`include "wb.v"


module mips_pipeline (
    clk,
    rst_n,
    start,
    issue
);

input  clk;
input rst_n;
output  issue;
reg  issue;
input  start;

wire [8:0] pc;
wire [31:0] w_instruction;
reg  [31:0] d_instruction;
wire [5:0] opcode;
wire [4:0] rs;
wire [4:0] rt;
wire [4:0] w_wb_wr_addr;
wire [4:0] rd;
reg [4:0] d_rt;
reg [4:0] d_rd;
reg [4:0] d2_rt;
reg [4:0] d2_rd;
reg [4:0] d3_rt;
reg [4:0] d3_rd;
wire [4:0] shamt;
wire [5:0] func;
wire  [15:0] imm;
wire  [31:0] imm_32;
wire  nop;
wire [5:0] w_opcode;
wire [5:0] w_funct;
reg [5:0] d_opcode;
reg [5:0] d_funct;
wire [3:0] w_alu_op;
wire [31:0] w_rs_data;
wire [31:0] w_rt_data;
reg [31:0] d_rt_data;
reg [31:0] d2_rt_data;
wire [31:0] w_wb_wr_data;
wire [31:0] w_mem_out_data;
reg [31:0] d_mem_out_data;
wire  w_wb_wr_enable;
wire [31:0] w_rs_or_shamt_data;
wire [31:0] w_op1_data;
wire [31:0] w_op2_data;
reg [31:0] d_op1_data;
reg [31:0] d_op2_data;
wire [31:0] w_alu_out_data;
reg [31:0] d_alu_out_data;
reg [31:0] d2_alu_out_data;
wire  w_exception;
wire [31:0] w_rt_or_imm_data;
reg  d_issue;
wire  w_swap_rs_sh;
wire  w_swap_rs_rt;
wire  w_swap_rt_imm;
wire  w_signed_ext;
wire  w_mem_rd;
wire  w_rg_write;
wire  w_byte_rd;
wire  w_signed_mem_rd;
wire  w_2byte_rd;
wire  w_4byte_rd;
wire  w_mem_wr;
wire  w_byte_wr;
wire  w_2byte_wr;
wire  w_4byte_wr;
reg  d_mem_rd;
reg  d_rg_write;
reg  d_byte_rd;
reg  d_signed_mem_rd;
reg  d_2byte_rd;
reg  d_4byte_rd;
reg  d_mem_wr;
reg  d_byte_wr;
reg  d_2byte_wr;
reg  d_4byte_wr;
reg  d2_mem_rd;
reg  d2_rg_write;
reg  d2_byte_rd;
reg  d2_signed_mem_rd;
reg  d2_2byte_rd;
reg  d2_4byte_rd;
reg  d2_mem_wr;
reg  d2_byte_wr;
reg  d2_2byte_wr;
reg  d2_4byte_wr;
reg  d3_rg_write;
wire  w_rg_write_imm;
reg  d_rg_write_imm;
reg  d2_rg_write_imm;
reg  d3_rg_write_imm;
reg  d3_mem_rd;




//program_counter         
pcounter  u_pc(
    clk,
  rst_n,
  start,
  pc
);
//instruction_memory     
if_fetch u_if(
    pc,
    w_instruction
);
//pipe1
always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_instruction <= 0;
    end
    else begin
        d_instruction <= w_instruction;
    end
end


//Decode and control stage 
//decode                  
id u_id(
    d_instruction,
    opcode,
    rs,
    rt,
    rd,
    shamt,
    func,
    imm,
    nop
);
//rf                      
id_rf u_rf(
    clk,
    rst_n,
    rs,
    rt,
    w_wb_wr_addr,
    w_wb_wr_data,
    w_wb_wr_enable,
    w_rs_data,
    w_rt_data
);
//decode_control      
id_cr u_cr(
    opcode,
    func,
    nop,
    w_swap_rs_sh,
    w_swap_rs_rt,
    w_swap_rt_imm,
    w_signed_ext,
    w_mem_rd,
    w_rg_write,
    w_byte_rd,
    w_signed_mem_rd,
    w_2byte_rd,
    w_4byte_rd,
    w_mem_wr,
    w_byte_wr,
    w_2byte_wr,
    w_4byte_wr,
    w_opcode,
    w_funct,
    w_rg_write_imm
);

assign w_rs_or_shamt_data = w_swap_rs_sh ? shamt : w_rs_data;
assign imm_32           = w_signed_ext ? {{16{imm[15]}},imm} : {16'h0,imm};
assign w_rt_or_imm_data = w_swap_rt_imm ? imm_32 : w_rt_data;
assign w_op1_data       = w_swap_rs_rt ? w_rt_or_imm_data :   w_rs_or_shamt_data;
assign w_op2_data       = w_swap_rs_rt ? w_rs_or_shamt_data : w_rt_or_imm_data;
//pipe2
always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_opcode <= 0;
    end
    else begin
        d_opcode <= w_opcode;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_funct <= 0;
    end
    else begin
        d_funct <= w_funct;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_op1_data <= 0;
    end
    else begin
        d_op1_data <= w_op1_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_op2_data <= 0;
    end
    else begin
        d_op2_data <= w_op2_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_byte_rd <= 0;
    end
    else begin
        d_byte_rd <= w_byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_2byte_rd <= 0;
    end
    else begin
        d_2byte_rd <= w_2byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_4byte_rd <= 0;
    end
    else begin
        d_4byte_rd <= w_4byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_byte_wr <= 0;
    end
    else begin
        d_byte_wr <= w_byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_2byte_wr <= 0;
    end
    else begin
        d_2byte_wr <= w_2byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_4byte_wr <= 0;
    end
    else begin
        d_4byte_wr <= w_4byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_mem_rd <= 0;
    end
    else begin
        d_mem_rd <= w_mem_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_signed_mem_rd <= 0;
    end
    else begin
        d_signed_mem_rd <= w_signed_mem_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_mem_wr <= 0;
    end
    else begin
        d_mem_wr <= w_mem_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_rt_data <= 0;
    end
    else begin
        d_rt_data <= w_rt_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_rg_write <= 0;
    end
    else begin
        d_rg_write <= w_rg_write;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_rt <= 0;
    end
    else begin
        d_rt <= rt;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_rd <= 0;
    end
    else begin
        d_rd <= rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_rg_write_imm <= 0;
    end
    else begin
        d_rg_write_imm <= w_rg_write_imm;
    end
end


//Alu stage
alu_cr  u_alu_cr (
    d_opcode,
    d_funct,
    w_alu_op
);

alu u_alu(
    d_op1_data, 
    d_op2_data, 
    w_alu_op,
    w_exception, 
    w_alu_out_data
);

//pipe3
always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_alu_out_data <= 0;
    end
    else begin
        d_alu_out_data <= w_alu_out_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_byte_rd <= 0;
    end
    else begin
        d2_byte_rd <= d_byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_2byte_rd <= 0;
    end
    else begin
        d2_2byte_rd <= d_2byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_4byte_rd <= 0;
    end
    else begin
        d2_4byte_rd <= d_4byte_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_byte_wr <= 0;
    end
    else begin
        d2_byte_wr <= d_byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_2byte_wr <= 0;
    end
    else begin
        d2_2byte_wr <= d_2byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_4byte_wr <= 0;
    end
    else begin
        d2_4byte_wr <= d_4byte_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_mem_rd <= 0;
    end
    else begin
        d2_mem_rd <= d_mem_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_signed_mem_rd <= 0;
    end
    else begin
        d2_signed_mem_rd <= d_signed_mem_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_mem_wr <= 0;
    end
    else begin
        d2_mem_wr <= d_mem_wr;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_rt_data <= 0;
    end
    else begin
        d2_rt_data <= d_rt_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_rg_write <= 0;
    end
    else begin
        d2_rg_write <= d_rg_write;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_rt <= 0;
    end
    else begin
        d2_rt <= d_rt;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_rd <= 0;
    end
    else begin
        d2_rd <= d_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_issue <= 0;
    end
    else begin
        d_issue <= w_exception;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_rg_write_imm <= 0;
    end
    else begin
        d2_rg_write_imm <= d_rg_write_imm;
    end
end

//datamem
dm  u_dm(
    clk,
    rst_n,
    d2_byte_rd,
    d2_2byte_rd,
    d2_4byte_rd,
    d2_mem_rd,
    d2_signed_mem_rd,
    d_alu_out_data,
    w_mem_out_data,
    d2_byte_wr,
    d2_2byte_wr,
    d2_4byte_wr,
    d2_mem_wr,
    d2_rt_data
);
//pipe4
always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d_mem_out_data <= 0;
    end
    else begin
        d_mem_out_data <= w_mem_out_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d2_alu_out_data <= 0;
    end
    else begin
        d2_alu_out_data <= d_alu_out_data;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d3_rg_write <= 0;
    end
    else begin
        d3_rg_write <= d2_rg_write;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d3_mem_rd <= 0;
    end
    else begin
        d3_mem_rd <= d2_mem_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d3_rt <= 0;
    end
    else begin
        d3_rt <= d2_rt;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d3_rd <= 0;
    end
    else begin
        d3_rd <= d2_rd;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        issue <= 0;
    end
    else begin
        issue <= d_issue;
    end
end


always @(posedge clk, negedge rst_n) begin
    if (rst_n == 0) begin
        d3_rg_write_imm <= 0;
    end
    else begin
        d3_rg_write_imm <= d2_rg_write_imm;
    end
end

//writeback

wb  u_wb(
    d3_rg_write,
    d3_rg_write_imm,
    d3_mem_rd,
    d3_rt,
    d3_rd,
    d2_alu_out_data,
    d_mem_out_data,
    w_wb_wr_addr,
    w_wb_wr_enable,
    w_wb_wr_data
);
endmodule
