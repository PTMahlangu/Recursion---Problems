
def find_min(elements):
    """This fuction finds and returns the minimum element in a list of integers."""
    if (len(elements)==1) and isinstance(elements[0],int):
        return elements[0]
    elif (not elements) or (not isinstance(elements[0],int)):
        return -1

    index_0 = elements[0]
    smallest = find_min(elements[1:])

    if index_0 < smallest:
        return index_0
    else:
        return smallest


def sum_all(elements):
    """This function calculates and returns the sum of all element in a list of integers."""
    for index in elements:
        if not isinstance(index,int):
            return -1

    if len(elements)==1:
        return elements[0]

    elif not elements:
        return -1

    else:
        return sum_all(elements[1:]) + elements[0]
        

def find_possible_strings(character_set,k):
    """Thi fuction  print all possible strings of length n that can be formed from the given set."""
    def permutation_repeat(text, prefix, k,list2):
        n = len(text)
        if k == 0: # checks, len(prefix) == len(text)
            list2.append(prefix)
            return 

        for i in range(n):
            new_prefix = prefix + text[i] 
            permutation_repeat(text, new_prefix, k-1,list2)
        
    possible_strings =[]
    for index in character_set:
        if not isinstance(index,str):
            return possible_strings

    permutation_repeat(character_set,"",k,possible_strings)
    return possible_strings

    




