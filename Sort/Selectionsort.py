import Utilities.utilities as ut

def selectionsort(ListToSort):
    sortedList = list(listToSort)
    index = 0
    while index < len(sortedList) - 1:
        lowestValueIndex = index
        searchIndex = index + 1
        while searchIndex < len(sortedList):
            if sortedList[searchIndex] < sortedList[lowestValueIndex]:
                lowestValueIndex = searchIndex
            searchIndex += 1
        sortedList = ut.swappListElements(sortedList, index, lowestValueIndex)
        index += 1
    return sortedList

if __name__ == "__main__":
    listToSort = [8, 3, 9, 1, 5, 4, 6, 10, 7, 2]
    sortedList = selectionsort(listToSort)
    
    print(f"Unsorted list: {listToSort}")
    print(f"Sorted list: {sortedList}")