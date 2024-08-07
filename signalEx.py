import numpy as np
import matplotlib.pyplot as plt

pure = np.linspace(1,10,100) 
noise = np.random.normal(0,1,100)
signal = pure + noise


plt.plot(pure)     #(0,1)부터 (10,100)까지 직선인 그래프 
plt.plot(noise)    #
plt.plot(signal) 

plt.show()
