#https://informatics.msk.ru/mod/statements/view.php?id=4535&chapterid=3757#1
schoolboys = int(input())
languages = {}
for g in range(1, schoolboys + 1):
    languages[g] = set()
    number_of_languages = int(input())
    for t in range(number_of_languages):
        language = input()
        languages[g].add(language)
share_languages = languages[1]
all_languages = languages[1]
for i in range(2, schoolboys + 1):
    share_languages = share_languages.intersection(languages[i])
    all_languages = all_languages.union(languages[i])
print(len(share_languages))
for i in share_languages:
    print(i)
print(len(all_languages))
for i in all_languages:
    print(i)



