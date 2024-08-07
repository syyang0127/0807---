import matplotlib.pyplot as plt

X = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
Y1 = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
Y2 = [15.6, 24.3, 11.5, 14.2, 13.1, 23.2, 12.4]
#plt.plot([15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4])

plt.plot(X, Y1, label="Seoul")
plt.plot(X, Y2, label="Busan")

plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(loc="upper left")
plt.title("Temperature of Cities")

plt.show()
