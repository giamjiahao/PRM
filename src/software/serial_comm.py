# Author: Zhaoyuan "Maxwell" Cui
# Physics department, University of Arizona
# This is the python script of serial communication


import serial
import PRM_Tool as gate
import argparse

parser=argparse.ArgumentParser(prog='PRM Script', description='Project gate Type-M Script')
parser.add_argument('-d', '--debug', dest='debug_choice', default='True', nargs=1, choices=['True','False'], help='Enable debug mode')
parser.add_argument('-s', '--software-only', dest='software_choice', default='False', nargs=1, choices=['True','False'],help='Software only mode, do not configure hardware')
args=parser.parse_args()

gate.DEBUG   =   args.debug_choice
gate.SOFT    =   args.software_choice

# Print PRM header
gate.PRM_HEADER()

gate.RPM_Config_Arudino()

# Open serial port in the python script
gate.PRM_MSG_INFO("Opening serial port...")

ser=serial.Serial('/dev/tty.usbmodem14201',9600,timeout=5)
ser.flush()
ser.flushInput()
gate.PRM_MSG_INFO("listening...")

# Wait for ready string from Arduino
msg=ser.read_until(b'Device Ready...')
gate.PRM_MSG_DEBUG(msg)

if(msg!=b'Device Ready...'):
    gate.PRM_MSG_INFO("Does't hear device status. Aborting...")
    exit()
gate.PRM_MSG_INFO("Connection established!")

while True:
    inputCommand=gate.PRM_User_Input()
    #if(inputCommand == "quit\n"):
    #    gate.PRM_MSG_INFO("Project gate System quitting.")
    #    break
    ser.write(inputCommand)
    msg=ser.read_until()
    if(msg.decode("UTF-8") != ""):
        gate.PRM_From_Device(msg.decode("UTF-8"))
    else:
        gate.PRM_MSG_INFO("Device return is empty!")
        break
