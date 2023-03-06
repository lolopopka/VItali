from collections import defaultdict
def revert(dct):
    new_dict = defaultdict(list) #cоздали словарь value которого есть массив
    for key, value in dct.items():
        new_dict[value].append(key)
    return new_dict

d = {1:2 , 2:4 , 3:4}
print(revert(d))