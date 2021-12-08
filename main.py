def corresponding_parenthesis(text):
    result = text.count("(") - text.count(")")
    if result == 0:
        return ""
    else:
        word = ''
        if result>0:
            print(result)
            for i in range(result):
                word+='('
        if result <0:
            result = result * - 1
            for i in range(result):
                word+=')'
        return word

def remove_more_than_two_repetitions(text):
    text = text.split()
    res = []
    for index,word in enumerate(text):
        res.append([])
        for letter_index,letter in enumerate(word):
            if letter_index >= 2:
                if(word[letter_index-1] != letter or word[letter_index-2] != letter):
                    res[index].append(letter)
            if letter_index < 2:
                res[index].append(letter)
        res[index] = "".join(res[index])
    return " ".join(res)


remove_more_than_two_repetitions("aaaabbbbaacaaaxxxxii")
# aabbaacaaxxii