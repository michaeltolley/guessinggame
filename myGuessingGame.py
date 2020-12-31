import random

#magicNumber = 34
winner = False
print("In this game you will choose the range fo the numbers you can choose from.")
lowerNumber = int(input("Enter lower number here:  "))
higherNumber = int(input("Enter higher number here:  "))

while higherNumber < lowerNumber:
    print("Put in a higher number.")
    higherNumber = int(input("Enter higher number here:  "))

magicNumber = random.randint(lowerNumber,higherNumber)

print("Guess a number between "+ str(lowerNumber) + " through " + str(higherNumber) +". You have 15 tries.")
#print("Pick a number between 1 and 2, to choose the number you will guess ")

for tries in range(1, 16, 1):
    answer = int(input("Enter number here:  "))

    if answer == magicNumber:
        winner = True
        print("congratulations you got it correct!")
        if tries < 6:
            print("you earned a gold medal!")
        elif tries < 11:
            print("you earned a silver medal!")
        elif tries < 15:
            print("you earned a bronze medal!")
        break
    else:
        if magicNumber > answer: 
            print("incorrect, you have used "+ str(tries) +" tries. Try a higher number.")
        else:
            print("incorrect, you have used "+ str(tries) +" tries. Try a lower number.")

if winner == False:
    print("sorry, you didn't get any right.")