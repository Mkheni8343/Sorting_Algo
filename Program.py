from sort_functions import *
import matplotlib.pyplot as plt
import time
import random

def plot_sort(num,gape):
	plt.title("Sorting Algorithms Comparision")
	plt.xlabel("Length of list")
	plt.ylabel("Time in MiliSeconds")
	bub = []
	mg = []
	tim = []
	lst = []
	xV = []
	ins1 = []
	for i in range(num):
		lst.append(random.randint(1,num*10))
	for i in range(1,num,gape):
		
		st = time.clock()
		bub_l = bubbleSort(lst[:i])
		en = time.clock()
		bub.append((en-st)*1000)

		st = time.clock()
		bub_l = mergeSort(lst[:i])
		en = time.clock()
		mg.append((en-st)*1000)

		new_l = lst[:i].copy()
		st = time.clock()
		new_l.sort()
		en = time.clock()
		tim.append((en-st)*1000)

		st = time.clock()
		insort = insertSort(lst[:i])
		en = time.clock()
		ins1.append((en-st)*1000)


		xV.append(i)
		print("Processing ..",str((i/num)*100),"%")


	line1, = plt.plot(xV,bub)
	line2,= plt.plot(xV,mg,marker='o')
	line3, = plt.plot(xV,tim,marker='*')
	line4, = plt.plot(xV,ins1,marker='+')

	fg = plt.legend([line1,line2,line3,line4],["Bubble Sort","Merge Sort","Tim Sort","Insertion Sort"])
	plt.savefig("Sorting_Comparisions_"+str(num)+".png")
	plt.show()
	plt.cla()

plot_sort(100,10)