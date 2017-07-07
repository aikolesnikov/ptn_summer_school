import string

# print(dir(string))

with open('pg1661.txt', 'rt') as f:
    # for line in f:
    #    print(line)

    text = f.read()
    # print(text)

    p = {ord(char): '' for char in string.punctuation}
    # print(p)

    words = text.lower().translate(p).split()
    # print(words)

    word_counter = {}
    for word in words:
        if word in word_counter:
            word_counter[word] = word_counter[word] + 1
        else:
            word_counter[word] = 1

    # print(word_counter)
    # print(len(word_counter))

    # sort by freequency and write to file
    # sorted(word_counter)
    # with open('w_pg1661.txt', 'wt') as f2:
    #    for w in word_counter:
    #        f2.write(w)
    #        f2.write('\n')

    counter_word = [(counter, word) for word, counter in word_counter.items()]
    print(counter_word)

