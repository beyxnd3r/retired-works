n = int(input("Введите елочку"))

for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('#' * (2 * i + 1))
print(' ' * (n - 1) + '#')
