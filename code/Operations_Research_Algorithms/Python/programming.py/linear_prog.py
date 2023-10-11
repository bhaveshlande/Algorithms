from scipy.optimize import linprog

c = [-3, -2]
A = [
    [1, 1],
    [2, 1],
]
b = [4, 5]

x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

if result.success:
    print("Optimal solution found:")
    print("x =", result.x[0])
    print("y =", result.x[1])
    print("Optimal value =", -result.fun)
else:
    print("No optimal solution found.")
