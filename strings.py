#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    if len(pattern) == 0:
        return True
    elif len(pattern) > len(text):
        return False
    else:
        if find_index(text, pattern) == None:
            return False
        else: 
            return True

    # position = 0
    # for char in text:
    #     if char == pattern[position]:
    #         if position == len(pattern) - 1:
    #             return True
    #         else: 
    #             position += 1
    #     else:
    #         position = 0
    # return False

 
def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    if len(pattern) == 0:
        return 0

    index = None
    position = 0

    for (ind, char) in enumerate(text):
        if char == pattern[position]:
            if position == 0:
                index = ind
            if position == len(pattern) - 1:
                return index
            position += 1
        else:
            if text[ind] == pattern[0]:
                index = ind
                position = 1
            elif char == pattern[0]:
                index = ind
                position = 0
            else:
                index = None
                position = 0

    return index


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    all_indexes = []

    if len(pattern) == 0:
        return list(range(len(text)))
    elif len(pattern) == 1:
        position = 0
        for (ind, char) in enumerate(text):
            if char == pattern[position]:
                all_indexes.append(ind)
        return all_indexes
    else:
        all_indexes = []

        start_index = None
        patt_position = 0


        for i in range(len(text)):
            if text[i] == pattern[patt_position]:
                if patt_position == 0:
                    start_index = i
                    patt_position += 1
                elif patt_position == len(pattern) - 1:
                    all_indexes.append(start_index)
                    start_index = None
                    patt_position = 0
                    if text[i] == pattern[0]:
                        start_index = i
                        patt_position = 1
            else:
                patt_position = 0
                start_index = None

        return all_indexes

    return all_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    # print(contains('abra cadabra', 'abra'))
    # print(find_index('abra cadabra', 'dabra'))
    print(find_index('ababcd', 'babcd'))
    print(find_all_indexes('abccc', 'cc'))
    # print(find_all_indexes('abccabc', 'abc'))