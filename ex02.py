import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, x, y, angle, length, level, max_level):
    if level > max_level:
        return

    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    ax.plot([x, x_end], [y, y_end], color='brown', lw=2)

    new_length = length * 0.75  # Зменшення довжини на кожному рівні
    draw_tree(ax, x_end, y_end, angle + np.pi / 6, new_length, level + 1, max_level)
    draw_tree(ax, x_end, y_end, angle - np.pi / 6, new_length, level + 1, max_level)

def pythagoras_tree(levels):
    fig, ax = plt.subplots()

    # підлаштував межі графіку, бо обрізалоьс
    ax.set_xlim([-15, 15])
    ax.set_ylim([0, 20])

    draw_tree(ax, 0, 0, np.pi / 2, 5, 1, levels)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

levels = int(input("Введіть рівень рекурсії для дерева Піфагора: "))
pythagoras_tree(levels)