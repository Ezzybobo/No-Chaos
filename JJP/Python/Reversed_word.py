word = input("Enter a word: ")
reversal =""

for index in range(len(word)-1,-1,-1) :
    reversal+=word[index]
print(reversal)
    

