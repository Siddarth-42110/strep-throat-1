def find_prob(a,b):
    if a ==1:
            prob_a = 0.2
            if b==1:
                  prob_bga = 0.85
            elif b==2:
                  prob_bga = 0.15
            else:
                  print("Invalid choice")
            prob_a_and_b = prob_a*prob_bga
            print("Probability of b given a:", prob_bga)
            print("Probability of both events occuring:", prob_a_and_b)
    elif a==2:
            prob_a = 0.8
            if b==1:
                    prob_bga = 0.02
            elif b==2:
                   prob_bga = 0.98
            else:
                   print("Invalid choice")
            prob_a_and_b = prob_a*prob_bga
            print("Probability of b given a:", prob_bga)
            print("Probability of both events occuring:", prob_a_and_b)
    else:
           print("invalid choice")
print("let's calculate probability. please enter choices for the events...")

print("person has a strep throat? \n 1. yes \n 2. no")
a = int(input("enter your choice (1/2):"))

print("person has tested positive? \n 1. yes \n 2. no")
b = int(input("enter your choice (1/2):"))

print("probabilities for event a and b:")
find_prob(a,b)