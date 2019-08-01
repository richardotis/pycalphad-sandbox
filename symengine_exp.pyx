from ctypes import c_double, c_void_p, c_int, cast, POINTER, CFUNCTYPE
import numpy as np


cdef void _my_callback(double *out, double *x, void *user_data) nogil:
    out[0] = 1.0

cdef double[::1] inp = np.array([300, 0.25, 0.25, 0.25, 0.25])
cdef double[::1] out = np.zeros((2,), order='C')


cdef void *addr1 = cast(<void*>_my_callback, c_void_p)
#cdef void *addr = <void*>&_my_callback
ctypedef void func_t(double *out, double *dof, void *user_data) nogil
cdef func_t* raw_function = <func_t*>addr1
raw_function(&out[0], &inp[0], <void*>NULL)
print(np.array(out))
