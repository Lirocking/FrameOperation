# import serial               # 串口类
import sys, ctypes          
from time import sleep      # 延时类
import re                   # 正则表达式
import dataTransfer

if __name__ == '__main__':
    sendStr = '4D 43 33 30 24 8C 33 33 32 33 33 33 E5 49 33 33 D9 32 32 32'
    result = dataTransfer.dataSUB33(sendStr)
    print(result)
    # sendStr = '68 31 10 00 00 00 00 68 20 04 '
    # diStr = 'FD 00 10 1A'

    # diList = dataADD33(diStr)
    hexStr = dataTransfer.frameBytes2HexStr(result)
    print(dataTransfer.splitHexStr(hexStr, 2, ' '))
    print(dataTransfer.reverseFrameStr(hexStr))
    # sendStr = sendStr.replace(' ', '')
    # cs = hex(one.uchar_checksum(bytes().fromhex(sendStr))).upper()[2:]
    # sendStr += cs.zfill(2) + '16'
    # sendStr = "FEFEFEFE" + sendStr
    # print(sendStr)

    #ser = serial.Serial('com5', 2400, timeout=6, inter_byte_timeout=4)
    #if not ser.is_open:
    #    ser.open()
    #sendBytes = bytes().fromhex(sendStr)
    #ser.write(sendBytes)

    #data = ''
    #sleep(2)
    #while True:
    #    data = ser.read_all()
    #    if data == '':
    #        continue
    #    else:
    #        break
    #    sleep(1)

    #print(data.hex().upper())



