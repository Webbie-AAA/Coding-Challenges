def valid_braces(string):
    paranthesis_dict = {'(': ')', '{': '}', '[': ']'}
    for paran in string:
        print(paran)
        if paran in '([{':
            if paranthesis_dict[paran] not in string:
                print(paranthesis_dict[paran])
                return False
        else:
            return False
    return True


print(valid_braces('()'))
