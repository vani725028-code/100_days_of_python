# 4. Create a list containing the lengths of each word in a sentence.

sentence = 'i will complete my chalange'
list = [len(word) for word in sentence.split()]
print(list)