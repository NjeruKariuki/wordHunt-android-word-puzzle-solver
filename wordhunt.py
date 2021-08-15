from itertools import permutations

global len_ls

def get_perms(ls):
    len_ls = len(ls)
    words = []
    perms = list(permutations(ls))
    print(len(perms))
    for name in range(len(perms)):
        word = ' '.join(map(lambda x: str(x[0]) + str(x[1]) + str(x[2]), perms))
        words.append(word)
    return words

lst_ex = ['a', 'n', 'd']
print(get_perms(lst_ex))