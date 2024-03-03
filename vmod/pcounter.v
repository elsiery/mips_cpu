/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////


module pcounter (
    i_clk,
    i_rst_n,
    i_start,
    o_pc
);


input [0:0] i_clk;
input i_rst_n;
input [0:0] i_start;
reg d_start;
output [8:0] o_pc;
reg [8:0] o_pc;

always @(posedge i_clk, negedge i_rst_n) begin
    if (i_rst_n == 0) begin
        o_pc <= 0;
    end
    else begin
        if (d_start == 1) begin
            o_pc <= o_pc + 1'b1;
        end
    end
end

always @(posedge i_clk,negedge i_rst_n) begin
    if(!i_rst_n) begin
        d_start <=0;
    end
    else begin
        if  (i_start==1) begin
            d_start <= 1'b1;
        end
    end
end


endmodule
