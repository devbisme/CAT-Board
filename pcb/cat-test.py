# -*- coding: utf-8 -*-

from skidl import *

KICAD_LIBS = r'C:\xesscorp\KiCad\share-kicad-03-01-2018\kicad\library'
XESS_LIBS = r'C:\xesscorp\KiCad\libraries'

skidl.lib_search_paths[KICAD].extend([KICAD_LIBS, XESS_LIBS])


def C__xesscorp_PRODUCTS_CAT_pcb_cat_flat_py():

    #===============================================================================
    # Component templates.
    #===============================================================================

    CAT_rescue_BARREL_JACK_Connect_BARREL_JACK = Part('CAT-rescue', 'BARREL_JACK', footprint='Connect:BARREL_JACK', dest=TEMPLATE)
    setattr(CAT_rescue_BARREL_JACK_Connect_BARREL_JACK, 'manf#', 'PJ-002A')

    CAT_rescue_DIPSW4_XESS_xess_DS_04 = Part('CAT-rescue', 'DIPSW4', footprint='XESS:xess-DS-04', dest=TEMPLATE)
    setattr(CAT_rescue_DIPSW4_XESS_xess_DS_04, 'manf#', '1825360-3')
    setattr(CAT_rescue_DIPSW4_XESS_xess_DS_04, 'assembly_order', '76')

    CAT_rescue_JUMPER3_XESS_HDR_1x3 = Part('CAT-rescue', 'JUMPER3', footprint='XESS:HDR_1x3', dest=TEMPLATE)

    CAT_rescue_JUMPER_RESCUE_CAT_XESS_S_JUMPER_2 = Part('CAT-rescue', 'JUMPER-RESCUE-CAT', footprint='XESS:S_JUMPER_2', dest=TEMPLATE)

    CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603 = Part('CAT-rescue', 'LED-RESCUE-CAT', footprint='LEDs:LED-0603', dest=TEMPLATE)
    setattr(CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603, 'manf#', 'LTST-C190KFKT')
    setattr(CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603, 'assembly_order', '55')

    CAT_rescue_SDRAM_XESS_TSOPII_54 = Part('CAT-rescue', 'SDRAM', footprint='XESS:TSOPII-54', dest=TEMPLATE)
    setattr(CAT_rescue_SDRAM_XESS_TSOPII_54, 'manf', 'Alliance Memory Inc.')
    setattr(CAT_rescue_SDRAM_XESS_TSOPII_54, 'manf#', 'AS4C16M16S-6TCN')
    setattr(CAT_rescue_SDRAM_XESS_TSOPII_54, 'assembly_order', '65')

    CAT_rescue_SERIAL_FLASH_SMD_Packages_SOIC_8_N = Part('CAT-rescue', 'SERIAL_FLASH', footprint='SMD_Packages:SOIC-8-N', dest=TEMPLATE)
    setattr(CAT_rescue_SERIAL_FLASH_SMD_Packages_SOIC_8_N, 'manf#', 'AT25SF041-SSHD-T')
    setattr(CAT_rescue_SERIAL_FLASH_SMD_Packages_SOIC_8_N, 'assembly_order', '74')

    CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT = Part('CAT-rescue', 'SW_PUSH', footprint='XESS:RS-282G05A3-SM_RT', dest=TEMPLATE)
    setattr(CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT, 'manf#', 'RS-282G05A3-SM RT')
    setattr(CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT, 'assembly_order', '73')

    Lattice_iCE_iCE40_HX8K_CT256_XESS_Lattice_caBGA_256 = Part('Lattice-iCE', 'iCE40-HX8K-CT256', footprint='XESS:Lattice_caBGA_256', dest=TEMPLATE)
    setattr(Lattice_iCE_iCE40_HX8K_CT256_XESS_Lattice_caBGA_256, 'manf#', 'ICE40HX8K-CT256')
    setattr(Lattice_iCE_iCE40_HX8K_CT256_XESS_Lattice_caBGA_256, 'assembly_order', '1')

    XESS_1117_XESS_SOT_223 = Part('XESS', '1117', footprint='XESS:SOT-223', dest=TEMPLATE)
    setattr(XESS_1117_XESS_SOT_223, 'keywords', 'voltage regulator, fixed')
    setattr(XESS_1117_XESS_SOT_223, 'manf#', 'AZ1117CH-ADJTRG1')
    setattr(XESS_1117_XESS_SOT_223, 'assembly_order', '51')
    setattr(XESS_1117_XESS_SOT_223, 'description', 'fixed-output voltage regulator')

    XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N = Part('XESS', 'EEPROM_I2C', footprint='SMD_Packages:SOIC-8-N', dest=TEMPLATE)
    setattr(XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N, 'keywords', 'EEPROM Serial')
    setattr(XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N, 'manf#', 'CAT24C32WI-GT3')
    setattr(XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N, 'assembly_order', '75')
    setattr(XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N, 'description', 'I2C Serial EEPROM')

    XESS_Grove_Male_XESS_GROVE_MALE = Part('XESS', 'Grove_Male', footprint='XESS:GROVE_MALE', dest=TEMPLATE)
    setattr(XESS_Grove_Male_XESS_GROVE_MALE, 'keywords', 'Seeed, Grove, connector, male')
    setattr(XESS_Grove_Male_XESS_GROVE_MALE, 'manf#', 'B4B-PH-K-S(LF)(SN)')
    setattr(XESS_Grove_Male_XESS_GROVE_MALE, 'assembly_order', '82')
    setattr(XESS_Grove_Male_XESS_GROVE_MALE, 'description', 'Seeed Grove male connector')

    XESS_JSHORTNORMAL_XESS_xess_JSHORT = Part('XESS', 'JSHORTNORMAL', footprint='XESS:xess-JSHORT', dest=TEMPLATE)

    XESS_OSC_XESS_2_5x3_2 = Part('XESS', 'OSC', footprint='XESS:2.5x3.2', dest=TEMPLATE)
    setattr(XESS_OSC_XESS_2_5x3_2, 'manf#', '501ACA100M000CAG')
    setattr(XESS_OSC_XESS_2_5x3_2, 'assembly_order', '2')

    XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12 = Part('XESS', 'PMOD_SCKT-12', footprint='XESS:PMOD_SCKT-12', dest=TEMPLATE)
    setattr(XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12, 'keywords', 'PMOD, header')
    setattr(XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12, 'assembly_order', '79')
    setattr(XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12, 'description', 'PMOD header')

    XESS_RN2_XESS_CTS_742C043 = Part('XESS', 'RN2', footprint='XESS:CTS_742C043', dest=TEMPLATE)
    setattr(XESS_RN2_XESS_CTS_742C043, 'manf#', '742C043472JP')
    setattr(XESS_RN2_XESS_CTS_742C043, 'assembly_order', '59')

    XESS_RN4_XESS_CTS_742C083 = Part('XESS', 'RN4', footprint='XESS:CTS_742C083', dest=TEMPLATE)
    setattr(XESS_RN4_XESS_CTS_742C083, 'manf#', '742C083201JP')
    setattr(XESS_RN4_XESS_CTS_742C083, 'assembly_order', '49')

    XESS_RPi_GPIO_RPi_Hat_Pin_Header_Straight_2x20 = Part('XESS', 'RPi_GPIO', footprint='RPi_Hat:Pin_Header_Straight_2x20', dest=TEMPLATE)

    XESS_SATA_CONN_XESS_SATA_MOLEX_67491 = Part('XESS', 'SATA_CONN', footprint='XESS:SATA-MOLEX-67491', dest=TEMPLATE)
    setattr(XESS_SATA_CONN_XESS_SATA_MOLEX_67491, 'manf#', '674911032')

    XESS_TPTP_COMPACT_Measurement_Points_Measurement_Point_Round_TH_Small = Part('XESS', 'TPTP-COMPACT', footprint='Measurement_Points:Measurement_Point_Round-TH_Small', dest=TEMPLATE)

    conn_Conn_02x10_Pin_Headers_Pin_Header_Straight_2x10 = Part('conn', 'Conn_02x10', footprint='Pin_Headers:Pin_Header_Straight_2x10', dest=TEMPLATE)
    setattr(conn_Conn_02x10_Pin_Headers_Pin_Header_Straight_2x10, 'assembly_order', '77')

    device_CP1_Capacitors_SMD_c_elec_6_3x5_3 = Part('device', 'CP1', footprint='Capacitors_SMD:c_elec_6.3x5.3', dest=TEMPLATE)
    setattr(device_CP1_Capacitors_SMD_c_elec_6_3x5_3, 'keywords', 'cap capacitor')
    setattr(device_CP1_Capacitors_SMD_c_elec_6_3x5_3, 'manf#', 'UWX1A101MCL1GB')
    setattr(device_CP1_Capacitors_SMD_c_elec_6_3x5_3, 'description', 'Polarised capacitor')

    device_C_Capacitors_SMD_C_0603 = Part('device', 'C', footprint='Capacitors_SMD:C_0603', dest=TEMPLATE)
    setattr(device_C_Capacitors_SMD_C_0603, 'keywords', 'cap capacitor')
    setattr(device_C_Capacitors_SMD_C_0603, 'manf#', 'GRM188R71C105KE15D')
    setattr(device_C_Capacitors_SMD_C_0603, 'assembly_order', '39')
    setattr(device_C_Capacitors_SMD_C_0603, 'description', 'Unpolarized capacitor')

    device_C_Capacitors_SMD_C_0805 = Part('device', 'C', footprint='Capacitors_SMD:C_0805', dest=TEMPLATE)
    setattr(device_C_Capacitors_SMD_C_0805, 'keywords', 'cap capacitor')
    setattr(device_C_Capacitors_SMD_C_0805, 'manf#', 'GRM21BR61A106KE19L')
    setattr(device_C_Capacitors_SMD_C_0805, 'assembly_order', '45')
    setattr(device_C_Capacitors_SMD_C_0805, 'description', 'Unpolarized capacitor')

    device_D_Diodes_SMD_SOD_323 = Part('device', 'D', footprint='Diodes_SMD:SOD-323', dest=TEMPLATE)
    setattr(device_D_Diodes_SMD_SOD_323, 'keywords', 'diode')
    setattr(device_D_Diodes_SMD_SOD_323, 'manf#', '1N4448WX-TP')
    setattr(device_D_Diodes_SMD_SOD_323, 'assembly_order', '34')
    setattr(device_D_Diodes_SMD_SOD_323, 'description', 'Diode')

    device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23 = Part('device', 'Q_PMOS_GSD', footprint='Housings_SOT-23_SOT-143_TSOT-6:SOT-23', dest=TEMPLATE)
    setattr(device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23, 'keywords', 'pmos p-mos p-mosfet transistor')
    setattr(device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23, 'manf#', 'DMP3098L-7')
    setattr(device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23, 'assembly_order', '64')
    setattr(device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23, 'description', 'Transistor P-MOSFET with substrate diode (general)')

    device_R_Resistors_SMD_R_0603 = Part('device', 'R', footprint='Resistors_SMD:R_0603', dest=TEMPLATE)
    setattr(device_R_Resistors_SMD_R_0603, 'keywords', 'r res resistor')
    setattr(device_R_Resistors_SMD_R_0603, 'manf#', 'RC0603FR-071K87L')
    setattr(device_R_Resistors_SMD_R_0603, 'assembly_order', '47')
    setattr(device_R_Resistors_SMD_R_0603, 'description', 'Resistor')

    device_R_Resistors_SMD_R_0805_HandSoldering = Part('device', 'R', footprint='Resistors_SMD:R_0805_HandSoldering', dest=TEMPLATE)
    setattr(device_R_Resistors_SMD_R_0805_HandSoldering, 'keywords', 'r res resistor')
    setattr(device_R_Resistors_SMD_R_0805_HandSoldering, 'manf#', 'RC0603FR-07768RL')
    setattr(device_R_Resistors_SMD_R_0805_HandSoldering, 'assembly_order', '48')
    setattr(device_R_Resistors_SMD_R_0805_HandSoldering, 'description', 'Resistor')

    device_R_Small_Resistors_SMD_R_0402 = Part('device', 'R_Small', footprint='Resistors_SMD:R_0402', dest=TEMPLATE)
    setattr(device_R_Small_Resistors_SMD_R_0402, 'keywords', 'r resistor')
    setattr(device_R_Small_Resistors_SMD_R_0402, 'manf#', 'RC0402JR-07100RL')
    setattr(device_R_Small_Resistors_SMD_R_0402, 'description', 'Resistor, small symbol')


    #===============================================================================
    # Component instantiations.
    #===============================================================================

    C1 = device_CP1_Capacitors_SMD_c_elec_6_3x5_3(ref='C1', value='100uF')

    C10 = device_C_Capacitors_SMD_C_0603(ref='C10', value='0.1uF')
    setattr(C10, 'manf#', 'GRM188R71C104KA01D')
    setattr(C10, 'assembly_order', '36')

    C11 = device_C_Capacitors_SMD_C_0603(ref='C11', value='1.0uF')
    setattr(C11, 'assembly_order', '43')

    C12 = device_C_Capacitors_SMD_C_0603(ref='C12', value='0.1uF')
    setattr(C12, 'manf#', 'GRM188R71C104KA01D')
    setattr(C12, 'assembly_order', '42')

    C13 = device_C_Capacitors_SMD_C_0603(ref='C13', value='1.0uF')
    setattr(C13, 'assembly_order', '37')

    C14 = device_C_Capacitors_SMD_C_0603(ref='C14', value='0.1uF')
    setattr(C14, 'manf#', 'GRM188R71C104KA01D')
    setattr(C14, 'assembly_order', '40')

    C16 = device_C_Capacitors_SMD_C_0603(ref='C16', value='0.1uF')
    setattr(C16, 'manf#', 'GRM188R71C104KA01D')
    setattr(C16, 'assembly_order', '19')

    C17 = device_C_Capacitors_SMD_C_0603(ref='C17', value='0.1uF')
    setattr(C17, 'manf#', 'GRM188R71C104KA01D')
    setattr(C17, 'assembly_order', '5')

    C18 = device_C_Capacitors_SMD_C_0603(ref='C18', value='0.1uF')
    setattr(C18, 'manf#', 'GRM188R71C104KA01D')
    setattr(C18, 'assembly_order', '29')

    C19 = device_C_Capacitors_SMD_C_0603(ref='C19', value='0.1uF')
    setattr(C19, 'manf#', 'GRM188R71C104KA01D')
    setattr(C19, 'assembly_order', '24')

    C2 = device_C_Capacitors_SMD_C_0805(ref='C2', value='10uF')
    setattr(C2, 'assembly_order', '66')

    C20 = device_C_Capacitors_SMD_C_0603(ref='C20', value='1.0uF')
    setattr(C20, 'assembly_order', '18')

    C21 = device_C_Capacitors_SMD_C_0603(ref='C21', value='1.0uF')
    setattr(C21, 'assembly_order', '12')

    C22 = device_C_Capacitors_SMD_C_0603(ref='C22', value='1.0uF')
    setattr(C22, 'assembly_order', '28')

    C23 = device_C_Capacitors_SMD_C_0603(ref='C23', value='1.0uF')
    setattr(C23, 'assembly_order', '23')

    C24 = device_C_Capacitors_SMD_C_0603(ref='C24', value='0.1uF')
    setattr(C24, 'manf#', 'GRM188R71C104KA01D')
    setattr(C24, 'assembly_order', '17')

    C25 = device_C_Capacitors_SMD_C_0603(ref='C25', value='0.1uF')
    setattr(C25, 'manf#', 'GRM188R71C104KA01D')
    setattr(C25, 'assembly_order', '32')

    C26 = device_C_Capacitors_SMD_C_0603(ref='C26', value='0.1uF')
    setattr(C26, 'manf#', 'GRM188R71C104KA01D')
    setattr(C26, 'assembly_order', '30')

    C27 = device_C_Capacitors_SMD_C_0603(ref='C27', value='0.1uF')
    setattr(C27, 'manf#', 'GRM188R71C104KA01D')
    setattr(C27, 'assembly_order', '21')

    C28 = device_C_Capacitors_SMD_C_0603(ref='C28', value='1.0uF')
    setattr(C28, 'assembly_order', '16')

    C29 = device_C_Capacitors_SMD_C_0603(ref='C29', value='1.0uF')
    setattr(C29, 'assembly_order', '35')

    C3 = device_C_Capacitors_SMD_C_0805(ref='C3', value='10uF')
    setattr(C3, 'assembly_order', '67')

    C30 = device_C_Capacitors_SMD_C_0603(ref='C30', value='1.0uF')
    setattr(C30, 'assembly_order', '26')

    C31 = device_C_Capacitors_SMD_C_0603(ref='C31', value='1.0uF')
    setattr(C31, 'assembly_order', '20')

    C32 = device_C_Capacitors_SMD_C_0805(ref='C32', value='10uF')
    setattr(C32, 'assembly_order', '27')

    C33 = device_C_Capacitors_SMD_C_0805(ref='C33', value='10uF')
    setattr(C33, 'assembly_order', '10')

    C34 = device_C_Capacitors_SMD_C_0603(ref='C34', value='0.1uF')
    setattr(C34, 'manf#', 'GRM188R71C104KA01D')
    setattr(C34, 'assembly_order', '6')

    C35 = device_C_Capacitors_SMD_C_0603(ref='C35', value='0.1uF')
    setattr(C35, 'manf#', 'GRM188R71C104KA01D')
    setattr(C35, 'assembly_order', '11')

    C38 = device_C_Capacitors_SMD_C_0603(ref='C38', value='1.0uF')
    setattr(C38, 'assembly_order', '22')

    C39 = device_C_Capacitors_SMD_C_0603(ref='C39', value='1.0uF')
    setattr(C39, 'assembly_order', '15')

    C4 = device_C_Capacitors_SMD_C_0805(ref='C4', value='10uF')
    setattr(C4, 'assembly_order', '68')

    C40 = device_C_Capacitors_SMD_C_0603(ref='C40', value='0.1uF')
    setattr(C40, 'manf#', 'GRM188R71C104KA01D')
    setattr(C40, 'assembly_order', '9')

    C41 = device_C_Capacitors_SMD_C_0603(ref='C41', value='0.1uF')
    setattr(C41, 'manf#', 'GRM188R71C104KA01D')
    setattr(C41, 'assembly_order', '14')

    C42 = device_C_Capacitors_SMD_C_0603(ref='C42', value='0.1uF')
    setattr(C42, 'manf#', 'GRM188R71C104KA01D')
    setattr(C42, 'assembly_order', '7')

    C43 = device_C_Capacitors_SMD_C_0603(ref='C43', value='0.01uF')
    setattr(C43, 'manf#', 'GRM188R71H103KA01D')
    setattr(C43, 'assembly_order', '13')

    C44 = device_C_Capacitors_SMD_C_0603(ref='C44', value='0.1uF')
    setattr(C44, 'manf#', 'GRM188R71C104KA01D')
    setattr(C44, 'assembly_order', '4')

    C45 = device_C_Capacitors_SMD_C_0603(ref='C45', value='0.1uF')
    setattr(C45, 'manf#', 'GRM188R71C104KA01D')
    setattr(C45, 'assembly_order', '31')

    C46 = device_C_Capacitors_SMD_C_0603(ref='C46', value='0.01uF')
    setattr(C46, 'manf#', 'GRM188R71H103KA01D')
    setattr(C46, 'assembly_order', '3')

    C47 = device_C_Capacitors_SMD_C_0603(ref='C47', value='0.1uF')
    setattr(C47, 'manf#', 'GRM188R71C104KA01D')
    setattr(C47, 'assembly_order', '25')

    C48 = device_C_Capacitors_SMD_C_0603(ref='C48', value='0.1uF')
    setattr(C48, 'manf#', 'GRM188R71C104KA01D')
    setattr(C48, 'assembly_order', '63')

    C5 = device_C_Capacitors_SMD_C_0603(ref='C5', value='0.1uF')
    setattr(C5, 'manf#', 'GRM188R71C104KA01D')
    setattr(C5, 'assembly_order', '44')

    C6 = device_C_Capacitors_SMD_C_0805(ref='C6', value='10uF')

    C8 = device_C_Capacitors_SMD_C_0603(ref='C8', value='0.1uF')
    setattr(C8, 'manf#', 'GRM188R71C104KA01D')
    setattr(C8, 'assembly_order', '41')

    C9 = device_C_Capacitors_SMD_C_0603(ref='C9', value='1.0uF')

    CON1 = CAT_rescue_BARREL_JACK_Connect_BARREL_JACK(ref='CON1', value='BARREL_JACK')

    D1 = device_D_Diodes_SMD_SOD_323(ref='D1', value='D')

    GPIO1 = XESS_RPi_GPIO_RPi_Hat_Pin_Header_Straight_2x20(ref='GPIO1', value='RPi_GPIO')

    GR1 = XESS_Grove_Male_XESS_GROVE_MALE(ref='GR1', value='Grove')
    setattr(GR1, 'assembly_order', '80')

    GR2 = XESS_Grove_Male_XESS_GROVE_MALE(ref='GR2', value='Grove')
    setattr(GR2, 'assembly_order', '81')

    GR3 = XESS_Grove_Male_XESS_GROVE_MALE(ref='GR3', value='Grove')

    GR4 = XESS_Grove_Male_XESS_GROVE_MALE(ref='GR4', value='Grove')

    GR5 = XESS_Grove_Male_XESS_GROVE_MALE(ref='GR5', value='Grove')

    HDR1 = conn_Conn_02x10_Pin_Headers_Pin_Header_Straight_2x10(ref='HDR1', value='CONN_02X10')

    JP1 = CAT_rescue_JUMPER_RESCUE_CAT_XESS_S_JUMPER_2(ref='JP1', value='JUMPER')

    JP2 = CAT_rescue_JUMPER3_XESS_HDR_1x3(ref='JP2', value='JUMPER3')

    JP3 = CAT_rescue_JUMPER3_XESS_HDR_1x3(ref='JP3', value='JUMPER3')

    JP4 = CAT_rescue_JUMPER3_XESS_HDR_1x3(ref='JP4', value='JUMPER3')

    JP5 = CAT_rescue_JUMPER_RESCUE_CAT_XESS_S_JUMPER_2(ref='JP5', value='JUMPER')

    JP6 = CAT_rescue_JUMPER3_XESS_HDR_1x3(ref='JP6', value='JUMPER3')

    LED1 = CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603(ref='LED1', value='LED')
    setattr(LED1, 'assembly_order', '52')

    LED2 = CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603(ref='LED2', value='LED')
    setattr(LED2, 'assembly_order', '53')

    LED3 = CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603(ref='LED3', value='LED')
    setattr(LED3, 'assembly_order', '54')

    LED4 = CAT_rescue_LED_RESCUE_CAT_LEDs_LED_0603(ref='LED4', value='LED')

    PM2 = XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12(ref='PM2', value='PMOD_SCKT-12')
    setattr(PM2, 'assembly_order', '78')

    PM3 = XESS_PMOD_SCKT_12_XESS_PMOD_SCKT_12(ref='PM3', value='PMOD_SCKT-12')

    Q1 = device_Q_PMOS_GSD_Housings_SOT_23_SOT_143_TSOT_6_SOT_23(ref='Q1', value='Q_PMOS_GSD')

    R1 = device_R_Resistors_SMD_R_0603(ref='R1', value='100')
    setattr(R1, 'manf#', 'RC0603JR-07100RL')
    setattr(R1, 'assembly_order', '33')

    R2 = device_R_Small_Resistors_SMD_R_0402(ref='R2', value='127')

    R3 = device_R_Small_Resistors_SMD_R_0402(ref='R3', value='127')

    R4 = device_R_Small_Resistors_SMD_R_0402(ref='R4', value='127')

    R5 = device_R_Small_Resistors_SMD_R_0402(ref='R5', value='127')

    R6 = device_R_Resistors_SMD_R_0603(ref='R6', value='100')
    setattr(R6, 'manf#', 'RC0603JR-07100RL')
    setattr(R6, 'assembly_order', '8')

    R7 = device_R_Resistors_SMD_R_0603(ref='R7', value='100')
    setattr(R7, 'manf#', 'RC0603JR-07100RL')
    setattr(R7, 'assembly_order', '38')

    R8 = device_R_Resistors_SMD_R_0805_HandSoldering(ref='R8', value='1260')

    R9 = device_R_Resistors_SMD_R_0603(ref='R9', value='768')

    RESET1 = CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT(ref='RESET1', value='SW_PUSH')
    setattr(RESET1, 'assembly_order', '71')

    RN1 = XESS_RN2_XESS_CTS_742C043(ref='RN1', value='4.7K')
    setattr(RN1, 'assembly_order', '57')

    RN10 = XESS_RN2_XESS_CTS_742C043(ref='RN10', value='4.7K')
    setattr(RN10, 'assembly_order', '60')

    RN11 = XESS_RN2_XESS_CTS_742C043(ref='RN11', value='4.7K')
    setattr(RN11, 'assembly_order', '61')

    RN12 = XESS_RN4_XESS_CTS_742C083(ref='RN12', value='100')
    setattr(RN12, 'manf#', '741C083101JP')

    RN2 = XESS_RN2_XESS_CTS_742C043(ref='RN2', value='100')
    setattr(RN2, 'manf#', '742C043101JP')
    setattr(RN2, 'assembly_order', '62')

    RN3 = XESS_RN2_XESS_CTS_742C043(ref='RN3', value='4.7K')
    setattr(RN3, 'assembly_order', '50')

    RN4 = XESS_RN2_XESS_CTS_742C043(ref='RN4', value='4.7K')
    setattr(RN4, 'assembly_order', '58')

    RN5 = XESS_RN4_XESS_CTS_742C083(ref='RN5', value='100')
    setattr(RN5, 'manf#', '742C083101JP')
    setattr(RN5, 'assembly_order', '56')

    RN6 = XESS_RN4_XESS_CTS_742C083(ref='RN6', value='100')
    setattr(RN6, 'manf#', '742C083101JP')
    setattr(RN6, 'assembly_order', '46')

    RN7 = XESS_RN4_XESS_CTS_742C083(ref='RN7', value='200')

    RN8 = XESS_RN4_XESS_CTS_742C083(ref='RN8', value='200')

    RN9 = XESS_RN2_XESS_CTS_742C043(ref='RN9', value='4.7K')

    SATA1 = XESS_SATA_CONN_XESS_SATA_MOLEX_67491(ref='SATA1', value='SATA_CONN')

    SATA2 = XESS_SATA_CONN_XESS_SATA_MOLEX_67491(ref='SATA2', value='SATA_CONN')

    SH1 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH1', value='JSHORTNORMAL')

    SH2 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH2', value='JSHORTNORMAL')

    SH3 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH3', value='JSHORTNORMAL')

    SH4 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH4', value='JSHORTNORMAL')

    SH5 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH5', value='JSHORTNORMAL')

    SH6 = XESS_JSHORTNORMAL_XESS_xess_JSHORT(ref='SH6', value='JSHORTNORMAL')

    SW1 = CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT(ref='SW1', value='SW_PUSH')
    setattr(SW1, 'assembly_order', '72')

    SW2 = CAT_rescue_SW_PUSH_XESS_RS_282G05A3_SM_RT(ref='SW2', value='SW_PUSH')

    SW3 = CAT_rescue_DIPSW4_XESS_xess_DS_04(ref='SW3', value='DIPSW4')

    TP_1_2V1 = XESS_TPTP_COMPACT_Measurement_Points_Measurement_Point_Round_TH_Small(ref='TP-1.2V1', value='TPTP-COMPACT')

    TP_3_3V1 = XESS_TPTP_COMPACT_Measurement_Points_Measurement_Point_Round_TH_Small(ref='TP-3.3V1', value='TPTP-COMPACT')

    TP_5V1 = XESS_TPTP_COMPACT_Measurement_Points_Measurement_Point_Round_TH_Small(ref='TP-5V1', value='TPTP-COMPACT')

    TP_GND1 = XESS_TPTP_COMPACT_Measurement_Points_Measurement_Point_Round_TH_Small(ref='TP-GND1', value='TPTP-COMPACT')

    U1 = XESS_1117_XESS_SOT_223(ref='U1', value='AZ1117EH-3.3')
    setattr(U1, 'manf#', 'AZ1117EH-3.3TRG1')
    setattr(U1, 'assembly_order', '69')

    U2 = XESS_EEPROM_I2C_SMD_Packages_SOIC_8_N(ref='U2', value='I2C Flash')

    U3 = XESS_1117_XESS_SOT_223(ref='U3', value='AZ1117EH-1.2')
    setattr(U3, 'manf#', 'AZ1117EH-1.2TRG1')
    setattr(U3, 'assembly_order', '70')

    U4 = Lattice_iCE_iCE40_HX8K_CT256_XESS_Lattice_caBGA_256(ref='U4', value='iCE40-HX8K-CT256')

    U5 = CAT_rescue_SDRAM_XESS_TSOPII_54(ref='U5', value='16Mx16 SDRAM')

    U6 = CAT_rescue_SERIAL_FLASH_SMD_Packages_SOIC_8_N(ref='U6', value='SPI Flash')

    U7 = XESS_OSC_XESS_2_5x3_2(ref='U7', value='100 MHz Osc')

    U8 = XESS_1117_XESS_SOT_223(ref='U8', value='AZ1117EH-ADJ')


    #===============================================================================
    # Net interconnections between instantiated components.
    #===============================================================================

    Net('+1.2V').connect(C38['1'], C4['1'], C40['1'], C42['1'], C44['1'], C45['1'], C46['1'], R1['2'], R6['2'], TP_1_2V1['1'], U3['2'], U3['4'], U4['A14'], U4['F10'], U4['F6'], U4['K10'], U4['K6'], U4['L2'])

    Net('+3.3V').connect(C10['1'], C11['1'], C12['1'], C13['1'], C14['1'], C16['1'], C17['1'], C18['1'], C20['1'], C21['1'], C22['1'], C24['1'], C25['1'], C26['1'], C28['1'], C29['1'], C3['1'], C30['1'], C39['1'], C41['1'], C43['1'], C47['1'], C48['1'], C5['1'], C8['1'], C9['1'], D1['2'], GR1['3'], GR2['3'], GR3['3'], JP2['3'], JP3['3'], RN1['1'], RN1['2'], RN10['1'], RN10['2'], RN11['1'], RN11['2'], RN3['3'], RN3['4'], RN4['3'], RN4['4'], RN9['1'], RN9['2'], SH3['2'], SH4['2'], TP_3_3V1['1'], U1['2'], U1['4'], U2['7'], U2['8'], U3['3'], U4['A13'], U4['A3'], U4['A8'], U4['C15'], U4['F8'], U4['H10'], U4['H15'], U4['K8'], U4['N13'], U4['N15'], U4['P3'], U4['R13'], U4['R8'], U5['1'], U5['14'], U5['27'], U5['3'], U5['43'], U5['49'], U5['9'], U6['3'], U6['7'], U6['8'], U7['1'], U7['4'])

    Net('+5V').connect(C1['1'], C2['1'], JP2['1'], JP3['1'], Q1['2'], TP_5V1['1'], U1['3'], U8['3'])

    Net('+5V-RPi').connect(GPIO1['2'], GPIO1['4'], JP4['3'], SH1['2'])

    Net('/SATA1_A_N').connect(R2['1'], RN7['2'], SATA1['3'])

    Net('/SATA1_A_P').connect(R2['2'], RN7['1'], SATA1['2'])

    Net('/SATA1_B_N').connect(R3['2'], RN7['3'], SATA1['5'])

    Net('/SATA1_B_P').connect(R3['1'], RN7['4'], SATA1['6'])

    Net('/SATA2_A_N').connect(R4['1'], RN8['2'], SATA2['3'])

    Net('/SATA2_A_P').connect(R4['2'], RN8['1'], SATA2['2'])

    Net('/SATA2_B_N').connect(R5['2'], RN8['3'], SATA2['5'])

    Net('/SATA2_B_P').connect(R5['1'], RN8['4'], SATA2['6'])

    Net('BCM0_ID_SD').connect(GPIO1['27'], RN1['4'], U2['5'])

    Net('BCM10_MOSI').connect(GPIO1['19'], RN12['1'])

    Net('BCM11_SCLK').connect(GPIO1['23'], RN12['4'])

    Net('BCM12').connect(GPIO1['32'], U4['R6'])

    Net('BCM13').connect(GPIO1['33'], U4['R5'])

    Net('BCM14_TXD').connect(GPIO1['8'], U4['T15'])

    Net('BCM15_RXD').connect(GPIO1['10'], U4['T14'])

    Net('BCM16').connect(GPIO1['36'], U4['R4'])

    Net('BCM17').connect(GPIO1['11'], JP1['1'], SH5['2'], U4['T13'])

    Net('BCM18_PCM_C').connect(GPIO1['12'], U4['T11'])

    Net('BCM19_MISO').connect(GPIO1['35'], U4['T3'])

    Net('BCM1_ID_SC').connect(GPIO1['28'], RN1['3'], U2['6'])

    Net('BCM20_MOSI').connect(GPIO1['38'], U4['R3'])

    Net('BCM21_SCLK').connect(GPIO1['40'], U4['T1'])

    Net('BCM22').connect(GPIO1['15'], JP5['1'], SH6['2'], U4['T10'])

    Net('BCM23').connect(GPIO1['16'], U4['P9'])

    Net('BCM24').connect(GPIO1['18'], U4['T9'])

    Net('BCM25').connect(GPIO1['22'], RN12['3'])

    Net('BCM26').connect(GPIO1['37'], U4['T2'])

    Net('BCM27_PCM_0').connect(GPIO1['13'], U4['R10'])

    Net('BCM2_SDA').connect(GPIO1['3'], U4['R16'])

    Net('BCM3_SCL').connect(GPIO1['5'], U4['T16'])

    Net('BCM4_GPCLK0').connect(GPIO1['7'], U4['R9'])

    Net('BCM5').connect(GPIO1['29'], U4['T6'])

    Net('BCM6').connect(GPIO1['31'], U4['T5'])

    Net('BCM7_CE1').connect(GPIO1['26'], U4['T7'])

    Net('BCM8_CE0').connect(GPIO1['24'], U4['T8'])

    Net('BCM9_MISO').connect(GPIO1['21'], RN12['2'])

    Net('DIPSW1').connect(SW3['8'], U4['C6'])

    Net('DIPSW2').connect(SW3['7'], U4['C5'])

    Net('DIPSW3').connect(SW3['6'], U4['C4'])

    Net('DIPSW4').connect(SW3['5'], U4['C3'])

    Net('GND').connect(C1['2'], C10['2'], C11['2'], C12['2'], C13['2'], C14['2'], C16['2'], C17['2'], C18['2'], C19['2'], C2['2'], C20['2'], C21['2'], C22['2'], C23['2'], C24['2'], C25['2'], C26['2'], C27['2'], C28['2'], C29['2'], C3['2'], C30['2'], C31['2'], C38['2'], C39['2'], C4['2'], C40['2'], C41['2'], C42['2'], C43['2'], C44['2'], C45['2'], C46['2'], C47['2'], C48['2'], C5['2'], C6['2'], C8['2'], C9['2'], CON1['2'], GPIO1['14'], GPIO1['20'], GPIO1['25'], GPIO1['30'], GPIO1['34'], GPIO1['39'], GPIO1['6'], GPIO1['9'], GR1['4'], GR2['4'], GR3['4'], GR4['4'], GR5['4'], HDR1['15'], JP6['3'], PM2['11'], PM2['5'], PM3['11'], PM3['5'], Q1['1'], R7['1'], R8['2'], RN2['1'], RN2['2'], RN5['5'], RN5['6'], RN5['7'], RN5['8'], RN6['5'], RN6['6'], RN6['7'], RN6['8'], SATA1['1'], SATA1['4'], SATA2['1'], SATA2['4'], SH2['1'], TP_GND1['1'], U1['1'], U2['1'], U2['2'], U2['3'], U2['4'], U3['1'], U4['A12'], U4['A4'], U4['E15'], U4['G7'], U4['G8'], U4['G9'], U4['H7'], U4['H8'], U4['H9'], U4['J7'], U4['J8'], U4['J9'], U4['K2'], U4['K7'], U4['L15'], U4['R7'], U4['T12'], U4['T4'], U5['12'], U5['28'], U5['41'], U5['46'], U5['52'], U5['54'], U5['6'], U6['4'], U7['2'])

    Net('GR1-IO1').connect(GR1['1'], RN9['4'], U4['C10'])

    Net('GR1-IO2').connect(GR1['2'], RN9['3'], U4['C9'])

    Net('GR2-IO1').connect(GR2['1'], RN10['3'], U4['C12'])

    Net('GR2-IO2').connect(GR2['2'], RN10['4'], U4['C11'])

    Net('GR3-IO1').connect(GR3['1'], RN11['3'], U4['C14'])

    Net('GR3-IO2').connect(GR3['2'], RN11['4'], U4['C13'])

    Net('HDR1-1').connect(HDR1['1'], U4['J1'])

    Net('HDR1-10').connect(HDR1['10'], U4['F1'])

    Net('HDR1-11').connect(HDR1['11'], U4['E2'])

    Net('HDR1-12').connect(HDR1['12'], U4['F3'])

    Net('HDR1-13').connect(HDR1['13'], U4['D1'])

    Net('HDR1-14').connect(HDR1['14'], U4['E3'])

    Net('HDR1-16').connect(HDR1['16'], U4['D2'])

    Net('HDR1-17').connect(HDR1['17'], U4['C2'])

    Net('HDR1-18').connect(HDR1['18'], U4['C1'])

    Net('HDR1-19').connect(HDR1['19'], U4['B2'])

    Net('HDR1-2').connect(HDR1['2'], U4['K1'])

    Net('HDR1-20').connect(HDR1['20'], U4['B1'])

    Net('HDR1-3').connect(HDR1['3'], U4['H1'])

    Net('HDR1-4').connect(HDR1['4'], U4['J2'])

    Net('HDR1-6').connect(HDR1['6'], U4['H2'])

    Net('HDR1-7').connect(HDR1['7'], U4['G2'])

    Net('HDR1-8').connect(HDR1['8'], U4['G1'])

    Net('HDR1-9').connect(HDR1['9'], U4['F2'])

    Net('LED1').connect(LED1['2'], U4['A9'])

    Net('LED2').connect(LED2['2'], U4['B8'])

    Net('LED3').connect(LED3['2'], U4['A7'])

    Net('LED4').connect(LED4['2'], U4['B7'])

    Net('Net-(C32-Pad1)').connect(C32['1'], C34['1'], U4['E7'])

    Net('Net-(C32-Pad2)').connect(C32['2'], C34['2'], R1['1'], U4['E8'])

    Net('Net-(C33-Pad1)').connect(C33['1'], C35['1'], U4['N8'])

    Net('Net-(C33-Pad2)').connect(C33['2'], C35['2'], R6['1'], U4['L8'])

    Net('Net-(CON1-Pad1)').connect(CON1['1'], JP4['1'])

    Net('Net-(CON1-Pad3)').connect(CON1['3'])

    Net('Net-(D1-Pad1)').connect(D1['1'], U4['E12'])

    Net('Net-(GPIO1-Pad1)').connect(GPIO1['1'])

    Net('Net-(GPIO1-Pad17)').connect(GPIO1['17'])

    Net('Net-(GR4-Pad3)').connect(GR4['3'], JP2['2'], PM2['12'], PM2['6'], SH3['1'])

    Net('Net-(GR5-Pad3)').connect(GR5['3'], JP3['2'], PM3['12'], PM3['6'], SH4['1'])

    Net('Net-(JP1-Pad2)').connect(JP1['2'], RN4['2'], SH5['1'], U4['M10'])

    Net('Net-(JP4-Pad2)').connect(JP4['2'], Q1['3'], SH1['1'])

    Net('Net-(JP5-Pad2)').connect(JP5['2'], RESET1['2'], RN4['1'], SH6['1'], U4['N11'])

    Net('Net-(JP6-Pad2)').connect(JP6['2'], SATA1['7'], SATA2['7'], SH2['2'])

    Net('Net-(LED1-Pad1)').connect(LED1['1'], RN5['4'])

    Net('Net-(LED2-Pad1)').connect(LED2['1'], RN5['3'])

    Net('Net-(LED3-Pad1)').connect(LED3['1'], RN5['2'])

    Net('Net-(LED4-Pad1)').connect(LED4['1'], RN5['1'])

    Net('Net-(R7-Pad2)').connect(R7['2'], RESET1['1'])

    Net('Net-(R8-Pad1)').connect(R8['1'], R9['2'], U8['1'])

    Net('Net-(RN12-Pad5)').connect(RN12['5'], RN3['1'], U4['R11'], U6['6'])

    Net('Net-(RN12-Pad6)').connect(RN12['6'], RN3['2'], U4['R12'], U6['1'])

    Net('Net-(RN12-Pad7)').connect(RN12['7'], U4['P12'], U6['5'])

    Net('Net-(RN12-Pad8)').connect(RN12['8'], U4['P11'], U6['2'])

    Net('Net-(RN2-Pad3)').connect(RN2['3'], SW2['1'])

    Net('Net-(RN2-Pad4)').connect(RN2['4'], SW1['1'])

    Net('Net-(RN6-Pad1)').connect(RN6['1'], SW3['4'])

    Net('Net-(RN6-Pad2)').connect(RN6['2'], SW3['3'])

    Net('Net-(RN6-Pad3)').connect(RN6['3'], SW3['2'])

    Net('Net-(RN6-Pad4)').connect(RN6['4'], SW3['1'])

    Net('Net-(U4-PadA10)').connect(U4['A10'])

    Net('Net-(U4-PadC7)').connect(U4['C7'])

    Net('Net-(U4-PadD10)').connect(U4['D10'])

    Net('Net-(U4-PadD11)').connect(U4['D11'])

    Net('Net-(U4-PadD12)').connect(U4['D12'])

    Net('Net-(U4-PadD13)').connect(U4['D13'])

    Net('Net-(U4-PadD3)').connect(U4['D3'])

    Net('Net-(U4-PadD4)').connect(U4['D4'])

    Net('Net-(U4-PadD5)').connect(U4['D5'])

    Net('Net-(U4-PadD6)').connect(U4['D6'])

    Net('Net-(U4-PadD7)').connect(U4['D7'])

    Net('Net-(U4-PadD8)').connect(U4['D8'])

    Net('Net-(U4-PadD9)').connect(U4['D9'])

    Net('Net-(U4-PadE10)').connect(U4['E10'])

    Net('Net-(U4-PadE11)').connect(U4['E11'])

    Net('Net-(U4-PadE4)').connect(U4['E4'])

    Net('Net-(U4-PadE5)').connect(U4['E5'])

    Net('Net-(U4-PadE6)').connect(U4['E6'])

    Net('Net-(U4-PadE9)').connect(U4['E9'])

    Net('Net-(U4-PadF11)').connect(U4['F11'])

    Net('Net-(U4-PadF12)').connect(U4['F12'])

    Net('Net-(U4-PadF4)').connect(U4['F4'])

    Net('Net-(U4-PadF5)').connect(U4['F5'])

    Net('Net-(U4-PadF7)').connect(U4['F7'])

    Net('Net-(U4-PadF9)').connect(U4['F9'])

    Net('Net-(U4-PadG10)').connect(U4['G10'])

    Net('Net-(U4-PadG11)').connect(U4['G11'])

    Net('Net-(U4-PadG12)').connect(U4['G12'])

    Net('Net-(U4-PadG3)').connect(U4['G3'])

    Net('Net-(U4-PadG4)').connect(U4['G4'])

    Net('Net-(U4-PadG5)').connect(U4['G5'])

    Net('Net-(U4-PadH11)').connect(U4['H11'])

    Net('Net-(U4-PadH12)').connect(U4['H12'])

    Net('Net-(U4-PadH3)').connect(U4['H3'])

    Net('Net-(U4-PadH4)').connect(U4['H4'])

    Net('Net-(U4-PadH5)').connect(U4['H5'])

    Net('Net-(U4-PadH6)').connect(U4['H6'])

    Net('Net-(U4-PadJ10)').connect(U4['J10'])

    Net('Net-(U4-PadJ11)').connect(U4['J11'])

    Net('Net-(U4-PadJ12)').connect(U4['J12'])

    Net('Net-(U4-PadJ3)').connect(U4['J3'])

    Net('Net-(U4-PadJ4)').connect(U4['J4'])

    Net('Net-(U4-PadJ5)').connect(U4['J5'])

    Net('Net-(U4-PadK11)').connect(U4['K11'])

    Net('Net-(U4-PadK12)').connect(U4['K12'])

    Net('Net-(U4-PadK3)').connect(U4['K3'])

    Net('Net-(U4-PadK5)').connect(U4['K5'])

    Net('Net-(U4-PadK9)').connect(U4['K9'])

    Net('Net-(U4-PadL10)').connect(U4['L10'])

    Net('Net-(U4-PadL11)').connect(U4['L11'])

    Net('Net-(U4-PadL12)').connect(U4['L12'])

    Net('Net-(U4-PadL3)').connect(U4['L3'])

    Net('Net-(U4-PadL5)').connect(U4['L5'])

    Net('Net-(U4-PadL6)').connect(U4['L6'])

    Net('Net-(U4-PadL7)').connect(U4['L7'])

    Net('Net-(U4-PadL9)').connect(U4['L9'])

    Net('Net-(U4-PadM11)').connect(U4['M11'])

    Net('Net-(U4-PadM12)').connect(U4['M12'])

    Net('Net-(U4-PadM2)').connect(U4['M2'])

    Net('Net-(U4-PadM3)').connect(U4['M3'])

    Net('Net-(U4-PadM5)').connect(U4['M5'])

    Net('Net-(U4-PadM6)').connect(U4['M6'])

    Net('Net-(U4-PadM7)').connect(U4['M7'])

    Net('Net-(U4-PadM8)').connect(U4['M8'])

    Net('Net-(U4-PadM9)').connect(U4['M9'])

    Net('Net-(U4-PadN10)').connect(U4['N10'])

    Net('Net-(U4-PadN12)').connect(U4['N12'])

    Net('Net-(U4-PadN14)').connect(U4['N14'])

    Net('Net-(U4-PadN2)').connect(U4['N2'])

    Net('Net-(U4-PadN3)').connect(U4['N3'])

    Net('Net-(U4-PadN5)').connect(U4['N5'])

    Net('Net-(U4-PadN6)').connect(U4['N6'])

    Net('Net-(U4-PadN7)').connect(U4['N7'])

    Net('Net-(U4-PadN9)').connect(U4['N9'])

    Net('Net-(U4-PadP10)').connect(U4['P10'])

    Net('Net-(U4-PadP13)').connect(U4['P13'])

    Net('Net-(U4-PadP2)').connect(U4['P2'])

    Net('Net-(U4-PadP4)').connect(U4['P4'])

    Net('Net-(U4-PadP5)').connect(U4['P5'])

    Net('Net-(U4-PadP6)').connect(U4['P6'])

    Net('Net-(U4-PadP7)').connect(U4['P7'])

    Net('Net-(U4-PadP8)').connect(U4['P8'])

    Net('Net-(U4-PadR2)').connect(U4['R2'])

    Net('Net-(U5-Pad40)').connect(U5['40'])

    Net('PM2-A1').connect(PM2['1'], U4['A1'])

    Net('PM2-A2').connect(PM2['2'], U4['B3'])

    Net('PM2-A3').connect(PM2['3'], U4['B5'])

    Net('PM2-A4').connect(PM2['4'], U4['B6'])

    Net('PM2-B1').connect(GR4['1'], PM2['7'], U4['A2'])

    Net('PM2-B2').connect(GR4['2'], PM2['8'], U4['B4'])

    Net('PM2-B3').connect(PM2['9'], U4['A5'])

    Net('PM2-B4').connect(PM2['10'], U4['A6'])

    Net('PM3-A1').connect(PM3['1'], U4['A11'])

    Net('PM3-A2').connect(PM3['2'], U4['B12'])

    Net('PM3-A3').connect(PM3['3'], U4['B14'])

    Net('PM3-A4').connect(PM3['4'], U4['B15'])

    Net('PM3-B1').connect(GR5['1'], PM3['7'], U4['B10'])

    Net('PM3-B2').connect(GR5['2'], PM3['8'], U4['B11'])

    Net('PM3-B3').connect(PM3['9'], U4['B13'])

    Net('PM3-B4').connect(PM3['10'], U4['A15'])

    Net('SATA1_A+').connect(RN7['8'], U4['L4'])

    Net('SATA1_A-').connect(RN7['7'], U4['L1'])

    Net('SATA1_B+').connect(RN7['5'], U4['K4'])

    Net('SATA1_B-').connect(RN7['6'], U4['M1'])

    Net('SATA2_A+').connect(RN8['8'], U4['M4'])

    Net('SATA2_A-').connect(RN8['7'], U4['P1'])

    Net('SATA2_B+').connect(RN8['5'], U4['R1'])

    Net('SATA2_B-').connect(RN8['6'], U4['N4'])

    Net('SD_A0').connect(U4['F13'], U5['23'])

    Net('SD_A1').connect(U4['E14'], U5['24'])

    Net('SD_A10').connect(U4['F14'], U5['22'])

    Net('SD_A11').connect(U4['F16'], U5['35'])

    Net('SD_A12').connect(U4['G14'], U5['36'])

    Net('SD_A2').connect(U4['E13'], U5['25'])

    Net('SD_A3').connect(U4['D14'], U5['26'])

    Net('SD_A4').connect(U4['B16'], U5['29'])

    Net('SD_A5').connect(U4['C16'], U5['30'])

    Net('SD_A6').connect(U4['D15'], U5['31'])

    Net('SD_A7').connect(U4['D16'], U5['32'])

    Net('SD_A8').connect(U4['E16'], U5['33'])

    Net('SD_A9').connect(U4['F15'], U5['34'])

    Net('SD_BS0').connect(U4['H14'], U5['20'])

    Net('SD_BS1').connect(U4['G13'], U5['21'])

    Net('SD_CKE').connect(U4['G15'], U5['37'])

    Net('SD_CLK').connect(U4['G16'], U4['H16'], U5['38'])

    Net('SD_DQ0').connect(U4['R14'], U5['2'])

    Net('SD_DQ1').connect(U4['P14'], U5['4'])

    Net('SD_DQ10').connect(U4['M16'], U5['45'])

    Net('SD_DQ11').connect(U4['M15'], U5['47'])

    Net('SD_DQ12').connect(U4['N16'], U5['48'])

    Net('SD_DQ13').connect(U4['P16'], U5['50'])

    Net('SD_DQ14').connect(U4['P15'], U5['51'])

    Net('SD_DQ15').connect(U4['R15'], U5['53'])

    Net('SD_DQ2').connect(U4['M13'], U5['5'])

    Net('SD_DQ3').connect(U4['M14'], U5['7'])

    Net('SD_DQ4').connect(U4['L13'], U5['8'])

    Net('SD_DQ5').connect(U4['L14'], U5['10'])

    Net('SD_DQ6').connect(U4['K13'], U5['11'])

    Net('SD_DQ7').connect(U4['K14'], U5['13'])

    Net('SD_DQ8').connect(U4['J16'], U5['42'])

    Net('SD_DQ9').connect(U4['L16'], U5['44'])

    Net('SD_LDQM').connect(U4['J13'], U5['15'])

    Net('SD_UDQM').connect(U4['J15'], U5['39'])

    Net('SW1').connect(SW1['2'], U4['A16'])

    Net('SW2').connect(SW2['2'], U4['B9'])

    Net('USER_CLK').connect(U4['C8'], U7['3'])

    Net('VCCIO_3').connect(C19['1'], C23['1'], C27['1'], C31['1'], C6['1'], HDR1['5'], JP6['1'], R9['1'], U4['E1'], U4['G6'], U4['J6'], U4['N1'], U8['2'], U8['4'])

    Net('~SD_CAS').connect(U4['K15'], U5['17'])

    Net('~SD_CS').connect(U4['H13'], U5['19'])

    Net('~SD_RAS').connect(U4['K16'], U5['18'])

    Net('~SD_WE').connect(U4['J14'], U5['16'])


#===============================================================================
# Instantiate the circuit and generate the netlist.
#===============================================================================

if __name__ == "__main__":
    C__xesscorp_PRODUCTS_CAT_pcb_cat_flat_py()
    generate_netlist()
