text = input('Enter your text: ')


def stringToArray(str):
    return str.split()


splittedText = stringToArray(text)


def countWords():
    i = 0
    sum = 0
    while i < len(splittedText):
        i += 1
        sum = i
    print (sum)

print(splittedText)
countWords()



