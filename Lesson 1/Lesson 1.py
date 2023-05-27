counter = 0
while counter<3:
    passcode = input("what's the passcode? ")
    is_correct = passcode == "0042"

    if is_correct:
       print("welcome!")
       break
    else:
       print("wrong password")
       counter = counter + 1
