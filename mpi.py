#brooke walters
#cis 677
# project four 
# due 4/16/2024


# import libraries
# from mpi4py import MPI
import time
import numpy as np


def random_matrices(n):
  a = np.random.randint(1, 200, size=(n, n))
  b = np.random.randint(1, 200, size=(n, n))
  c = np.zeros((n, n))
  return a,b,c


def multiple_matrices(a,b,c):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]

if __name__ == "__main__":
  n_vals =  [3,4,5,6,7]
  for n in n_vals:
    #create randomly generated matrices, with c clearing out to 0
    a,b,c = random_matrices(n)
    a_numpy = np.array(a)
    b_numpy = np.array(b)
    c_numpy = np.array(c)

    # find the execution time
    start_time = time.time()
    # matrix multiplication with numpy  function
    multiple_matrices(a_numpy,b_numpy, c_numpy)
    end_time = time.time()
    elapsed_time = end_time - start_time
