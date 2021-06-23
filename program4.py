def fibonacciFinder(max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k

for i in range (2, 100):
    for j in range (2,3):
        if i % j == 0:
            break
        else:
            print(i)

def primeFinder(max):
    for i in range (2, 100):
        for j in range (2,3):
            if i % j == 0:
                break
            else:
                print(i)

# print(primeFinder(100))

def triangleArea(base, height):
    area = base*height/2
    return area

areaList = [0]*5

for b in range(0,5):
    areaList[b] = triangleArea(b, 6)

print(areaList)

# function with a tuple as the parameter
#def foodSum2(Dict, *args):
    #for keys in args:
        #print(Dict[keys])

#foodSum2(Menu, "Burgers")

#def foodSum2(Dict, *args):
    #for keys in args:
        #if keys in args:
            #sum += Dict[keys]

#foodSum2(Menu, "Burgers")

#list1 = [1, 2, 3, 4, 5]
#list2 = [10, 11, 12, 13, 14]
#difflist = []

# for i in list1:
    #for j in list2:
        #diffList.append(abs(i - j))
#diffList.sort()
#print(diffList[0])