def word_count(arg1):
    word_list = arg1.lower().split()
    result_dict = dict()
    for word in word_list:
        if word in result_dict.keys():
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict

print(word_count("Hi, my name is is is"))