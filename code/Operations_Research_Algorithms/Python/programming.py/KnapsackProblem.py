def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], result


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack(values, weights, capacity)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)
