def swappListElements(x, indexOne, indexTwo):
    swappedList = list(x)
    tmp = swappedList[indexOne]
    swappedList[indexOne] = swappedList[indexTwo]
    swappedList[indexTwo] = tmp
    return swappedList
 
if __name__ == "__main__":
    pass