print("Hello")
name=input("Enter your name:")
print("Welcome",name)
print("Let's go")
score =0
print("Welcome to the Quize!")
answer=input("What is the capital of India?")
if answer=="new delhi":
    print("Correct answer!")
    score+=1
else:
    print("Wrong answer")
print("Your Score is:",score)
answer=int(input("5+5="))
if answer==10:
    print("correct answer!")
    score+=1
else:
    print("wrong answer")
print("Your Score is:",score)
answer=input("python is a structured programming language?(yes/no)")
if answer=="no":
    print("Correct answer!")
    score+=1
else:
    print("Wrong answer")
print("Your Score is:",score)
answer=input("Who is the founder of python:")
if answer=="guido van rossum":
    print("Correct answer!")
    score+=1
else:
    print("Wrong answer")
print("Your Score is:",score)
answer=input("For loop is a finite loop of the python? (yes/no)")
if answer=="yes":
    print("Correct answer!")
    score+=1
else:
    print("Wrong answer")
print("Your final Score is:",score,"/5")
if score==5:
    print("excellent!")
elif score>=3:
    print("Good job!")
else:
    print("Keep practicing!")
again=input("Play again? (yes/no)")    
while again=="yes":
    print("Let's go")
    score =0
    print("Welcome to the Quize!")
    answer=input("What is the capital of India?")
    if answer=="new delhi":
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer")
    print("Your Score is:",score)
    answer=int(input("5+5="))
    if answer==10:
        print("correct answer!")
        score+=1
    else:
        print("wrong answer")
    print("Your Score is:",score)
    answer=input("python is a structured programming language?(yes/no)")
    if answer=="no":
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer")
    print("Your Score is:",score)
    answer=input("Who is the founder of python:")
    if answer=="guido van rossum":
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer")
    print("Your Score is:",score)
    answer=input("For loop is a finite loop of the python? (yes/no)")
    if answer=="yes":
        print("Correct answer!")
        score+=1
    else:
        print("Wrong answer")
    print("Your final Score is:",score,"/5")
    if score==5:
        print("excellent!")
    elif score>=3:
        print("Good job!")
    else:
        print("Keep practicing!")
    percentage=(score/5)*100
    print("Percentage:",percentage,"%")
    print("Thank You!")
    exit()
