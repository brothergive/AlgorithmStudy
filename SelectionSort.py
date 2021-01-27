def selection_sort(s):
    for i in range(len(s)):
        for j in range(i+1,): #i+1 ~ 끝
            if s[i] < s[j]:
                s[i], s[j] = s[j], s[i]
    return print(s)

s = [1, 4, 2, 0, 9, 5, 3]
selection_sort(s)