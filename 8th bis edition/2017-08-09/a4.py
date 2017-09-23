import multiprocessing, os, time

def fun(l):
	print("podproces")
	l.acquire()
	print("Lock OK - podproces")
	time.sleep(10)
	l.release()
	print("zwolniłem - podproces")
	time.sleep(10)

if __name__ == '__main__':
	q = multiprocessing.Lock()
	p = multiprocessing.Process(target=fun, args=(q,))
	p.start()
	print("główny")
	time.sleep(1)
	q.acquire()
	print("Lock OK - główny")
	q.release()
	time.sleep(30)

