#by wxyinasilent
#2022/11/19
#github/wxyinasilent555

import serial
from time import sleep

def get_bmp_data():
    filepath = 'cxk.txt'
    f = open(filepath)
    bmp_data = []
    for line in f:
        val = line.strip().split(',')
        if len(val) == 0:
            continue
        bmp_data.append([int(x) for x in val])
    f.close()
    return bmp_data

def main():
    com = serial.Serial('com13', 460800, timeout=10) #设置端口号、波特率、超时时间
    print(com)
    print(com.isOpen())

    bmp_data = get_bmp_data()
    print(len(bmp_data))
    for frame in bmp_data[0:]:
        ret = com.write(bytes(frame))
        sleep(0.03)

if __name__ == '__main__':
    main()
