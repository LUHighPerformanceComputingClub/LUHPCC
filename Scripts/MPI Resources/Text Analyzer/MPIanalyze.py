# An MPI enabled analyzer to find a given keyword in a text
# Made by Noah Harris for HPCC

import time
import socket
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank() # process number
size = comm.Get_size()-1 # how many processes exist, minus head
name = socket.gethostname()

keyword = "bee"

if rank == 0: # if we're process 0, split the script into multiple parts and send to slaves for processing

	start = time.time()

	file = open("script.txt", "r")
	#file = open("bible.txt", "r")

	script = file.read().split() # get entire script to parse

	process = 0
	send = [[] for i in range(size)]

	for i in script:
		send[process].append(i)
		process += 1

		if process == size:
			process = 0

	for i in range (size):
		comm.send(send[i], dest=i+1)

	print("Process", rank, "on", name, "has sent out their scripts!")
	found = 0

	for i in range(size):
		found += comm.recv(source=i+1)

	print("Process", rank, "on", name, "has finished compiling the results!")

	end = time.time()

	print("We found", found, "many", keyword + "\'s in this script!")
	print("This script took", end-start, "many seconds to run.")

else:
	script = comm.recv(source=0)
	print("Process", rank, "on", name, "got their script!")
	found = 0

	for i in script:
		if keyword in i:
			found += 1

	print("Process", rank, "on", name, "has finished their analyzation and found", found, keyword + "\'s!")
	comm.send(found, dest=0)
