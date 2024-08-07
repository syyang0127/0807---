import numpy as np

# numpy 쓰는 이유 : 간편하고 처리가 빠름

heights = [1.83, 1.76, 1.79, 1.86, 1.90]
weights = [70, 50, 90, 88, 100]

np_heights = np.array(heights)
np_weights = np.array(weights)


bmi = np_weights/(np_heights**2)

print(bmi)