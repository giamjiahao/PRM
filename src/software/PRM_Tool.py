import os

GATE_PREFIX="\033[1;31;40m[GATE-M]-->\033[0;37;40m"
FATAL_PREFIX=""
WARNING_PREFIX=""
DEBUG=""
SOFT=""

def PRM_MSG_INFO(content):
    print(GATE_PREFIX,end='')
    print(content)

def PRM_MSG_DEBUG(content):
    if(DEBUG == "True"):
        print(GATE_PREFIX+"[Debug] ",end='')
        print(content)
    else:
        return

def PRM_MSG_WARNING(content):
    print(GATE_PREFIX,end='')
    #   Add Warning style
    print("Warning: ",end='')

def PRM_MSG_FATAL(content):
    print(GATE_PREFIX,end='')
    #   Add Fatal style
    return -1

def PRM_From_Device(content):
    print(GATE_PREFIX,end='')
    print("Device: "+content)

def PRM_HEADER():
    print("\t\t------------------\n")
    print("\t\tProject GATE Type-M\n")
    print("\t\t------------------\n")
    PRM_MSG_INFO("System engaged.")

def PRM_User_Input():
    print(GATE_PREFIX,end='')
    userInput=input()
    return str.encode(userInput+"\n")

def PRM_Task_List():
    print(GATE_PREFIX,end='')

def RPM_Config_Arudino():
    if(SOFT == "False"):
        # Verify and upload Arduino sketches
        PRM_MSG_INFO("Uploading sketches to arduino")
        UPLOAD_EXIT_CODE=os.system("/Applications/Arduino.app/Contents/MacOS/Arduino --upload /Users/giamjiahao/Documents/PRM-master/src/hardware/arduino/prm-arduino-main/prm-arduino-main.ino")
        if UPLOAD_EXIT_CODE != 0:
            PRM_MSG_INFO("Arduino uploading failed!")
            exit()
        PRM_MSG_INFO("Configuration done.")
    else:
        PRM_MSG_INFO("Software only mode. Arduino is not use!")
