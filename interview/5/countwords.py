f = open("abc.txt", 'r')
count = 0
for line in f:
    words = line.split(" ")
    count= count + len(words)
    words = line.split(",")
    count = count + len(words)
print("Total Number of Words:"+str(count))
f.close()
