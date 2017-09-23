import socket, sys

if len(sys.argv) != 3:
	print("USAGE: " + sys.argv[0] + " dstHost dstPort", file=sys.stderr)
	exit(1);

dstAddrInfo = socket.getaddrinfo(sys.argv[1], sys.argv[2])
dstAddrInfo = dstAddrInfo[0]
sfd = socket.socket(dstAddrInfo[0], socket.SOCK_DGRAM)

sfd.sendto("Ala ma kota".encode(), dstAddrInfo[4])
