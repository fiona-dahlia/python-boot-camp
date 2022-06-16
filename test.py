import list_util

word = 'fiona'
word_length = len(word)
print('word:', word)
print('word length:', word_length)

for i in range(0, word_length):
    print(i, word[i])

print()

for i in range(word_length - 1, -1, -1):
    print(i, word[i])

word_reversed = ''
a = 'f'
b = 'i'
c = 'o'

word_reversed = a + b + c
print('word_reversed:', word_reversed)

res = list_util.two_sum([1, 2, 3, 4], 11)
print(res)
