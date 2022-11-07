def lcounter(text,letter):
    count=0
    for i in range(0,len(text),1):
        if text[i]==letter:
            count+=1
    return count