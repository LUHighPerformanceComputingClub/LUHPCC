# A test program made to show how nodes can communicate up to their size count
# Made by Noah Harris for HPCC

from mpi4py import MPI

comm=MPI.COMM_WORLD

rank=comm.rank
size=comm.size

i=1
for j in range(5):
	data=j*j
	comm.send(data,dest=(rank+1)%size)
	data1=comm.recv(source=(rank-1)%size)
	print (data1)
	
