f=open("test_genome.txt")

total_same = 0
total_different = 0

for i, line in enumerate(f):
    if line[0]=="#":
        continue
    else:
        d = line.strip().split("\t")

        if d[1] == "MT":
            continue
        same = d[3][0] == d[3][1]
        
        if same:
            total_same += 1
        else:
            total_different += 1

print total_same
print total_different