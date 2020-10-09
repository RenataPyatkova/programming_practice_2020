dictionary = {}

for i in range(int(input())):
    words = input().split()
    dictionary[words[0]] = words[1]

word = input()
for key in dictionary:
    if key == word:
        print(dictionary[key])

    if dictionary[key] == word:
        print(key)