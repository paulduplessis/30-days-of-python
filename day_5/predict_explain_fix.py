import copy

team = [["Paul", 80], ["Tom", 75]]
backup = team.copy()
backup[0][1] = 0
backup.append(["New", 50])
print(team)


# .copy() creates a shallow copy, so the inner lists are still shared by backup
# hence when ["Paul", 80] is changed to ["Paul", 0] it changes the team object too
# output is [["Paul", 0], ["Tom", 75]]
# change is below to fix this + import copy at top

team = [["Paul", 80], ["Tom", 75]]

deep_backup = copy.deepcopy(team)
deep_backup[0][1] = 0
deep_backup.append(["New", 50])
print(team)