import numpy as np
import matplotlib.pyplot as plt

ftemp = [63, 73, 80, 95, 23, 63, 69, 29, 40, 10, 72] #리스트
F=np.array(ftemp)                                    #넘파이 배열로 저장
(F-32)*5/9
#plt.plot(F) #numpy 배열 이용
plt.plot(ftemp) #list 이용
plt.show()
