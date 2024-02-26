module tb_sdram_test;

reg master_clk_i;
wire sdram_clk_o;
reg sdram_clk_i;
reg led_disp_d0_o;
reg led_disp_d1_o;
reg led_disp_d2_o;
reg led_disp_d3_o;
reg led_disp_d4_o;
reg led_disp_d5_o;
reg led_disp_d6_o;
reg led_disp_d7_o;
wire [3:0] led_status;
reg pb_i;
wire sd_intf_cke;
wire sd_intf_cs;
wire sd_intf_cas;
wire sd_intf_ras;
wire sd_intf_we;
wire [1:0] sd_intf_bs;
wire [12:0] sd_intf_addr;
wire sd_intf_dqml;
wire sd_intf_dqmh;
wire [15:0] sd_intf_dq;

initial begin
    $from_myhdl(
        master_clk_i,
        sdram_clk_i,
        led_disp_d0_o,
        led_disp_d1_o,
        led_disp_d2_o,
        led_disp_d3_o,
        led_disp_d4_o,
        led_disp_d5_o,
        led_disp_d6_o,
        led_disp_d7_o,
        pb_i
    );
    $to_myhdl(
        sdram_clk_o,
        led_status,
        sd_intf_cke,
        sd_intf_cs,
        sd_intf_cas,
        sd_intf_ras,
        sd_intf_we,
        sd_intf_bs,
        sd_intf_addr,
        sd_intf_dqml,
        sd_intf_dqmh,
        sd_intf_dq
    );
end

sdram_test dut(
    master_clk_i,
    sdram_clk_o,
    sdram_clk_i,
    led_disp_d0_o,
    led_disp_d1_o,
    led_disp_d2_o,
    led_disp_d3_o,
    led_disp_d4_o,
    led_disp_d5_o,
    led_disp_d6_o,
    led_disp_d7_o,
    led_status,
    pb_i,
    sd_intf_cke,
    sd_intf_cs,
    sd_intf_cas,
    sd_intf_ras,
    sd_intf_we,
    sd_intf_bs,
    sd_intf_addr,
    sd_intf_dqml,
    sd_intf_dqmh,
    sd_intf_dq
);

endmodule
