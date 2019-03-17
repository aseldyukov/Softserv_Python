# Reversing Words in a String
def rev_words(s):
    s = s.split()
    s.reverse()
    s = ''.join(s)
    print(s)

some_words = input('Введіть декілька слів через пробіл: ')
rev_words(some_words)