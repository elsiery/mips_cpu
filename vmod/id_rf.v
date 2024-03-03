/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////




module id_rf (
    i_clk,
    i_rst_n,
    i_reg1,
    i_reg2,
    i_wr_reg,
    i_data_in,
    i_wr_control,
    o_data1,
    o_data2
);


input [0:0] i_clk;
input i_rst_n;
input [4:0] i_reg1;
input [4:0] i_reg2;
input [4:0] i_wr_reg;
input [31:0] i_data_in;
input [0:0] i_wr_control;
output [31:0] o_data1;
wire [31:0] o_data1;
output [31:0] o_data2;
wire [31:0] o_data2;

reg [31:0] mem [0:32-1];



always @(posedge i_clk, negedge i_rst_n) begin
    if (i_rst_n == 0) begin
        mem[0] <= 0;
        mem[1] <= 0;
        mem[2] <= 0;
        mem[3] <= 0;
        mem[4] <= 0;
        mem[5] <= 0;
        mem[6] <= 0;
        mem[7] <= 0;
        mem[8] <= 0;
        mem[9] <= 0;
        mem[10] <= 0;
        mem[11] <= 0;
        mem[12] <= 0;
        mem[13] <= 0;
        mem[14] <= 0;
        mem[15] <= 0;
        mem[16] <= 0;
        mem[17] <= 0;
        mem[18] <= 0;
        mem[19] <= 0;
        mem[20] <= 0;
        mem[21] <= 0;
        mem[22] <= 0;
        mem[23] <= 0;
        mem[24] <= 0;
        mem[25] <= 0;
        mem[26] <= 0;
        mem[27] <= 0;
        mem[28] <= 0;
        mem[29] <= 0;
        mem[30] <= 0;
        mem[31] <= 0;
    end
    else begin
        if ((i_wr_control == 1)) begin
            mem[i_wr_reg] <= i_data_in;
        end
    end
end



assign o_data1 = mem[i_reg1];



assign o_data2 = mem[i_reg2];

endmodule
