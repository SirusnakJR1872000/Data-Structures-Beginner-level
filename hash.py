# lets assume a array
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}

for name in names:
    # if countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1