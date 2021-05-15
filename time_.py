import time

def time_this(func):
    def time_wrap(param):
    	avg_time = 0
    	for i in range(100000):
    		t0 = time.time()
    		func(param)
    		t1 = time.time()
    		avg_time += (t1-t0)
    	avg_time /= 100000	
    	print("Выполнение заняло %.5f секунд" % avg_time)
    	      
    return time_wrap


@time_this
def Fibb(N):
	list_ = [1,2]
	sum_=2
	for n in range(2,N):
		list_.append(list_[n-1]+list_[n-2])
		if list_[n]%2==0:
				sum_ += list_[n]
		elif list_[n] >= 400000000:
			break
			
	return list_[n-1]
Fibb(1000)
