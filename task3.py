n  = int(input("Total voters : "))
can1 = "a"
total_a_vote = 0
total_b_vote = 0
total_c_vote = 0
invalid_vote = 0
can2 = "b"
can3 = "c"
for i in range(1 , (n + 1)):
    user_age = int(input("\nEnter your age :"))
    if(user_age >= 18):
        choose_candidate = input("Choose the Candidate : ").lower()
        if(choose_candidate == "a"):
            total_a_vote = total_a_vote + 1
        elif(choose_candidate == "b"):
            total_b_vote = total_b_vote + 1
        elif (choose_candidate == "c"):
            total_c_vote = total_c_vote + 1
        else:
            invalid_vote = invalid_vote + 1
if(total_a_vote > total_b_vote and total_a_vote > total_c_vote):
    print("A is Winner")
elif(total_b_vote > total_a_vote and total_b_vote > total_c_vote):
    print("B is Winner")
elif(total_c_vote > total_a_vote and total_c_vote >  total_b_vote):
    print("C is Winner")
else:
    if total_a_vote == total_b_vote == total_c_vote:
        print("Tie Eachother A , B and C")

    elif total_a_vote == total_b_vote:
        print("Tie Candidate A and Candidate B")

    elif total_b_vote == total_c_vote:
        print("Tie Candidate B and Candidate C")

    elif total_a_vote == total_c_vote:
        print("Tie  Candidate A and Candidate C")

print("Candidate a :",total_a_vote)
print("Candidate b :",total_b_vote)
print("Candidate c :",total_c_vote)
print("Invalid Votes : ",invalid_vote)