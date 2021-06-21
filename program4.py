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

