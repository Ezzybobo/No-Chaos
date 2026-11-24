word = input("Enter a word: ")
original_word = word
reversal =""

for index in range(len(word)-1,-1,-1) :
    reversal+=word[index]
    
if (reversal==original_word):
	print(original_word," is a Palindrome")
else :
	print(original_word," is not a Palindrome")
