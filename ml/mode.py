from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# the mode is the value that appears most frequently
x = stats.mode(speed)

print(x)
