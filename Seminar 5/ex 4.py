def max_line_file(filename):
    f = open(filename, 'r')

    result = []

    for line in f:
        max_lenght = 0
        max_word = ''

        words = line.split(' ')

        for word in words:
            word = word.strip()

            if len(word) > max_lenght:
                max_word, max_lenght = word, len(word)

        result.append(max_lenght)

    f.close()
    return result

def test_max_line_file():
    assert max_line_file('data.input') == [4, 4]

def is_palindrom(word):
    return word == word[::-1]

def find_count(filename, word):
    f = open(filename, 'r')
    count = 0

    for line in f:
        word = line.split(' ')

        for w in words:
            if word == w.strip():
                count += 1
f.close()

return count

def count_pali(filename):
    f = open(filename, 'r')
    result = {}


    for line in f:
        words = line.split(' ')

        for word in words:
            if is_palindrom(word):
                result[word] = find_count(filname, word.strip())
    f.close()

    return result




