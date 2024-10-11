def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            chosen_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    chosen_items = [[] for _ in range(budget + 1)]
    
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                chosen_items[b] = chosen_items[b - cost] + [item]
    
    return chosen_items[budget], dp[budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 90
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм: вибрані страви {greedy_result}, загальна калорійність: {greedy_calories}")

print("===================================")

dp_result, dp_calories = dynamic_programming(items, budget)
print(f"Динамічне програмування: вибрані страви {dp_result}, загальна калорійність: {dp_calories}")