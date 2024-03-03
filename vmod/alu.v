/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////







module alu (
    i_op_1,
    i_op_2,
    i_alu_op,
    o_exception,
    o_result
);


input [31:0] i_op_1;
input [31:0] i_op_2;
input [3:0] i_alu_op;
output [0:0] o_exception;
reg [0:0] o_exception;
output signed [31:0] o_result;
wire signed [31:0] o_result;

reg signed [31:0] w_result;



always @(i_op_2, i_op_1, i_alu_op) begin
    case (i_alu_op)
        'h0: begin
            if ((i_op_2 > 0)) begin
                w_result = (i_op_1 << i_op_2);
            end
        end
        'h1: begin
            if ((i_op_2 > 0)) begin
                w_result = (i_op_1 >>> i_op_2);
            end
        end
        'h2: begin
            if ((i_op_2 > 0)) begin
                w_result = $signed($signed(i_op_1) >>> i_op_2);
            end
        end
        'h3: begin
            w_result = ($signed(i_op_1) + $signed(i_op_2));
        end
        'h4: begin
            w_result = (i_op_1 + i_op_2);
        end
        'h5: begin
            w_result = ($signed(i_op_1) - $signed(i_op_2));
        end
        'h6: begin
            w_result = (i_op_1 - i_op_2);
        end
        'h7: begin
            w_result = (i_op_1 & i_op_2);
        end
        'h8: begin
            w_result = (i_op_1 | i_op_2);
        end
        'h9: begin
            w_result = (i_op_1 ^ i_op_2);
        end
        'ha: begin
            w_result = (~(i_op_1 | i_op_2));
        end
        'hb: begin
            if (($signed(i_op_1) < $signed(i_op_2))) begin
                w_result = 1;
            end
            else begin
                w_result = 0;
            end
        end
        'hc: begin
            if ((i_op_1 < i_op_2)) begin
                w_result = 1;
            end
            else begin
                w_result = 0;
            end
        end
        'hd: begin
            w_result = (i_op_2 << 16);
        end
        default: begin
            w_result = 0;
        end
    endcase
end
always@(*) begin
    o_exception = 1'b0;
    if(i_alu_op == 'h3) begin
        o_exception = ($signed(i_op_1) + $signed(i_op_2) > 2147483647)||($signed(i_op_1) + $signed(i_op_2) < -2147483648);
    end else if(i_alu_op=='h5) begin
        o_exception = ($signed(i_op_1) - $signed(i_op_2) > 2147483647)||($signed(i_op_1) - $signed(i_op_2) < -2147483648);
    end
end

assign o_result = w_result;

endmodule
