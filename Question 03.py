# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID:UoW - w1870622 / IIT - 20200883

# Date:  2021 / 12 / 08

#Question 03

#entering the staff optional extension section listing the outcomes

#Initializing Variables
pass_credits = 0
defer_credits = 0
fail_credits = 0
total = 0

stop = " "

#elements list of histogram
Progress = []
Trailer = []
Retriever = []
Excluded = []

finished_items = []

#elements of table
elements = [Progress, Trailer, Retriever, Excluded]


list_items = [[120, 0, 0], [100, 20, 20], [100, 0, 20], [80, 20, 20], [60, 40, 20],
        [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]


#elements list of histogram
Progress = []
Trailer = []
Retriever = []
Excluded = []

#range of valid inputs
valid_range = [0 , 20, 40, 60, 80, 100, 120]



#progression outcome - function
def progression_out(pass_credits,defer_credits):
    test = "";
    
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
    return test
        

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
        test = ""
        if total != 120:
            print("Total Incorrect")
            validity()
            break
        else:
            test = progression_out(pass_credits, defer_credits)
            finished_items.append([test,pass_credits,defer_credits,fail_credits])
            break



#function for listing

def valid(list_items):
    global pass_credits, defer_credits, fail_credits
    for i in range(len(list_items)):
        pass_credits = list_items[i][0]
        defer_credits = list_items[i][1]
        fail_credits = list_items[i][2]
        progression_out()


#for creating the histogram - vertical

def histo_create1():
    print("\n-----------------------------------------------------")
    print("Vertical Histogram")
    histo_tab_create(elements)
    print(outcomes, "outcomes in total.")
    print("\n-----------------------------------------------------")




#function for the histogram table

def histo_tab_create(elements) :
    global outcomes
    print("Progress", len(Progress), " ", "Trailer", len(Trailer), " ", "Retriever", len(Retriever), " ", "Excluded", len(Excluded))
    outcomes = len(Progress) + len(Trailer) + len(Retriever) + len(Excluded)
    for i in range(outcomes):
        for x in elements:
            if len(x) > 0:
                print("    ", "*", "    ", end="")
                x.pop()
            else:
                print("    ", " ", "    ", end="")
        print()


#for creating the histogram - Horizontal

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


#for final list to display
def hist():
    for i in finished_items:
        print(i[0]," - ",i[1],",",i[2],",",i[3])




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
hist()
histo_create()
histo_create1()
histo_tab_create(elements)
