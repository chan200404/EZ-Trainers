pw = []
profit = [20, 10, 6, 9, 18, 12, 16, 30, 15]
weight = [4, 5, 6, 3, 2, 5, 4, 6, 6]
capacity = 30
for i in range(len(profit)):
    p_w = profit[i] / weight[i]
    pw.append((p_w, profit[i], weight[i]))  

pw.sort(reverse=True, key=lambda x: x[0])

total_profit = 0

def knapsack(capacity):
    global total_profit
    for p_w, p, w in pw:
        if capacity >= w:  
            total_profit += p
            capacity -= w
    
    return total_profit

max_profit = knapsack(capacity)

print("Profit:", max_profit)
