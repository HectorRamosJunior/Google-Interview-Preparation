"""Given an array of numbers, find the longest alternating subsequence. 
That is, a subsequence [a1, a2, a3, ..., ak] where a1 > a2, a3 < a2, ... 
Or vice versa (Graphically looks like /\/\/\... or \/\/\/\....)

https://www.careercup.com/question?id=5667564572114944
"""

# Tailored version of the DP solution to the longest increasing subsequence.
# Employs memoization by storing the longest list ending in increasing 
# and decreasing for each index of the array, and finds the longest sequence
# ending in decreasing and increasing possible by checking the previous indexes.
def longest_alternating_subsequence(array):
    # Initializes two lists to each index in the array given
    # The first list will be for subsequences that end alternating up
    # The second list wil be for subsequences that end alternating down
    subsequence_list = [ [[], []] for x in xrange(len(array))]

    # 
    for i in xrange(len(array)):
        i_list_alternating_up, i_list_alternating_down = subsequence_list[i]

        # Checks the previous indexes' alternating lists and appends itself 
        # To the longest valid alternating subsequence available
        for j in xrange(i):
            j_list_alternating_up, j_list_alternating_down = subsequence_list[j]

            # Look at the altnerating down list of the current prior index
            if array[i] > array[j]:
                if len(j_list_alternating_down) + 1 > len(i_list_alternating_up):
                    i_list_alternating_up = list(j_list_alternating_down)
            # Look at the alternating up list of the current prior index
            elif array[i] < array[j]:
                if len(j_list_alternating_up) + 1 > len(j_list_alternating_down):
                    i_list_alternating_down = list(j_list_alternating_up)

        # Append the value of i to the end of both lists
        i_list_alternating_up.append(array[i])
        i_list_alternating_down.append(array[i])
        # Add updated lists for i back into subsequence list
        subsequence_list[i][0] = i_list_alternating_up
        subsequence_list[i][1] = i_list_alternating_down

        # For possible debugging.
        print "The longest subsequences for index %d:" % i
        print "Ending alternating up: ", subsequence_list[i][0]
        print "Ending alternating down: ", subsequence_list[i][1]

    # Grabs the longest subsequence, whichever alternation it ends up
    longest_alternating = []
    for subsequence in subsequence_list:
        increased_list, decreased_list = subsequence

        if len(increased_list) > len(longest_alternating):
            longest_alternating = increased_list
        if len(decreased_list) > len(longest_alternating):
            longest_alternating = decreased_list

    return longest_alternating


if __name__ == "__main__":
    from random import randint

    array = [randint(-100,100) for x in xrange(10)]

    print "The randomized given array is :"
    print array, "\n"

    longest_alternating = longest_alternating_subsequence(array)
    print "\nThe longest altnerating subsequence for the given array is: "
    print longest_alternating