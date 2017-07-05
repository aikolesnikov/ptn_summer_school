import string

print(dir(string))

with open('pg1661.txt', 'rt') as f:
    # for line in f:
    #    print(line)

    text = f.read()
    print(text)

    p = {ord(char): '' for char in string.punctuation}
    print(p)

    words = text.lower().translate(p).split()
    print(words)

    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] = word_counter[word] +1
        else:
            word_counter[word] = 1

    print(word_counter)
    print(len(word_counter))

    // отсортировать слова по частоте и записать в файл