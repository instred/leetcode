from typing import Dict, List
from datetime import datetime, timedelta
from statistics import median
from random import randint


# Nie byłem pewny w jakim języku pisac komentarze, więc zdecywowałem się na użycie angielskiego ze względu na uniwersalność 
# i to, że zwykle to nim sie posługuje pisząc kod, komentarze czy commity.

expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}



# Some custom testing data 
# expenses_sparse = {
#     "2023-02": {
#         "10": {
#             "food": [15.0],
#             "fuel": [45.0]
#         },
#     },
# }


# First, some helper functions for the end solution
def findFirstSunday(year: str, month: str) -> int:

    # Get the 7th day of the month as a datetime obj
    date = datetime(int(year), int(month), 7)

    # Calc the offset - Mon is 0, so Sun 6
    # Ex. 7th is Tue - 1, so to find first Sun we need to subtract 2 days
    day = (date.weekday() - 6 ) % 7
    return date - timedelta(day)


def extractDict(expenses: Dict) -> List | None:
    valid_expenses = []

    # Loop through data end add valid ones
    
    for date, days in expenses.items():
        year, month = date.split('-')
        
        # Get the first Sunday as a Date obj
        firstSunday = findFirstSunday(year, month)
        
        for day, categories in days.items():  
            if int(day) > firstSunday.day:
                continue
            
            for values in categories.values():  
                valid_expenses.extend(values)

    return valid_expenses

def partition(arr: List[int], left: int, right: int) -> int:
    
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quickSelect(arr: List[int], left: int, right: int, k: int):

    if left == right:
        return arr[left]
    
    # I've choosen the random pivot variation since it's generally better for avoiding worst cases. 
    pivot_index = randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    pivot_idx = partition(arr, left, right)
    
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return quickSelect(arr, left, pivot_idx-1, k)
    else:
        return quickSelect(arr, pivot_idx+1, right, k)
    

# Sol1 will loop through the data, adding every value that fits the condition (to first Sun), 
# then will use the built-in sort on expenses list to get sorted list, on which wer can use the median from statistics lib to calculate the median.

# Apart from the values extraction, the median will be O(nlogn), since this is the time complexity for python .sort(), which median function uses internally

def solution1(expenses: Dict) -> int | None:
    valid_expenses = extractDict(expenses)

    return median(valid_expenses) if valid_expenses else None


# There are 3 ways we can optimize it (at least 3 I could think about), all of them will be faster than just .sort()
# Quicksort - avg O(nlogn), O(logn - recursion stack) 
# Heaps - O(nlogn) since, n * logn insertions, O(n) space
# QuickMerge - avg O(n), worst O(n^2), which I will use since it will be the best one for large datasets, with no extra space. Also, we don't need the sorted list anyway
# We will look for the kth smallest element (k being middle one)

def solution2(expenses: Dict) -> int | None:
    valid_expenses = extractDict(expenses)
    if not valid_expenses:
        return None
    
    n = len(valid_expenses)
    if n % 2 == 1:
        return quickSelect(valid_expenses, 0, n-1, n//2)
    else:
        left = quickSelect(valid_expenses, 0, n-1, (n//2)-1)
        right = quickSelect(valid_expenses, 0, n-1, n//2)
        return (left+right) / 2
