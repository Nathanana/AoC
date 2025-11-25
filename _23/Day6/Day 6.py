times = [49877895]
distances = [356137815021882]

total1 = 1

for id, t in enumerate(times):
    wins = 0
    for i in range(t+1):
        if (t - i) * i > distances[id]:
            wins += 1
    total1 *= wins
    
print(total1)