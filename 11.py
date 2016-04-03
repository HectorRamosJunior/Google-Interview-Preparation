"""Find the no of possible patterns in android lock screen. 
Write a program to count them.
Assumes nodes needed for a pattern are 4 <= n <= 9

https://www.careercup.com/question?id=5663422257561600
"""

# Calls the first recursive function, returns the number of patterns
def get_num_patterns(min_length, max_length, node_list):
    # Hash set for O(1) lookup time when checking for new patterns
    patterns_set = set()

    for node in node_list:
        get_patterns(node, patterns_set, min_length, max_length)

    return len(patterns_set)

# Recursively calls itself to get every possible pattern available from
# The last node visited given and the pattern its currently on.
def get_patterns(node, patterns_set, min_length, max_length,
                        current_pattern_list=[]):

    pattern_length = len(current_pattern_list)

    # Add pattern if it is valid length and not in patterns_set yet
    if pattern_length >= min_length and pattern_length <= max_length:
        pattern_as_string = get_string_representation(current_pattern_list)

        if not pattern_as_string in patterns_set:
            patterns_set.add(pattern_as_string)

    # If pattern can be longer, check for any possible patterns recursively
    if pattern_length < max_length:
        for adjacent_node in node.edge_list:
            # Only add adjacent nodes to pattern if unvisited.
            if not adjacent_node.key in current_pattern_list:
                # Copies so it doesn't modify previous calls' lists by ref
                next_pattern_list = list(current_pattern_list)
                next_pattern_list.append(adjacent_node.key)

                get_patterns(adjacent_node, patterns_set, min_length,
                            max_length, next_pattern_list)

# Returns string representation of the current list of node keys
def get_string_representation(current_pattern_list):
    output_string = ""

    for node_key in current_pattern_list:
        output_string += node_key + " "

    return output_string

class Node(object):
    def __init__(self, key, edge_list=[]):
        self.key = key
        self.edge_list = edge_list


if __name__ == "__main__":
    # Lock screen assumed to be a 3x3 grid where each node can access
    # only the nodes immediately nearby diagonally or horizontally/veritcally
    # Graph looks as follows:
    # 1 2 3
    # 4 5 6
    # 7 8 9

    n1 = Node("1"); n2 = Node("2"); n3 = Node("3")
    n4 = Node("4"); n5 = Node("5"); n6 = Node("6")
    n7 = Node("7"); n8 = Node("8"); n9 = Node("9")

    n1.edge_list = [n2, n4, n5]
    n2.edge_list = [n1, n3, n4, n5, n6]
    n3.edge_list = [n2, n5, n6]
    n4.edge_list = [n1, n2, n5, n7, n8]
    n5.edge_list = [n1, n2, n3, n4, n6, n7, n8, n9]
    n6.edge_list = [n2, n3, n5, n8, n9]
    n7.edge_list = [n4, n5, n8]
    n8.edge_list = [n4, n5, n6, n7, n9]
    n9.edge_list = [n5, n6, n8]

    node_list = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

    num = get_num_patterns(min_length=4, max_length=9, node_list=node_list)
    print "There are %d num patterns for the lock screen given." %num
    print "This assumes each node can only access nodes directly adjacent"
