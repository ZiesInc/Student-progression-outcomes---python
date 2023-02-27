# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:UoW - w1870622 / IIT - 20200883

# Date:  2021 / 12 / 08

#Question 01 - Part 03

#entering the staff section for histogram

#Initializing Variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
total =0

stop = " "

#elements list of histogram
Progress = []
Trailer = []
Retriever = []
Excluded = []

#range of valid inputs
valid_range = [0 , 20, 40, 60, 80, 100, 120]



#progression outcome - function
def progression_out(pass_credits,defer_credits):
    if pass_credits == 120:
        print("Progress")
        Progress.append(0)
    elif pass_credits == 100:
        print("Progress (module trailer)")
        Trailer.append(0)
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
        Retriever.append(0)
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
        Retriever.append(0)
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
        Retriever.append(0)
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
        Excluded.append(0)
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
        Retriever.append(0)
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
        Excluded.append(0)
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
        Retriever.append(0)
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")
        Excluded.append(0)

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
        

#for creating the histogram

def histo_create():
    print("\n-----------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress", len(Progress), " :", "*" * len(Progress))
    print("Trailer", len(Trailer), "  :", "*" * len(Trailer))
    print("Retriever", len(Retriever), ":", "*" * len(Retriever))
    print("Excluded", len(Excluded), " :", "*" * len(Excluded))
    outcomes = len(Progress) + len(Trailer) + len(Retriever) + len(Excluded)
    print(outcomes, "outcomes in total.")
    print("\n-----------------------------------------------------")

#function for re-runinng

def re_run():
    global stop
    while True:
        try:
            stop = str(input("Would you like to enter another set of data? \n Enter 'y' for yes or 'q' to quit and view results: "))
        except:
            print("-Please enter 'y' or 'q'-")
        if stop == "q":
            histo_create()
            break
        elif stop == "y":
            validity()
        else:
            print("-Please enter 'y' or 'q'-")
            
    return stop



validity()
re_run()
