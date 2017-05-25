f = open('originalDataset.txt', 'U')
ff = open('updatedDataset.txt', 'wb')

for line in f:
    if not '?' in line:
                ff.write(line)
f.close()
ff.close()
