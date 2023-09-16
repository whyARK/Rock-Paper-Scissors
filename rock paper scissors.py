import random

user_count = 0
bot_choice = random.choice(["камінь","ножниці","папір"])
bot_count = 0
while user_count != 3 or bot_count != 3:
    user_choice = input("камінь,ножниці чи папір?")
    bot_choice = random.choice(["камінь","ножниці","папір"])

    if user_choice == "камінь" and bot_choice == "камінь":
        user_count += 0
        print("вибір бота -",bot_choice)
        print("гравець -",user_count)
        print("бот -",bot_count,"\n")
    if user_choice == "камінь" and bot_choice == "ножниці":
        user_count += 1
        print("вибір бота -",bot_choice)
        print("гравець -",user_count)
        print("бот -",bot_count,"\n")
    if user_choice == "камінь" and bot_choice == "папір":
        bot_count += 1
        print("вибір бота -",bot_choice)
        print("гравець - ",user_count)
        print("бот -",bot_count,"\n")


    if user_choice == "ножниці" and bot_choice == "камінь":
        bot_count += 1
        print("вибір бота -",bot_choice)
        print(user_count)
        print(bot_count)
    if user_choice == "ножниці" and bot_choice == "ножниці":
        user_count += 0
        print("вибір бота -",bot_choice)
        print(user_count)
        print(bot_count)
    if user_choice == "ножниці" and bot_choice == "папір":
        user_count += 1
        print("вибір бота -",bot_choice)
        print(user_count)
        print(bot_count)


    if user_choice == "папір" and bot_choice == "камінь":
        user_count += 1
        print("вибір бота -",bot_choice)
        print("гравець -",user_count)
        print("бот -",bot_count)
    if user_choice == "папір" and bot_choice == "ножниці":
        bot_count += 1
        print("вибір бота -",bot_choice)
        print("гравець -",user_count)
        print("бот -",bot_count)
    if user_choice == "папір" and bot_choice == "папір":
        user_count += 0
        print("вибір бота -",bot_choice)
        print("гравець -",user_count)
        print("бот -",bot_count)

    if user_count == 3:
        print("You won")
        break
    if bot_count == 3:
        print("You lost")
        break