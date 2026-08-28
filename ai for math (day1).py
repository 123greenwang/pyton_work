import numpy as np

# 你已经会Python了，直接学NumPy的"数学语法"
A = np.array([[1, 2], [3, 4], [5, 6]])
v = np.array([1, 2])

# 矩阵乘法（不是元素乘法！）
print(A @ v)        # 结果: [5, 11, 17]

# 转置、形状
print(A.shape)      # (3, 2)
print(A.T)          # 2x3 矩阵
