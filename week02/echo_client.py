#!/usr/bin/env python
import socket
from pathlib import *

HOST = 'localhost'
PORT = 10000

def echo_client():

    ''' Echo Server 的 Client 端 '''
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 接收用户输入文件名并发送服务端
        data = input('input > ')

        # 设定退出条件
        if data == 'exit':
            break	
        p = Path(data)
        if p.exists() and p.is_file():
            with open(p,'rb') as f:
                s.sendall(f.read())
        else:
            print(f'file is not exists')
    s.close()


if __name__ == '__main__':
    echo_client()
