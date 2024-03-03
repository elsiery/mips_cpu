/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////








module id_cr (
    i_opcode,
    i_funct,
    i_nop,
    o_swap_rs_sh,
    o_swap_rs_rt,
    o_swap_rt_imm,
    o_signed_ext,
    o_mem_rd,
    o_rg_write,
    o_byte_rd,
    o_signed_mem_rd,
    o_2byte_rd,
    o_4byte_rd,
    o_mem_wr,
    o_byte_wr,
    o_2byte_wr,
    o_4byte_wr,
    o_opcode,
    o_funct,
    o_rg_write_imm
);


input [5:0] i_opcode;
input [5:0] i_funct;
input [0:0] i_nop;
output [0:0] o_swap_rs_sh;
reg [0:0] o_swap_rs_sh;
output [0:0] o_swap_rs_rt;
reg [0:0] o_swap_rs_rt;
output [0:0] o_swap_rt_imm;
reg [0:0] o_swap_rt_imm;
output [0:0] o_signed_ext;
reg [0:0] o_signed_ext;
output [0:0] o_mem_rd;
reg [0:0] o_mem_rd;
output [0:0] o_rg_write;
reg [0:0] o_rg_write;
output [0:0] o_byte_rd;
reg [0:0] o_byte_rd;
output [0:0] o_signed_mem_rd;
reg [0:0] o_signed_mem_rd;
output [0:0] o_2byte_rd;
reg [0:0] o_2byte_rd;
output [0:0] o_4byte_rd;
reg [0:0] o_4byte_rd;
output [0:0] o_mem_wr;
reg [0:0] o_mem_wr;
output [0:0] o_byte_wr;
reg [0:0] o_byte_wr;
output [0:0] o_2byte_wr;
reg [0:0] o_2byte_wr;
output [0:0] o_4byte_wr;
reg [0:0] o_4byte_wr;
output [5:0] o_opcode;
wire [5:0] o_opcode;
output [5:0] o_funct;
wire [5:0] o_funct;
output [0:0] o_rg_write_imm;
reg [0:0] o_rg_write_imm;




always @(i_nop, i_opcode, i_funct) begin: ID_CR_LOGIC
    o_swap_rs_sh = 0;
    o_swap_rs_rt = 0;
    o_swap_rt_imm = 0;
    o_signed_ext = 0;
    o_mem_rd = 0;
    o_rg_write = 0;
    o_byte_rd = 0;
    o_signed_mem_rd = 0;
    o_2byte_rd = 0;
    o_4byte_rd = 0;
    o_mem_wr = 0;
    o_byte_wr = 0;
    o_2byte_wr = 0;
    o_4byte_wr = 0;
    o_rg_write_imm = 0;
    if ((i_nop == 1)) begin
        o_swap_rs_sh = 0;
        o_swap_rs_rt = 0;
        o_swap_rt_imm = 0;
        o_signed_ext = 0;
        o_mem_rd = 0;
        o_rg_write = 0;
        o_byte_rd = 0;
        o_signed_mem_rd = 0;
        o_2byte_rd = 0;
        o_4byte_rd = 0;
        o_mem_wr = 0;
        o_byte_wr = 0;
        o_2byte_wr = 0;
        o_4byte_wr = 0;
        o_rg_write_imm = 0;
    end
    else if ((i_opcode == 0)) begin
        o_rg_write = 1;
        if ((((i_funct == 0) | (i_funct == 2)) | (i_funct == 3))) begin
            o_swap_rs_sh = 1;
            o_swap_rs_rt = 1;
        end
        else if ((((i_funct == 4) | (i_funct == 6)) | (i_funct == 7))) begin
            o_swap_rs_sh = 0;
            o_swap_rs_rt = 1;
        end
    end
    else if (((i_opcode >= 8) & (i_opcode <= 15))) begin
        o_swap_rt_imm = 1;
        o_rg_write_imm = 1;
        if ((((i_opcode == 12) | (i_opcode == 13)) | (i_opcode == 14))) begin
            o_signed_ext = 0;
        end
        else begin
            o_signed_ext = 1;
        end
    end
    else if ((((i_opcode >= 32) & (i_opcode <= 37)) & (i_opcode != 35))) begin
        o_swap_rt_imm = 1;
        o_signed_ext = 1;
        o_mem_rd = 1;
        case (i_opcode)
            'h20: begin
                o_byte_rd = 1;
                o_signed_mem_rd = 1;
            end
            'h21: begin
                o_2byte_rd = 1;
                o_signed_mem_rd = 1;
            end
            'h22: begin
                o_4byte_rd = 1;
                o_signed_mem_rd = 1;
            end
            'h24: begin
                o_byte_rd = 1;
                o_signed_mem_rd = 0;
            end
            'h25: begin
                o_2byte_rd = 1;
                o_signed_mem_rd = 0;
            end
        endcase
    end
    else if ((((i_opcode == 40) | (i_opcode == 41)) | (i_opcode == 43))) begin
        o_swap_rt_imm = 1;
        o_signed_ext = 1;
        o_mem_wr = 1;
        case (i_opcode)
            'h28: begin
                o_byte_wr = 1;
            end
            'h29: begin
                o_2byte_wr = 1;
            end
            'h2b: begin
                o_4byte_wr = 1;
            end
        endcase
    end
end



assign o_opcode = i_opcode;
assign o_funct = i_funct;

endmodule
