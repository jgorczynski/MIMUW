import os, sys, time, signal

print("====", os.getpid())

p = os.fork()
a=1

if p==0:
	a=2*a
	print("AAAA", os.getpid())
	time.sleep(2)
	print("AAAA", os.getpid(), a)
	time.sleep(20)
else:
	print("BBBB", os.getpid(), p)
	time.sleep(10)
	os.kill(p, signal.SIGTERM)
	print("BBBB", os.getpid(), p, a)
	time.sleep(10)

