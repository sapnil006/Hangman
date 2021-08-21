import game_data
import random
import art

print(art.logo)
x = game_data.data

choicea = random.choice(x)
choiceb = random.choice(x)
if choicea == choiceb:
    choiceb = random.choice(x)
# print(f"{choice1}\n\n and {choice2}\n\n")
flag = True
score = 0
while flag:

    print(f"compare A: {choicea['name']}, a {choicea['description']}, from {choicea['country']}")
    print(f"{art.vs}\n")
    print(f"compare B: {choiceb['name']}, a {choiceb['description']}, from {choiceb['country']}\n\n")
    choice = input("Who has more followers? Type 'A' or 'B':").lower()

    if choice == "a":
        if choicea['follower_count'] > choiceb['follower_count']:
            score = score + 1

            print(art.logo)
            print(f"You're right! Current score: {score}")
            if len(game_data.data) == 1:
                print("WINNER!")
                flag = False
            x.remove(choiceb)
            print(len(game_data.data))
            choiceb = random.choice(x)
            if choicea == choiceb:
                choiceb = random.choice(x)

        else:

            print(art.logo)
            print(f"game over,your final score is {score}")
            flag = False
    elif choice == "b":
        if choiceb['follower_count'] > choicea['follower_count']:
            score = score + 1

            print(art.logo)
            print(f"You're right! Current score: {score}")
            if len(game_data.data) == 1:
                print("WINNER!")
                flag = False
            x.remove(choicea)
            print(len(game_data.data))
            choicea = choiceb
            choiceb = random.choice(x)
            if choicea == choiceb:
                choiceb = random.choice(x)

        else:

            print(art.logo)
            print(f"game over,your final score is {score}")
            flag = False
    else:
        print("wrong choice")
        flag = False
