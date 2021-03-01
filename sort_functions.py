def bubbleSort(inp):
	for i in range(len(inp)):
		for j in range(i+1,len(inp)):
			if inp[i] > inp[j]:
				inp[i],inp[j] = inp[j],inp[i]
	return inp


def Merge(inp1,inp2):
	ind = 0
	ind1 = 0
	ind2 = 0
	merged_l = []
	while ind1 < len(inp1) or ind2 < len(inp2) :
		if ind2 == len(inp2) or (ind1 < len(inp1) and inp1[ind1] < inp2[ind2] ) :
			merged_l.append(inp1[ind1])
			ind1 += 1
		else:
			merged_l.append(inp2[ind2])
			ind2 += 1
	return merged_l



def mergeSort(inp):
	if len(inp) == 1:
		return inp
	lst1 = mergeSort(inp[:(len(inp)//2)])
	lst2 = mergeSort(inp[(len(inp)//2):])
	return Merge(lst1,lst2)

def insertSort(inp):
	for i in range(1,len(inp)):
		currentvalue = inp[i]
		pos = i
		while pos>0 and inp[pos-1]>currentvalue:
			inp[pos] = inp[pos-1]
			pos = pos - 1
		inp[pos] = currentvalue
	return inp