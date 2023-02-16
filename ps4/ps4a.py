# Problem Set 4A
# Name: Ishan Mukherjee
# Collaborators: -
# Time Spent: 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # base case: if a string is a single character, return the character as the
    # only member of the permutations list, since the only permutation of a
    # single-character string is the character itself
    if len(sequence) <= 1:
        return[sequence]
    
    permutations_list = []
    
    # get_permutations(sequence[1:]) returns the permutations of all but the
    # first character in sequence
    for permutation in get_permutations(sequence[1:]):    
        # len(str) + 1 is the number of places in the str where you can put an 
        # extra letter, eg the letter "x" can be placed in "ab" in three ways:
        # "xab", "axb", "abx"
        for i in range(len(permutation) + 1): 
            # place sequence[0] in the i'th position of a string
            new_permutation = permutation[0:i]+sequence[0]+permutation[i:]
            if new_permutation not in permutations_list:
                permutations_list.append(new_permutation)
    
    return permutations_list
    
            

if __name__ == '__main__':
    # test case 1
    example_input = "ab"
    print("\nInput:", example_input)
    print("Expected Output:", ["ab", "ba"])
    print("Actual Output:", get_permutations(example_input))
    
    # test case 2
    # copied from example
    example_input = "abc"
    print("\nInput:", example_input)
    print("Expected Output:", ["abc", "acb", "bac", "bca", "cab", "cba"])
    print("Actual Output:", get_permutations(example_input)
          
    # test case 3
    example_input = "xxy"
    print("\nInput:", example_input)
    print("Expected Output:", ["xxy", "xyx", "yxx"])
    print("Actual Output:", get_permutations(example_input))
