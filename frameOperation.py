import serial               # 串口类
import sys, ctypes          
from time import sleep      # 延时类
import one
import re                   # 正则表达式


def dataADD33(dataStr: str):
    '''
    数据域加33
    '''
    str33 = bytes().fromhex(dataStr)
    result = []
    for i in str33:
        i += 51
        if i > 255:
            i &= 0xFF
        result.append(i)
    return result

def dataSUB33(dataStr: str):
    '''
    数据域减33
    '''
    str33 = bytes().fromhex(dataStr)
    result = []
    for i in str33:
        i -= 51
        if i < 0:
            i &= 0xFF
        result.append(i)
    return result

def frameBytes2HexStr(dataBytes: list) -> str:
    '''
    byte 数组转化为 hex string
    '''
    hexStr = ''
    while len(dataBytes) > 0:
        tmp = hex(dataBytes.pop()).upper()[2:]
        hexStr += tmp
    return hexStr

def splitHexStr(hexStr: str, splitNum: int, splitSymbol: 'default' = ' ') -> str:
    '''
    为16进制报文添加分隔符，默认添加空格来分割
    '''
    reguler = '.{' + str(splitNum) + '}'
    pattern = re.compile(reguler)
    return (splitSymbol.join(pattern.findall(hexStr)))


if __name__ == '__main__':
    sendStr = '4D 43 33 30 24 8C 33 33 32 33 33 33 E5 49 33 33 D9 32 32 32'
    result = dataSUB33(sendStr)
    print(result)
    # sendStr = '68 31 10 00 00 00 00 68 20 04 '
    # diStr = 'FD 00 10 1A'

    # diList = dataADD33(diStr)
    hexStr = frameBytes2HexStr(result)
    while True:
        sleep(3)
        print(splitHexStr(hexStr, 3, ' '))
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



