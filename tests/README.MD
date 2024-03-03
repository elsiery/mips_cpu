## Tests

* This folder contains the test programs i've used for testing both my models.
* There are six programs as seen.
* python model expects instructions in binary format.
* first write your program in a file similar to the programs given.
* Then through python file "convert_asm_bin.py" convert your program file to binary format.

        > python convert_asm_bin.py --asm=third_program

* output file will be created as "third_program_binary.txt" with instructions in binary format.
* Then run mips through the following command.

        > python MIPS_PIPELINE.py   --input=third_program

* python program loads all the binary instructions in "third_program_binary.txt" and runs them.
* output report for that program will be stored in "third_program_out.rpt".

* verilog model expects instructions in hexadecimal format.
* first write your program in a file similar to the programs given.
* Then through python file "convert_asm_hexa.py" convert your program file to hexadecimal format.

        > python convert_asm_hexa.py --asm=third_program

* output file will be created as "third_program_hexa.txt" with instructions in hexa format.
* change the instruction file in "if_fetch.v" and "mips_pipeline_tb.v" as "third_program_hexa.txt"
* Then run mips through the following command.

        > iverilog -o mips_pipeline mips_pipeline_tb.v mips_pipeline.v

        > vvp mips_pipeline

* output report for that program will be stored in "third_program_report.rpt".
* You can try running both the models with other given programs in the same above process.
* uploading binary and hexadecimal files of "third_program" 
* uploading reports of both python and verilog for "third_program"
* Both the models generate "vcd" files. you can view them using "GTKWAVE"
* All the six programs uploded here have been tested on both models and they are all passing. 

