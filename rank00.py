import multicast_expert
import socket

interfaces=multicast_expert.get_interface_ips(include_ipv4=True, include_ipv6=False)
#interfaceip=multicast_expert.get_default_gateway_iface_ip_v4()
interfaceip=interfaces[-1]
print(interfaceip)

with multicast_expert.McastTxSocket(socket.AF_INET, mcast_ips=['239.1.2.3'], iface_ip=interfaceip) as mcast_tx_sock:
    mcast_tx_sock.sendto(b'Hello World', ('239.1.2.3', 12345))
