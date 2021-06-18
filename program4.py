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

print(primeFinder(100))