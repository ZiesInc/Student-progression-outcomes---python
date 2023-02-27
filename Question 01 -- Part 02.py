# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:UoW - w1870622 / IIT - 20200883

# Date:  2021 / 12 / 06

#Question 01 -Part 02


#entering the student validation section - program to student validation section

#Initializing Variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
total=0

#range of valid inputs
valid_range = [0 , 20, 40, 60, 80, 100, 120]



#progression outcome - function
def progression_out(pass_credits, defer_credits):
    if pass_credits == 120:
        print("Progress")
    elif pass_credits == 100:
        print("Progress (module trailer)")
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")

#validation - function
        
def validity():
    global pass_credits
    while True:
        try:
            pass_credits = int(input("Please enter your credits at Pass: "))
        except ValueError:
            print("Integer Required")
            continue
        else:
            if pass_credits not in valid_range :
                print("Out of Range")
            elif pass_credits in valid_range:
                break
            
    while True:
        try:
            defer_credits = int(input("Please enter your credit at Defer: "))
        except ValueError:
            print("Integer Required")
            continue
        else:
            if defer_credits not in valid_range:
                print("Out of Range")
            elif defer_credits in valid_range:
                break
            
    while True:
        try:
            fail_credits = int(input("Please enter your credit at Fail: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if fail_credits not in valid_range:
                print("Out of Range")
            elif fail_credits in valid_range:
                break

    while True:
        total = pass_credits + defer_credits + fail_credits
        if total != 120:
            print("Total Incorrect")
            validity()
            break
        else:
            progression_out(pass_credits, defer_credits)
            break
        


validity()
