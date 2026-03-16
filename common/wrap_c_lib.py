import ctypes
import numpy as np

def load_c_lib(lib_path):
    lib = ctypes.cdll.LoadLibrary(lib_path)

    def prediction(x):
        X = np.array(x, dtype=np.float32)
        X = np.ascontiguousarray(X)
        rows, cols = X.shape
        out = np.zeros(rows, dtype=np.float32)
        lib.predict.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
        lib.predict(X.ctypes.data_as(ctypes.POINTER(ctypes.c_float)), rows, out.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))
        return out

    return prediction