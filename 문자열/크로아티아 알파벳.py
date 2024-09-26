# https://www.acmicpc.net/problem/2941

cta = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cta:
    word = word.replace(i, '#')

#print(word)
print(len(word))