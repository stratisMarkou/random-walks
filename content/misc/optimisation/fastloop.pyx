#cython: boundscheck=False, wraparound=False, nonecheck=False
from libc.math cimport exp
import numpy as np

def matmul(double[:, ::1] A, double[::1] x):

    cdef int I = A.shape[0]
    cdef int J = A.shape[1]
    cdef double[:] y = np.zeros(I)
    cdef double tmp = 0

    for i in range(I):
        tmp = 0
        for j in range(J):
            tmp += A[i, j] * x[j]
        y[i] = tmp

    return y


def conjugate_gradients(double[:, :] A, double[:] b, double[:] x0):
    
    cdef double[:] x = x0
    cdef int N = A.shape[0]
            
    cdef double[:] g = np.dot(A, x) - b
    cdef double[:] d = np.multiply(-1, g)
    cdef double[:] alpha = np.array([0.]) 
    cdef double[:] beta = np.array([0.]) 
    
    for i in range(N):
        
        alpha[0] = - np.dot(d, g) / np.dot(d, np.dot(A, d))
        
        x = np.add(x, np.multiply(alpha, d))
        
        g = np.add(g, np.multiply(alpha, np.dot(A, d)))

        beta[0] = np.dot(g, np.dot(A, d)) / np.dot(d, np.dot(A, d))
        d = np.multiply(-1., np.add(g, np.multiply(beta, d)))
        
    return x