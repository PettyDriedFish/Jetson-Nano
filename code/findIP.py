from scapy.all import ARP, Ether, srp

def get_ip_from_mac(mac_address):
    # 创建一个ARP请求数据包，目标MAC地址设置为广播地址
    arp = ARP(pdst='192.168.1.1/24', hwdst='ff:ff:ff:ff:ff:ff')
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether/arp

    # 发送ARP请求，并等待响应
    result = srp(packet, timeout=3, verbose=False)[0]

    # 遍历响应数据包，查找匹配的MAC地址
    for sent, received in result:
        if received:
            # 提取IP地址
            ip_address = received.psrc
            return ip_address

    return None

# 目标设备的MAC地址
mac_address = 'AC:15:A2:3F:C2:4A'

# 获取对应的IP地址
ip_address = get_ip_from_mac(mac_address)
print(f"IP Address: {ip_address}")
