from functools import reduce
def is_palindrom(string):
    if len(string) <=1:
        return True
    if string[0].lower() != string[-1]:
        return False
    return is_palindrom(string[1:len(string)-1])

def count_palindromes(underage,filename):
    with open(filename, 'r') as f:
        personal_data=list(map(lambda line: line.split('\n')[0].split(','),f))

    if underage:
        result=list(filter(lambda person: is_palindrom(person[0])and int(person[1])<18,personal_data))
    else:
        result=list(filter(lambda person: is_palindrom(person[0]),personal_data))

    result_count = len(result)
    return result_count

result_underage = count_palindromes(True,'people.txt')
print(f"Persoanele sub 18 ani cu numele palindrom :{result_underage}")

result_all = count_palindromes(False,'people.txt')
print(f"Toate numele care sunt palindrom:{result_all}")

def test_underage_true():
    assert count_palindromes(True,people.txt) == 2
def test_underage_false():
    assert count_palindromes(False,people.txt) == 6

 #test_underage_true()
 #test_underage_false()