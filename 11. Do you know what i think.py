whatImThinking = "book"
your_guess = ""
count = 0
is_right = False
while your_guess != whatImThinking and count <3:
    your_guess = input("Do you know, what i'm thinking now?\nguess: ")
    count+=1
    if(your_guess == whatImThinking):
        is_right = True
        break
if(is_right):
    print("You guessed right!")
else:
    print("Limt crossed!")

