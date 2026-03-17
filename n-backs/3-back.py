n_backs = "A B C A E F B E F G H X G I L M N O X C O"

def turn_str_to_list(string:str) -> list:
    output = string.split()
    return output

# Ok now I want to work out how many 3-backs there are. 

# How to do that
# Firstly, it's about the 3-sliding window. 
# Ranging and indexing can be used


# So given a list of letters:
# How to loop through them: range of length of loop? Does that work
# Will that not give index out of range
# I guess in the actual game, I think it's always out of 18. 
# Meaning the list is divisible by 3. 

# Shall we make an interim program that splits a list into subset of 3
def split_list_into_subsets_of_3(big_list:list)-> list[list[str]]:
    subsets_of_three = []
    for x in range(len(big_list)):
        subsets_of_three.append(big_list[x:x+3])
        print(subsets_of_three)
    return subsets_of_three
        
# Input = ['A', 'B', 'C', 'A', 'E', 'F', 'B', 'E', 'F', 'G', 'H', 'X', 'G', 'I', 'L', 'M', 'N', 'O', 'X', 'C', 'O']
# Output = [['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'E'], ['A', 'E', 'F'], ['E', 'F', 'B'], ['F', 'B', 'E'], ['B', 'E', 'F'], ['E', 'F', 'G'], ['F', 'G', 'H'], ['G', 'H', 'X'], ['H', 'X', 'G'], ['X', 'G', 'I'], ['G', 'I', 'L'], ['I', 'L', 'M'], ['L', 'M', 'N'], ['M', 'N', 'O'], ['N', 'O', 'X'], ['O', 'X', 'C'], ['X', 'C', 'O'], ['C', 'O'], ['O']]

# The end of the output is: [['X', 'C', 'O'], ['C', 'O'], ['O']]
# So I guess the index out of range error is only when you're trying to index for it
# When it's performing a looping operation, and can't index that far. It just returns as far as it can go!


# For the nth item in the list, being judged against: let's call that n_term
# For the length of three_back = [i:i+3] - that's to get the 3 back position
# is n_term == three_back
# If so counter accumulates 

#TODO: Do build the function planned above

def three_back_count(n_backs: list) -> int:
    count = 0
    


if __name__ == "__main__":
    n_backs_list = turn_str_to_list(n_backs)
    print(n_backs_list)
    print(split_list_into_subsets_of_3(n_backs_list))


    