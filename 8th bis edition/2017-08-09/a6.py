import socket, sys

if len(sys.argv) != 2:
	print("USAGE: " + sys.argv[0] + " listenPort", file=sys.stderr)
	exit(1);

sfd = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sfd.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
sfd.bind(('::', int(sys.argv[1])))

while True:
	data, sAddr, = sfd.recvfrom(4096)
	print("odebrano od", sAddr, ":", data.decode());
