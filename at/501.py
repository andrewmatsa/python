def recognize(ip,*ips,**named_ips):
	free = []
	is_ip = lambda x: len(x) == 15
	if is_ip(ip):
		free.append(ip)
	if ips:
		[free.append(item) for item in ips if is_ip(item)]
		return free, free[0]
	else:
		return free

print recognize("192.168.100.100", "192.168.100.101", "192.168.100.102", "192.168.100.103", "192.168.100.104")