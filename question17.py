# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

total = 0
while True:
    T = input()
    if not T:
        print(total)
        break
    T = T.strip().split(" ")
    if T[0] == "D":
        total += int(T[1])
    elif T[0] == "W":
        total -= int(T[1])

account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()
