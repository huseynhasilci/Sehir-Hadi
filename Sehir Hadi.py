import time
import random
print "Welcome to SEHIR HADI!!"
prize = [10000]
question_list =["--- Q1: What color are Zebras? ---","--- Q2: Where was the old Campus of Sehir University? ---"] #question list
answer1 = ["ans 1. Black with white stripes.","ans 1. Levent"] #q1 and q2  first answers
answer2 = ["ans 2. White with black stripes.","ans 2. Altunizade"] #q1 and q2 second answers
answer3 = ["ans 3. Black with red stripes.","ans 3. Maltepe"] #q1 and q2 third answers
true_or_false1 = [False,False]
true_or_false2 = [True,True]
true_or_false3 = [False,False]
correct_answers = ["2","2"]
user_dict = {"5577":("abbas",5.4),
             "540":("busra",3.2),
             "522":("ellie",10.2),
             "502":("peyami",999.2),
             "544":("esma",1.2),
             "5551":("omer",7.2),
             "542":("john",7.2),
             "541":("mumin",0.5),
             "546":("ebru",3.2),
             "5466":("betul",3.2)} #users informations
users_list = user_dict.values()[0:]
def game(n,enterence):
    print n
    print "The game will start soon."
    print "The prize is",prize
    total_user = len(users_list)
    print "******************Total player",len(users_list)
    for q_no in range(len(question_list)):
        print question_list[q_no]
        print answer1[q_no]             #to write answers orderly
        print answer2[q_no]
        print answer3[q_no]
        save_here1 = []
        save_here2 = []
        save_here3 = []

        if user_dict[enterence] in users_list:
            choosing_part = raw_input("Choose the correct answer, write 1,2 or 3")
            if choosing_part == correct_answers[q_no]:
                print "Correct answer."
                save_here2.append(enterence)
            else:
                print "Wrong answer"
                users_list.remove(user_dict[enterence])
                print users_list
        for i in range(total_user-1):
            if user_dict[enterence] in users_list:
                users_list.remove(user_dict[enterence])
            while True:
                answer_random = random.randint(1,3)
                if answer_random == 2:
                    adding_random1 = random.choice(users_list)
                    save_here2.append(adding_random1)
                    break
                elif answer_random == 1:
                    removing_users1 = random.choice(users_list)
                    users_list.remove(removing_users1)
                    save_here1.append(removing_users1)
                    break
                elif answer_random == 3:
                    removing_users2 = random.choice(users_list)
                    users_list.remove(removing_users2)
                    save_here3.append(removing_users2)
                    break
            if choosing_part == "2":
                users_list.append(user_dict[enterence])
        print "*****************Total player.",len(save_here2)
        total_user = total_user - (len(save_here1) + len(save_here3))
        print answer1[q_no],len(save_here1)
        print answer2[q_no],len(save_here2)#len(save_here2)
        print answer3[q_no],len(save_here3)
        print "*********************************"
    prize_share = prize[0] / total_user
    # print users_list[i][enterence][0],users_list[i][enterence][1] + prize_share
    #print user_dict[enterence][0],user_dict[enterence][1]+prize_share

    for user in range(len(save_here2)):
        print users_list[user][0],users_list[user][1]+prize_share
    print "Going back to log in page"
    firstRun()
def users_data():
    for i in user_dict.items():
        print i  # to see users informations
    print "Going back to admin menu..."
    time.sleep(1)
    admin_menu()
def deleting_question_part():
    delete = raw_input("Which index do you want to delete.")
    for i in range(len(question_list)):
        if int(delete) - 1 == i:
            question_list.pop(i)
            answer1.pop(i)
            answer2.pop(i)             # deleting questions
            answer3.pop(i)
            true_or_false1.pop(i)
            true_or_false2.pop(i)
            true_or_false3.pop(i)
    print "Question is deleting..."
    time.sleep(1)
    print "Going back to to admin menu..."
    admin_menu()
def adding_question_part():
    adding_question = raw_input("Write your new question.")
    question_list.append(adding_question)
    adding_answer1 = raw_input("Write your correct answer.")
    answer1.append(adding_answer1)
    correct_answers.append("1")
    true_or_false1.append(True)
    adding_answer2 = raw_input("Write your incorrect answer.")
    answer2.append(adding_answer2)
    true_or_false2.append(False)
    adding_answer3 = raw_input("Write your incorrect answer.")
    answer3.append(adding_answer3)
    true_or_false3.append(False)                                            #adding question to the qustion list
    print "Adding question to the data base..."
    time.sleep(1)
    print "Done"
    print "Going back to Admin menu."
    admin_menu()

def questions():
    for i in range(len(question_list)):
        print question_list[i]
        print answer1[i],true_or_false1[i]
        print answer2[i],true_or_false2[i]
        print answer3[i],true_or_false3[i]         # to see the questions answers and which answer is true or false
    print "Going back to Admin menu..."
    time.sleep(1)
    admin_menu()

def admin_menu():
    print"""
    *******************
    1 - Set prize for the next competition. If you want to select the prize pool press 1.
    2 - Display questions for the next competition. If you want to show questions for the next competition press 2.
    3 - Add new question to the next competition. If you want to add new question to the next competition press 3.
    4 - Delete a question from the next competition. If you want to delete a question from the next competition press 4.
    5 - See users data. If you want to see users data press 5.
    6 - Log out. If you want to log out from the admin menu and start the competition press 6.
    *******************
    """

    admin_menu_controller = raw_input("Please select your step to do in admin menu.")
    if  admin_menu_controller == "1":
        to_select_prize = raw_input("Please enter your prize for the competition.")
        print "Setting prize..."
        time.sleep(1.0)
        del prize[0]                    #setting prize part
        prize.append(int(to_select_prize))
        print "The prize is:", int(to_select_prize)
        print "Going back to admin menu."
        admin_menu()
    elif admin_menu_controller == "2":
         print "Questions loading..."
         time.sleep(1)
         questions()                    #to see the questions
    elif admin_menu_controller == "3":
         print "Adding question menu loading..."
         time.sleep(1)              #to add questions
         adding_question_part()
    elif admin_menu_controller == "4":
         print "Deleting question menu loading..." #to delete questions
         time.sleep(1)
         deleting_question_part()
    elif admin_menu_controller == "5":
         print "Going to users data"
         time.sleep(1)                  #to see users data
         print users_data()
    elif admin_menu_controller == "6":
        print "Logging out from the admin menu..."
        time.sleep(1)                       # to start the game
        firstRun()
    else:
        print "This is not a valid option please write correct option."
        admin_menu()
def firstRun():
    enterence = raw_input("Please type your phone number in order to sign in:")
    if enterence == "**":
        print "Going to admin menu..."
        time.sleep(1)
        admin_menu()
    elif enterence == "00":     # if you want to chane something in the game questions answers or deleting something or you can start the game directly
        print "Goodbye"
        exit(0)
    elif enterence in user_dict:
        print "Welcome " , game(user_dict[enterence][0],enterence)
    else:
        print "Phone number does not exist! Please try again... "
        firstRun()

firstRun()






