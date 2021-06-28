def calculateValues(num, value, word):
    if int(value) < num:
        return True
    elif str(value) != word and len(word) < 10:
        return True
    else:
        return False

print(calculateValues(4, "7", "clocking"))