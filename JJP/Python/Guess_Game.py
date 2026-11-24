import sys

guess_number = 23
count = 1
    
number = int(input("Guess a number from (1-100): "))
if (number==guess_number) :
    print("You entered the guess number correctly")
    print("Count = ",count)
    sys.exit()
  
while number != guess_number:
    number = int(input("Guess a number from (1-100): "))
    count += 1
    if (number==guess_number) :
        print("You entered the guess number correctly");
        print("Count",count)
        break
