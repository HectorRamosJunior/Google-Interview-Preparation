"""Given a sorted array of size N of int32, find an element that repeats 
greater than ceil(N / 2) times. Your algo may assume that there will be 
always such element.    Space/time O(1). 

Follow up question: Now element repeats > ceil(N / 4) times. Space/time O(1)

https://www.careercup.com/question?id=5647871593414656
"""

# For N/2
def findRepeatingElement(array):
    length = len(array)

    if length == 2:
        return array[0]

    # In order for a sorted array to cross this proportion,
    # The indexes of the length / proportion become a chokepoint
    index = length / 2 - 1

    # Ceiling
    if length % 2 == 1:
        index += 1

    if array[index] == array[index - 1] and array[index] == array[index + 1]:
        return array[index]


# For N/4
def findRepeatingElement2(array):
    length = len(array)

    if length == 2:
        return array[0]
    elif length <= 4:
        return array[1]

    index = length / 4 - 1

    # Ceiling
    if length % 4 > 0:
        index += 1

    # 3 checks: Left Quarter, Middle, Right Quarter
    for x in xrange(3):
        if array[index] == array[index - 1] and array[index] == array[index + 1]:
            return array[index]

        # Handoff for Right Quarter
        if x == 0:
            index = length - 1 - index
        # Handoff for Middle
        elif x == 1:
            index = length / 2 - 1

            # Ceiling
            if length % 2 == 1:
                index += 1

l1 = [1, 1, 1, 1, 1, 1, 7, 8, 9, 10]
l2 = [1, 1, 1, 1, 5, 6, 7, 8, 9, 10]
l3 = [1, 2, 3, 3, 3, 3, 7, 8, 9, 10]
l4 = [1, 2, 3, 4, 7, 7, 7] 
l5 = [1, 2, 3, 3, 3, 6, 7]
l6 = [1, 2, 2, 4]



print findRepeatingElement(l1)
print findRepeatingElement2(l2)
print findRepeatingElement2(l3)
print findRepeatingElement2(l4)
print findRepeatingElement2(l5)
print findRepeatingElement2(l6)