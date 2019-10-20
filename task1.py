import statistics
url = input();
def average(numbers):
	 return float(sum(numbers))/(len(numbers))
f=open(url);
arr=[]
for line in f: 
	arr.append(float(line))
print ('percentile\n' + format(statistics.median(arr),'.2f') +
 '\n' + format(max(arr),'.2f') +
 '\n'+format(min(arr),'.2f') +
 '\n'+format(average(arr),'.2f'))