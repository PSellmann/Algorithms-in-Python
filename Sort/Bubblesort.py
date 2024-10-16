import Utilities.utilities as ut

def bubblesort(listToSort):
    sortedList = list(listToSort)
    swapped = True
    while swapped:
        index = 0
        swapped = False
        while index < len(sortedList) - 1:
            if sortedList[index] > sortedList[index + 1]:
                swapped = True
                sortedList = ut.swappListElements(sortedList, index, index + 1)
            index += 1
    return sortedList
        

if __name__ == "__main__":
    listToSort = [8, 3, 9, 1, 5, 4, 6, 10, 7, 2]
    sortedList = bubblesort(listToSort)
    
    print(f"Unsorted list: {listToSort}")
    print(f"Sorted list: {sortedList}")