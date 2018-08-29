from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Make list of all lines for both a and b
    linelist_a = a.splitlines()
    linelist_b = b.splitlines()

    # Create sets of linelists to eliminate duplicates and allow intersection
    lset_a = set(linelist_a)
    lset_b = set(linelist_b)

    # return all values that lset_a and lset_b share
    return lset_a.intersection(lset_b)


def sentences(a, b):
    """Return sentences in both a and b"""

    # take separate lists of sentences in strings a and b
    senlist_a = sent_tokenize(a)
    senlist_b = sent_tokenize(b)

    # turn lists into sets to eliminate duplicates and allow intersection
    senset_a = set(senlist_a)
    senset_b = set(senlist_b)

    # return all values that senset_a and senset_b share
    return senset_a.intersection(senset_b)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # function takes string s and substring-length n as input, and gives back list of all substrings of length n
    def extract_substr(s, n):
        substrs = []

        j = n
        i = 0
        while j <= len(s):
            substrs.append(s[i:j])
            i += 1
            j += 1

        return substrs

    # make lists of substrings for a and b
    substrlist_a = extract_substr(a, n)
    substrlist_b = extract_substr(b, n)

    # turn both lists of substrings into sets to remove duplicates and allow intersection
    substrset_a = set(substrlist_a)
    substrset_b = set(substrlist_b)

    # return all substrings that are in both a and b
    return substrset_a.intersection(substrset_b)
