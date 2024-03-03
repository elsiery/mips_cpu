/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////





module if_fetch(
    address,
    instruction
);

input [8:0] address;
output [31:0] instruction;

reg [31:0] mem [0:44];

initial begin
	$readmemh("first_program_hexa.txt", mem);
end

assign instruction = mem[address];
endmodule
