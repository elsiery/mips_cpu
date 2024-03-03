/////////////////////////////////////////////////////////////////////
//
//
//Author : Elsie Rezinold Yedida
//
//
//
/////////////////////////////////////////////////////////////////////






`timescale 1ns/1ps
module mips_pipeline_tb;

reg clk;
reg rst_n;
reg start;
wire issue;
reg [31:0] i_mem [0:44];
reg [31:0] d_mem [0:1023];
reg [31:0] r_mem [0:31];
reg [5:0] t_opcode;
reg [5:0] q_opcode;
reg [4:0] t_rs;
reg [4:0] t_rt;
reg [4:0] q_rt;
reg [4:0] t_rd;
reg [4:0] t_shamt;
reg [5:0] t_func;
reg [15:0] t_imm;
reg [31:0] t_alu_out;
reg [31:0] q_alu_out;
reg [31:0] t_mem_access;
integer i,r,j,k,l,m,n,p,fetch,decode,execute,mem_access_number,wb_number,q;
reg [31:0] temp_3,temp_4;
reg [31:0] r_alu_out,addr,comp,comp_addr;
reg [31:0] r_mem_out;
reg [5:0] r_opcode;
reg [4:0] r_rt,r_rd;
integer ins_number;
integer rpt;

//reg [31:0] t_instruction;
mips_pipeline u_dut (
    clk,
    rst_n,
    start,
    issue
);

always #5 clk = ~clk;
initial begin
    $readmemh("first_program_hexa.txt",i_mem);
    rpt = $fopen("first_program_report.rpt");
    ins_number=45;
end

initial begin
   	$dumpfile("mips_waves.vcd");
   	$dumpvars();
end 


initial begin
    clk = 1'b0;
    rst_n=1'b1;
    start = 1'b0;
    for (n=0;n<32;n=n+1) begin
        r_mem[n]=32'd0;
    end
    for(p=0;p<1024;p=p+1) begin
        d_mem[p]=32'd0;
    end
    @(negedge clk);
    rst_n = 1'b0;
    @(negedge clk);
    rst_n = 1'b1;
    @(posedge clk);
    start = 1'b1;

    #500;
end

initial begin
    @(negedge clk);
    @(negedge clk);
    @(posedge clk);
    fetch = 0;
    for(i=0;i<ins_number;i=i+1) begin
        #1;
        if ((i==u_dut.pc)&&(i_mem[i]==u_dut.w_instruction)) begin
            $display("Fetch stage is accurate for instruction %d",i);
            fetch = fetch+1;
        end
        else begin 
            $display("Fetch stage is not accurate for instruction %d",i);
        end
        @(posedge clk);
    end
end

initial begin
    @(negedge clk);
    @(negedge clk);
    @(posedge clk);
    @(posedge clk);
    decode = 0;
    for(j=0;j<ins_number;j=j+1) begin
        #1;
        t_opcode = i_mem[j][31:26];
        t_rs = i_mem[j][25:21];
        t_rt = i_mem[j][20:16];
        t_rd = i_mem[j][15:11];
        t_shamt = i_mem[j][10:6];
        t_func = i_mem[j][5:0];
        t_imm = i_mem[j][15:0];
        if ((t_opcode==u_dut.opcode)&&
            (t_rs==u_dut.rs) &&
            (t_rt==u_dut.rt) &&
            (t_rd==u_dut.rd) &&
            (t_shamt==u_dut.shamt) &&
            (t_func==u_dut.func)&&
            (t_imm==u_dut.imm)) begin
            $display("decode stage is accurate for instruction %d",j);
            decode = decode+1;
        end
        else begin 
            $display("decode stage is not accurate for instruction %d",j);
        end
        @(posedge clk);
    end
end

initial begin
    @(negedge clk);
    @(negedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    execute = 0;
    for(k=0;k<ins_number;k=k+1) begin
        #1;
        t_alu_out = m_alu_out(k);
        if((t_alu_out==u_dut.w_alu_out_data)) begin
            $display("Alu is accurate for instruction %d",k);
            //$display("%d %d",t_alu_out,u_dut.w_alu_out_data);
            execute=execute+1;
        end 
        else begin
            $display("Alu is not accurate for instruction %d",k);
            $display("%h %h",t_alu_out,u_dut.w_alu_out_data);
            $finish;
        end
        @(posedge clk);
    end
    //$finish;
end

initial begin
    @(negedge clk);
    @(negedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    mem_access_number = 0;
    for(q=0;q<ins_number;q=q+1) begin
        #1;
        t_mem_access = mem_access(q);
        q_alu_out = m_alu_out(q);
        q_opcode = i_mem[q][31:26];
        q_rt = i_mem[q][20:16];
        if (q_opcode==40) begin
            temp_3 = r_mem[q_rt];
            temp_4 = temp_3[7:0];
            d_mem[q_alu_out][7:0] = temp_4[7:0];
        end
        else if (q_opcode==41) begin
            temp_3 = r_mem[q_rt];
            temp_4 = temp_3[15:0];
            d_mem[q_alu_out][15:0] = temp_4[15:0];
        end
        else if (q_opcode==43) begin
            temp_3 = r_mem[q_rt];
            temp_4 = temp_3;
            d_mem[q_alu_out] = temp_4;
        end
        if((q_opcode >= 32)&&(q_opcode<=37)) begin
            if(t_mem_access==u_dut.w_mem_out_data) begin
                $display("memory rd is accurate for instruction %d",q);
                mem_access_number = mem_access_number+1;
            end
            else begin
                $display ("memory rd is not accurate for instruction %d",q);
                $display ("%d  %d",u_dut.w_mem_out_data,t_mem_access);
            end
        end
        else 
            mem_access_number = mem_access_number+1;

        @(posedge clk);
    end
    //$finish;
end

initial begin
    @(negedge clk);
    @(negedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    @(posedge clk);
    wb_number = 0;
    for(r=0;r<ins_number;r=r+1) begin
        #1;
        r_alu_out = m_alu_out(r);
        r_mem_out = mem_access(r);
        r_opcode = i_mem[r][31:26];
        r_rt = i_mem[r][20:16];
        r_rd = i_mem[r][15:11];
        if (r_opcode==0) begin
            addr = r_rd;
            r_mem[addr] = r_alu_out;
            comp = r_alu_out;
            comp_addr = addr;
        end
        else if((r_opcode>=8)&&(r_opcode<=15)) begin
            addr = r_rt;
            r_mem[addr] = r_alu_out;
            comp = r_alu_out;
            comp_addr = addr;
        end
        else if((r_opcode >= 32)&&(r_opcode <= 37)) begin
            addr = r_rt;
            r_mem[addr] = r_mem_out;
            comp = r_mem_out;
            comp_addr = addr;
        end
        if ((r_opcode==0)||((r_opcode>=8)&&(r_opcode<=15))||((r_opcode >= 32)&&(r_opcode <= 37))) begin
            if ((comp==u_dut.w_wb_wr_data)&&(comp_addr==u_dut.w_wb_wr_addr)) begin
                $display ("WB is accurate for instruction %d",r);
                wb_number = wb_number+1;
            end
            else begin
                $display ("WB is not accurate for %d",r);
                $display ("%d %d",comp,u_dut.w_wb_wr_data);
                $display ("%d %d",comp_addr,u_dut.w_wb_wr_addr);
            end
        end
        else
            wb_number = wb_number+1;
        @(posedge clk);
    end
    if ((fetch==ins_number) &&
        (decode==ins_number) &&
        (execute==ins_number)&&
        (mem_access_number==ins_number)&&
        (wb_number==ins_number)
        )
        $display("All instructions are passing");
        $fdisplay(rpt,"All %d instructions are passing",ins_number);

    $finish;
end






function [31:0] m_alu_out;
    input integer m;
    reg [31:0] m_op1_data,m_op2_data;
    reg [5:0] m_opcode;
    reg [4:0] m_rs;
    reg [4:0] m_rt;
    reg [4:0] m_rd;
    reg [4:0] m_shamt;
    reg [5:0] m_func;
    reg [15:0] m_imm;    
    begin
        m_opcode = i_mem[m][31:26];
        m_rs = i_mem[m][25:21];
        m_rt = i_mem[m][20:16];
        m_rd = i_mem[m][15:11];
        m_shamt = i_mem[m][10:6];
        m_func = i_mem[m][5:0];
        m_imm = i_mem[m][15:0];
        //$display("%d",m);
        if (m_opcode==0) begin
            if((m_func==0)||(m_func==2)||(m_func==3)) begin
                m_op1_data = r_mem[m_rt];
                m_op2_data = m_shamt;
            end
            else if((m_func==4)||(m_func==6)||(m_func==7)) begin
                m_op1_data = r_mem[m_rt];
                m_op2_data = r_mem[m_rs];
            end
            else begin
                m_op1_data = r_mem[m_rs];
                m_op2_data = r_mem[m_rt];
            end
        end
        else if (m_opcode >= 8) begin
            //$display("m_op=%d",m_opcode);

            if (((m_opcode>=8)&&(m_opcode<=11))||((m_opcode>=32)&&(m_opcode<=43))) begin
                m_op1_data = r_mem[m_rs];
                m_op2_data = {{16{m_imm[15]}},m_imm};
                //$display("m_op1=%d",m_op1_data);
                //$display("m_op2=%d",m_op2_data);
                //$display("m_op=%d",m_opcode);
                //$display("1111111");

            end
            else if ((m_opcode>=12)&&(m_opcode<=14)) begin
                m_op1_data = r_mem[m_rs];
                m_op2_data = {{16{1'b0}},m_imm};
                //$display("m_op1=%d",m_op1_data);
                //$display("m_op2=%d",m_op2_data);
                //$display("m_op=%d",m_opcode);
                //$display("2222");

            end
            else if (m_opcode==15) begin
                m_op1_data = 0;
                m_op2_data= m_imm;
                //$display("3333");
            end
        end
        else begin
            m_op1_data=0;
            m_op2_data=0;
        end
            //        $display("%h        %h",m_op1_data,m_op2_data);
        if (((m_opcode==0)&&((m_func == 32)||(m_func==33)))||((m_opcode==8)||(m_opcode==9)||(m_opcode==32)||(m_opcode==33)||(m_opcode==34)||(m_opcode==36)||(m_opcode==37)||(m_opcode==40)||(m_opcode==41)||(m_opcode==43)))
            m_alu_out = m_op1_data+m_op2_data;
        else if ((m_opcode==0)&&((m_func == 34)||(m_func==35)))
            m_alu_out = m_op1_data-m_op2_data;
        else if (((m_opcode==0)&&(m_func ==36))||(m_opcode==12))
            m_alu_out = m_op1_data&m_op2_data;
        else if (((m_opcode==0)&&(m_func ==37))||(m_opcode==13))
            m_alu_out = m_op1_data | m_op2_data;
        else if (((m_opcode==0)&&(m_func ==38))||(m_opcode==14))
            m_alu_out = m_op1_data ^ m_op2_data;
        else if ((m_opcode==0)&&(m_func ==39))
            m_alu_out = ~(m_op1_data|m_op2_data);
        else if (((m_opcode==0)&&((m_func == 42)||(m_func == 43)))|((m_opcode ==10)||(m_opcode==11)))
            if ($signed(m_op1_data)<$signed(m_op2_data))
                m_alu_out = 1;
            else
                m_alu_out = 0;
        else if (m_opcode==15)
            m_alu_out = {m_imm,{16{1'b0}}};
        else if ((m_opcode==0)&&((m_func==0)||(m_func==4)))
            m_alu_out = m_op1_data << m_op2_data;
        else if ((m_opcode==0)&((m_func==2)||(m_func==6)))
            m_alu_out = m_op1_data >> m_op2_data;
        else
            m_alu_out=0;
    end

endfunction

function [31:0] mem_access;
    input integer l;
    reg [5:0] l_opcode;
    reg [31:0] temp;
    reg [31:0] alu_out;
    reg [7:0] temp_1;
    reg [15:0] temp_2;
    begin
        l_opcode = i_mem[l][31:26];

        if ((l_opcode >= 32)&&(l_opcode<=37)) begin
            alu_out=m_alu_out(l);
            temp = d_mem[alu_out];
        end
        else begin 
            temp=0;
        end
        if (l_opcode==32) begin
            temp_1 = temp[7:0];
            mem_access = {{24{temp_1[7]}},temp_1};
        end
        else if (l_opcode==33) begin
            temp_2 = temp[15:0];
            mem_access = {{16{temp_2[15]}},temp_2};
        end
        else if (l_opcode==34) begin
            mem_access = temp;
        end
        else if (t_opcode==36) begin
            temp_1 = temp[7:0];
            mem_access = {{24{1'b0}},temp_1};
        end
        else if (t_opcode==37) begin
            temp_2 = temp[15:0];
            mem_access = {{16{1'b0}},temp_2};
        end
        else 
            mem_access=0;
    end
endfunction



















endmodule
