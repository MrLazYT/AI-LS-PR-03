import matplotlib.pyplot as plt
import numpy as np

# task 1
# x = np.linspace(-10, 10, 500)
# y = (x ** 2) * np.sin(x)

# plt.plot(x, y)
# plt.title("Графік функції x^2 * sin(x)")
# plt.xlabel("x")
# plt.ylabel("x^2 * sin(x)")
# plt.grid(True)
# plt.show()

# task 2
# data = np.random.normal(loc=5, scale=2, size=1000)

# plt.hist(data, bins=30, color='skyblue', edgecolor='black')
# plt.title("Гістограма розподілу")
# plt.xlabel("Значення")
# plt.ylabel("Частота")
# plt.grid(True)
# plt.show()

#task 3
# labels = ['Малювання', 'Вивчення історії', 'Англійська', 'Читання', 'Ігри']
# sizes = [10, 25, 20, 25, 20]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Співвідношення видів транспорту")
# plt.axis('equal')
# plt.legend()
# plt.show()

# task 4
# np.random.seed(0) 

# group_A = np.random.normal(loc=70, scale=10, size=100)
# group_B = np.random.normal(loc=80, scale=5, size=100)
# group_C = np.random.normal(loc=65, scale=15, size=100)

# plt.boxplot([group_A, group_B, group_C], labels=['Група A', 'Група B', 'Група C'])
# plt.title("Box-Plot оцінок трьох груп студентів")
# plt.ylabel("Оцінки")
# plt.grid(True)
# plt.show()

# task 5
# x = np.random.rand(100)
# y = np.random.rand(100)

# plt.scatter(x, y, color='green', alpha=0.6)
# plt.title('Розсіювання даних')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()

# task 6
# X = np.linspace(0, 10, 100)
# y1 = np.sin(X)
# y2 = np.cos(X)
# y3 = np.sin(X) + np.cos(X)

# plt.plot(X, y1, color='green', label='f(x) = sin(x)')
# plt.plot(X, y2, color='blue', label='g(x) = cos(x)')
# plt.plot(X, y3, color='red', label='h(x) = sin(x) + cos(x)')
# plt.title('Графіки функцій')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.grid(True)
# plt.show()