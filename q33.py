# 13. Find the frequency of every element in a list.
n = input("Enter string:")
freq ={}
for word in n.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word] = 1
print(freq)         


