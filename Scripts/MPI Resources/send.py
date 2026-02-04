# A simple program to show how sending and receiving data works for an MPI cluster
# Made by Noah Harris for HPCC

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank % 2 == 0: # even rank
	data = rank
	print("Process", rank, "has sent their data!")
	comm.send(data, dest=rank+1) # so 1 will get 0's data, 3 will get 2's, etc...
elif rank % 2 == 1: # odd rank
	data = comm.recv(source=rank-1)
	print("On process", rank, "data has been received from", rank-1)
