letters = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '10': ' '
}
word = input("Введите слово или фразу")
word = word.upper()
for slovo in word:
    for ind in letters:
        if slovo in letters[ind]:
            for k in letters[ind]:
                if k==slovo:
                    print(ind, end='')
                    break
                else:
                    print(ind, end='')