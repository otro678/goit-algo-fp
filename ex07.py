import random
import matplotlib.pyplot as plt

n_simulations = 5000000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(n_simulations):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_1 + dice_2
    sum_counts[dice_sum] += 1

sum_probabilities = {key: value / n_simulations * 100 for key, value in sum_counts.items()}

print("Ймовірності для кожної суми (за методом Монте-Карло):")
for key in sorted(sum_probabilities.keys()):
    print(f"Сума: {key}, Ймовірність: {sum_probabilities[key]:.2f}%")

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

x_values = list(sum_probabilities.keys())
y_values_mc = list(sum_probabilities.values())
y_values_analytical = [analytical_probabilities[key] for key in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_mc, label="Монте-Карло", marker='o')
plt.plot(x_values, y_values_analytical, label="Аналітичні", marker='x')
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння ймовірностей (Монте-Карло та аналітичні)")
plt.legend()
plt.grid(True)
plt.show()
