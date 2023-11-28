import random
continuee = True
while continue:
    print("You rolled : ",random.randint(1,6))
    print("Roll again? Y/N")
    continuee = "Y" in input()