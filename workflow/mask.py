#!/usr/bin/env python

import sys
import alp
import re

#mask an ip address
pattern = re.compile(r'^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])/(3[0-2]|[1-2]?\d)$')
match = pattern.match(sys.argv[1])
if not match:
    error_dic = dict(title="Cannot match.", subtitle="maskip xxx.xxx.xxx.xxx/xx", uid="error", valid=False, arg="error")
    error = alp.Item(**error_dic)
    alp.feedback(error)
else:
    result = match.groups()
    binary = bin(int(result[0]))[2:].zfill(8) + bin(int(result[1]))[2:].zfill(8) + bin(int(result[2]))[2:].zfill(8) + bin(int(result[3]))[2:].zfill(8)
    subnet_b = binary[0: int(result[4])]
    padding = subnet_b.ljust(32, '0')
    mask_b = int(result[4]) * '1' + (32 - int(result[4])) * '0'
    mask_ip = str(int(mask_b[0: 8], 2)) + '.' + str(int(mask_b[8: 16], 2)) + '.' + str(int(mask_b[16: 24], 2)) + '.' + str(int(mask_b[24: 32], 2))
    subnet_ip = str(int(padding[0: 8], 2)) + '.' + str(int(padding[8: 16], 2)) + '.' + str(int(padding[16: 24], 2)) + '.' + str(int(padding[24: 32], 2))
    host_b = binary[int(result[4]):]
    host_id = int(host_b.zfill(32), 2)

    mask_ip_dic = dict(title=str(mask_ip), subtitle="Subnet Mask", uid="maskip", valid=True, arg=str(mask_ip), icon="icon.png")
    subnet_ip_dic = dict(title=str(subnet_ip), subtitle="Subnet IP Address", uid="subnetip", valid=True, arg=str(subnet_ip), icon="icons/ip.png")
    host_id_dic = dict(title=str(host_id), subtitle="Host ID", uid="hostid", valid=True, arg=str(host_id), icon="icons/host.png")
    ip_b_dic = dict(title=str(binary), subtitle="Binary IP Address", uid="ipb", valid=True, arg=str(binary), icon="icons/ip.png")
    subnet_b_dic = dict(title=str(subnet_b), subtitle="Binary Subnet IP Address", uid="subnetb", valid=True, arg=str(subnet_b), icon="icons/ip.png")
    host_b_dic = dict(title=str(host_b), subtitle="Binary Host ID", uid="hostb", valid=True, arg=str(host_b), icon="icons/host.png")

    m = alp.Item(**mask_ip_dic)
    s = alp.Item(**subnet_ip_dic)
    h = alp.Item(**host_id_dic)
    ip = alp.Item(**ip_b_dic)
    sb = alp.Item(**subnet_b_dic)
    hb = alp.Item(**host_b_dic)

    item_list = [m, s, h, ip, sb, hb]
    alp.feedback(item_list)
