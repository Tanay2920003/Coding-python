f1 = open('file2.txt')
f2 = open('file2copy.txt','w')
for line in f1:
    if 'a' not in line:
        f2.write(line)
        print('## File Copied Successfully! ##')
f1.close()
f2.close()
