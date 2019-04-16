import re                   # 正则表达式
import sys, ctypes          


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

def calCheckNum(hexStr: str) -> str:
    '''
    输入16进制字符串，返回校验和
    '''
    return hexStr
def reverseFrameStr(frameStr: str, partitionNum: 'default' = 2) -> str:
    '''
    输入帧字符串，按需进行字符倒置，默认每两个一倒置
    '''

    return frameStr[::-1]