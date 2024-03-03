/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////






module alu_cr (
    i_op_code,
    i_funct_field,
    o_alu_op
);


input [5:0] i_op_code;
input [5:0] i_funct_field;
output [3:0] o_alu_op;
reg [3:0] o_alu_op;




always @(i_op_code, i_funct_field) begin: ALU_CR_LOGIC
    if ((((i_funct_field == 0) | (i_funct_field == 4)) & (i_op_code == 0))) begin
        o_alu_op = 0;
    end
    else if ((((i_funct_field == 2) | (i_funct_field == 6)) & (i_op_code == 0))) begin
        o_alu_op = 1;
    end
    else if ((((i_funct_field == 3) | (i_funct_field == 7)) & (i_op_code == 0))) begin
        o_alu_op = 2;
    end
    else if ((((i_funct_field == 32) & (i_op_code == 0)) | (i_op_code == 8))) begin
        o_alu_op = 3;
    end
    else if ((((((((i_funct_field == 33) & (i_op_code == 0)) | (i_op_code == 9)) | ((i_op_code >= 32) & (i_op_code <= 37))) | (i_op_code == 40)) | (i_op_code == 41)) | (i_op_code == 43))) begin
        o_alu_op = 4;
    end
    else if (((i_funct_field == 34) & (i_op_code == 0))) begin
        o_alu_op = 5;
    end
    else if (((i_funct_field == 35) & (i_op_code == 0))) begin
        o_alu_op = 6;
    end
    else if ((((i_funct_field == 36) & (i_op_code == 0)) | (i_op_code == 12))) begin
        o_alu_op = 7;
    end
    else if ((((i_funct_field == 37) & (i_op_code == 0)) | (i_op_code == 13))) begin
        o_alu_op = 8;
    end
    else if ((((i_funct_field == 38) & (i_op_code == 0)) | (i_op_code == 14))) begin
        o_alu_op = 9;
    end
    else if (((i_funct_field == 39) & (i_op_code == 0))) begin
        o_alu_op = 10;
    end
    else if ((((i_funct_field == 42) & (i_op_code == 0)) | (i_op_code == 10))) begin
        o_alu_op = 11;
    end
    else if ((((i_funct_field == 43) & (i_op_code == 0)) | (i_op_code == 11))) begin
        o_alu_op = 12;
    end
    else if ((i_op_code == 15)) begin
        o_alu_op = 13;
    end
    else begin
        o_alu_op = 14;
    end
end

endmodule
