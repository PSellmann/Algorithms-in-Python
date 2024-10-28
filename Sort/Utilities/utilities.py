def swappListElements(x, indexOne, indexTwo):
    swappedList = list(x)
    swappedList[indexOne], swappedList[indexTwo] = swappedList[indexTwo], swappedList[indexOne]
    return swappedList
 
if __name__ == "__main__":
    pass