from itertools import product
def gen_comb_list(list_set):
    '''
        Parameters:
            list_set: a list of lists where each contains at least one element

        Returns:
            a list of lists, each of which is made from a combination of elements in each list in list_set

        Examples:
            gen_comb_list([[1, 2, 3]]) returns [[1], [2], [3]]
            gen_comb_list([[1, 2, 3], [4, 5]]) returns [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]]
            gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]) returns [[1, 4, 6], [2, 4, 6], [3, 4, 6], [1, 5, 6], [2, 5, 6], [3, 5, 6], [1, 4, 7], [2, 4, 7], [3, 4, 7], [1, 5, 7], [2, 5, 7], [3, 5, 7], [1, 4, 8], [2, 4, 8], [3, 4, 8], [1, 5, 8], [2, 5, 8], [3, 5, 8]]
    '''


    for i in list_set:
        if len(i) > 1:
            new_list_ii = []
            for combination in product(*list_set):
                # print(*original_list_ii)
                new_list_ii.append(list(combination))
            return new_list_ii

        else:
            new_list = []
            for i in list_set:
                # keep_j = []
                # print(keep_j)
                for j in i:
                    keep_j = []
                    keep_j.append(j)
                    # print(keep_j)
                    new_list.append(keep_j)
            return new_list

# print(gen_comb_list([[1, 2, 3]]))
# print(gen_comb_list([[1, 2, 3], [4, 5]]))
# print(gen_comb_list([[1, 2, 3], [4, 5], [6, 7, 8]]))