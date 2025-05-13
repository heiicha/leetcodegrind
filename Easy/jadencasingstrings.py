def to_jaden_case(string):
    words = []
    for word in string.split():
        words.append(word.capitalize())
    print(' '.join(words))

to_jaden_case("How can mirrors be real if our eyes aren't Real")