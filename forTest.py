# aList = [1,2,3,4,5,6]
# print (len(aList))

# for i in range(len(aList)):
#     print(i)

anotherList = ["a\tb\tc", "d\te", "f"]

for i in range(len(anotherList)):
    anotherList[i] = anotherList[i].split("\t")

for line in anotherList:
    print (line)

binval = "101010010100101010101001010101010101010011100101"
print(hex(int(binval, 2)))