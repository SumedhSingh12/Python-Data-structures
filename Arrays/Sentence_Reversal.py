def reverse_sent(sentence):
    words = []
    word = ""
    for i in range(len(sentence)):
        if sentence[i] != " ":
            word += sentence[i]
            if i+1 < len(sentence) and sentence[i+1] == " ":
                words.append(word)
                word = ""
    for i in range(len(words)):
        word += (words[len(words)-(1+i)])
        word += " "
    return(word)