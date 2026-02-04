# A random number adder to show how multiple cores can communicate and aggregate results at the head node
# Made by Noah Harris for HPCC

from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

myNumber = int(random.random() * 100)

print("Process", rank, "has the random number", myNumber)

if rank != 0:
	comm.send(myNumber, dest=0) # send our number to the 0th process
else:
	sum = 0

	for i in range(1, size):
		sum += comm.recv(source=i)

	print("Process", rank, "has summed all numbers from the other processes, totaling to", sum)
