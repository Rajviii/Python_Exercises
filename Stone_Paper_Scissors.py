# Stone Paper Scissors
import random
print("1. for Stone")
print("2. for Paper")
print("3. for Scissors")

#c = int(input("Enter your Choice"))
#c = random.sample(range(0,4))
score = 0
while(score<5):
    h = int(input("Enter Your Choice: "))
    print(h)
    c = random.randint(1, 3)
    print("Computer's choice: ",c)
    if c ==1 and h == 1:
        print("Tied")
        continue
    elif c == 1 and h == 2:
        print("You Won!!")
        score = score + 1
        print("Score = ",score)
        continue
    elif c == 1 and h == 3:
        print("You Loss")
        continue
    elif c == 2 and h == 1:
        print("You Won!!")
        score = score + 1
        print("Score = ",score)
        continue
    elif c == 2 and h == 3:
        print("You Loss")
        continue
    elif c == 3 and h == 1:
        print("You Loss")
        continue
    elif c == 3 and h == 2:
        print("You Won!!")
        score = score + 1
        print("Score = ",score)
        continue
    elif c == 3 and h == 3:
        print("Tied")
        continue