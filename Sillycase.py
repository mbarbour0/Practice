def sillycase(word):
    return_list = []
    for i in word[:int(len(word)/2)]:
        return_list.append(i.lower())
    for i in word[int(len(word)/2):]:
        return_list.append(i.upper())
    final_list = ''.join(return_list)
    return final_list
print(sillycase('TeSt Word TrY to CaMel CasEmE'))