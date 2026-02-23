# A bogo-sort algorithm with multi-core non-blocking performance
# Made by Noah Harris for HPCC

import random
import time
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

TAG_DATA = 1
TAG_RESULT = 2
TAG_STOP = 3

ARR_SIZE = 8

#Functions to do the sorting
def is_sorted(arr):
    #Checks if the array is in the right order
    for num in range(len(arr)-1):
        if arr[num]>arr[num+1]:
            #Return false if the item to the left is bigger than the item to the right
            return False
    return True

def bogoSortNode(arr): # will attempt to sort the array until success, then return attempts
    arr = arr.copy()
    attempts = 0

    while True:
        # Check if another worker already finished
        if comm.iprobe(source=0, tag=TAG_STOP):
            comm.recv(source=0, tag=TAG_STOP)
            print(f"[WORKER {rank}] Received stop signal. Exiting early.")
            return None, attempts

        if is_sorted(arr):
            return arr, attempts

        np.random.shuffle(arr)
        attempts += 1

if (rank == 0): #head node code
    startTime= time.time()

    # Create small random array
    data = np.random.permutation(ARR_SIZE).astype('i')
    print("Here is the list pre-sort:", data)

    # Non-blocking sends to all workers
    send_reqs = []
    for worker in range(1, size):
        req = comm.Isend(data, dest=worker, tag=TAG_DATA)
        send_reqs.append(req)

    # Prepare non-blocking receives from all workers
    recv_buffers = {}
    recv_reqs = []

    for worker in range(1, size):
        buf = np.empty_like(data)
        recv_buffers[worker] = buf
        req = comm.Irecv(buf, source=worker, tag=TAG_RESULT)
        recv_reqs.append((worker, req))

    sorted_result = None
    winner = None

    # Poll for completion
    while sorted_result is None:
        for worker, req in recv_reqs:
            if req.Test():
                sorted_result = recv_buffers[worker]
                winner = worker
                break
        time.sleep(0.01)  # prevent busy spin

    print(f"[HEAD] Sorted result received from worker {winner}: {sorted_result}")
    print(f"Completed in: {int(time.time()-startTime)} seconds!")

    # Tell all workers to stop
    for worker in range(1, size):
        comm.isend(False, dest=worker, tag=TAG_STOP)

else: # slave code
    # Receive data non-blocking
    data = np.empty(ARR_SIZE, dtype='i')
    recv_req = comm.Irecv(data, source=0, tag=TAG_DATA)

    # Wait for data arrival
    while not recv_req.Test():
        time.sleep(0.01)

    print(f"[WORKER {rank}] Received array {data}")

    # Perform bogosort
    sorted_arr, attempts = bogoSortNode(data)

    if sorted_arr is not None:
        print(f"[WORKER {rank}] Sorted after {attempts} shuffles")
        comm.Isend(sorted_arr, dest=0, tag=TAG_RESULT)

        
print(f"[RANK {rank}] Exiting.")