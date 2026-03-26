import ctypes
import numpy as np

def load_c_lib(lib_path):
    lib = ctypes.cdll.LoadLibrary(lib_path)
    lib.predict.argtypes = [
        ctypes.POINTER(ctypes.c_float),
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_float)
    ]
    lib.predict.restype = None  # explicitly declare void return

    def prediction(x):
        X = np.array(x, dtype=np.float32, order='C')
        X = np.ascontiguousarray(X)
        
        # Handle both 1D (single sample) and 2D inputs
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        rows, cols = X.shape
        out = np.zeros(rows, dtype=np.float32)

        for i in range(rows):
            row = np.ascontiguousarray(X[i])  # ensure each row is contiguous
            lib.predict(
                row.ctypes.data_as(ctypes.POINTER(ctypes.c_float)),
                ctypes.c_int(1),
                out[i : i + 1].ctypes.data_as(ctypes.POINTER(ctypes.c_float))
            )

        return out

    return prediction