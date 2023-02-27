# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:UoW - w1870622 / IIT - 20200883

# Date:  2021 / 12 / 06

#Question 01 - Part 01



#entering to the student section

#Initializing Variables
pass_credits = 0
defer_credits = 0
fail_credits = 0

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

#Gettting Inputs       
pass_credits = int(input("Please Enter Your credits at pass : "))
defer_credits = int(input("Please enter your credit at defer: "))
fail_credits = int(input("Please enter your credit at fail : "))


progression_out(pass_credits, defer_credits)
