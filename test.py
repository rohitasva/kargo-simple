def get_permutations(string):
    permutations = []

    if len(string) <= 1: return [string]
    last = string[-1]
    rest = string[:-1]

    all_permutations = get_permutations(rest)

    for permutation in all_permutations:
        for i in range(0, len(permutation)+1):
            new_word = permutation[:i] + last + permutation[i:]
            permutations.append(new_word)
    return permutations

print(get_permutations("235"))

