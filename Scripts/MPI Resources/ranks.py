# A simple program to return the current rank, size of cluster, and hostname of all nodes in cluster
# Made by Noah Harris for HPCC

from mpi4py import MPI
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = socket.gethostname()

print("Process", rank, "of", size, "is running on", hostname)
