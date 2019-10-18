import statistics
def average(numbers):
	 return float(sum(numbers))/(len(numbers))
f=open('C:\\Users\\Kate\\Desktop\\test1.txt');
arr=[]
for line in f: 
	arr.append(float(line))
print  (percentile(arr))
print (format(statistics.median(arr),'.2f') +
 '\n' + format(max(arr),'.2f') +
 '\n'+format(min(arr),'.2f') +
 '\n'+format(average(arr),'.2f'))