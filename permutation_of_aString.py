#Find all the possible permutations of a string

def print_all_permutations(ques, answer):
    if len(ques) == 0:
        print(answer)
    for i in range(0, len(ques)):
        ch = ques[i]
        lp = ques[0:i]
        rp = ques[i+1:]
        ros = lp + rp
        print_all_permutations(ros, answer+ch)

s1 = "ABC"
print_all_permutations(s1, "")
