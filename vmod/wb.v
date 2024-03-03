/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////





module wb (
    i_rg_wr,
    i_rg_wr_imm,
    i_mem_rd,
    i_rt,
    i_rd,
    i_alu_data,
    i_mem_rd_data,
    o_wb_addr,
    o_wb_cntrl,
    o_wb_data
);


input [0:0] i_rg_wr;
input [0:0] i_rg_wr_imm;
input [0:0] i_mem_rd;
input [4:0] i_rt;
input [4:0] i_rd;
input [31:0] i_alu_data;
input [31:0] i_mem_rd_data;
output [4:0] o_wb_addr;
reg [4:0] o_wb_addr;
output [0:0] o_wb_cntrl;
wire [0:0] o_wb_cntrl;
output [31:0] o_wb_data;
reg [31:0] o_wb_data;





assign o_wb_cntrl = ((i_rg_wr | i_mem_rd) | i_rg_wr_imm);


always @(i_rd, i_mem_rd, i_rg_wr_imm, i_rt, i_rg_wr) begin: WB_WB_ADDR
    o_wb_addr = 0;
    if ((i_rg_wr == 1)) begin
        o_wb_addr = i_rd;
    end
    else if (((i_mem_rd == 1) | (i_rg_wr_imm == 1))) begin
        o_wb_addr = i_rt;
    end
end


always @(i_mem_rd, i_rg_wr_imm, i_mem_rd_data, i_rg_wr, i_alu_data) begin: WB_WB_DATA
    o_wb_data = 0;
    if (((i_rg_wr == 1) | (i_rg_wr_imm == 1))) begin
        o_wb_data = i_alu_data;
    end
    else if ((i_mem_rd == 1)) begin
        o_wb_data = i_mem_rd_data;
    end
end

endmodule
