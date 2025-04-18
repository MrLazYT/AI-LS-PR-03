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
# labels = ['Автомобіль', 'Велосипед', 'Громадський транспорт', 'Пішки']
# sizes = [50, 20, 25, 5]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title("Співвідношення видів транспорту")
# plt.axis('equal')
# plt.legend()
# plt.show()

# task 4
np.random.seed(0) 

group_A = np.random.normal(loc=70, scale=10, size=100)
group_B = np.random.normal(loc=80, scale=5, size=100)
group_C = np.random.normal(loc=65, scale=15, size=100)

plt.boxplot([group_A, group_B, group_C], labels=['Група A', 'Група B', 'Група C'])
plt.title("Box-Plot оцінок трьох груп студентів")
plt.ylabel("Оцінки")
plt.grid(True)
plt.show()