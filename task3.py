path = input();
sumArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
for i in range(5):
	f = open(path + 'Cash' + str(i + 1) + '.txt');
	j = 0;
	for line in f:
		sumArr[j] += float(line);
		j = j + 1;
mx = max(sumArr);
i = 1;
for x in sumArr:
	if (x == mx):
		print (i)
		break;
	i = i + 1;