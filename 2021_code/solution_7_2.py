# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
        # print(line)
        count += 1
        test = line.strip()
        val = test.find("0")
        val_add = float(test[val::])
        total += val_add
    
avg = total/count
print("Average spam confidence:",avg)
# print("Done")
