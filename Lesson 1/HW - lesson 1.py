import random
answer = random.randint(1, 10)
print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")

counter = 0
while counter < 3:
    your_answer = int(input("Do ban biet to dang nghi den so nao? "))
    is_correct = answer
    if your_answer == is_correct:
        print("Dung roi!")
        break
    else:
        if your_answer < answer:
            print("Thap qua!")
        else:
            print("Cao qua!")
            counter = counter + 1
