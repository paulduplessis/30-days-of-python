ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

ages_min = ages[0]
ages_max = ages[-1]

print(ages_min)
print(ages_max)

ages.append(ages_min)
ages.append(ages_max)

ages.sort()

median_pos1 = (len(ages) - 1) // 2
median_pos2 = len(ages) // 2

ages_median = (ages[median_pos1] + ages[median_pos2]) / 2
print(ages_median)

ages_mean = sum(ages) / len(ages)
print(ages_mean)

ages_range = ages[-1] - ages[0]
print(ages_range)

