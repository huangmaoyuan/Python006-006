#!/usr/bin/env python
import socket
from pathlib import *

HOST = 'localhost'
PORT = 10000


def echo_server():

    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)
    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        file_name = "test.txt"
        p = Path(__file__)
        recv_file = p.resolve().parent.joinpath(file_name)
        with open(recv_file,'wb+') as f:
            while True:
                data = conn.recv(1024)
                if not data:                    
                    break
                f.write(data)
        conn.close()
    s.close()


if __name__ == '__main__':
    echo_server()
