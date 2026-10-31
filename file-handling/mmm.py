#ziayd zac here


file=open("/Users/mac/Desktop/ziyad/hoja python/file-handling/test.py","r")
print(file.read())
file.close()

file=open("/Users/mac/Desktop/ziyad/hoja python/file-handling/test.py","r")
for line in file:
    print(line.strip())
file.close()



