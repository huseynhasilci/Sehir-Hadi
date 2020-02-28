import random
import time


class User:
    def __init__(self):
        self.is_qualified = False
        self.name = ['abbas','busra','ellie','peyami','esma','omer','john','mumin','ebru','betul']
        self.balances = [5.4,3.2,10.2,999.2,1.2,7.2,7.2,0.5,3.2,3.2]
        self.phone_number = ["5577","540","522","502","544","5551","542","541","546","5466"]
        # user data part
    def print_user_stats(self):
        print self.name, self.balances, self.phone_number

class Answer:
    def __init__(self,text=["Black with white stripes.","Levent"],text1=["White with black stripes.","Altunizade"],text2=["Black with red stripes.","Maltepe"],is_correct=[False,False],is_correct1=[True,True],is_correct2=[False,False]):
        self.text = text
        self.text1 =text1                   # to display answers correctness
        self.text2 = text2
        self.answer_no = ["1","2","3"]
        self.is_correct = is_correct
        self.is_correct1 = is_correct1
        self.is_correct2 = is_correct2
        self.num_answering_users = [[],[],[]]
        self.q_no = 1
        self.zipped = zip(self.answer_no,self.text)
    def display(self,display_correctness,display_num_answering_users, q_no):
        corr_ans = Question().correct_answers[q_no]
        self.display_correctness = display_correctness
        self.display_num_answering_users = display_num_answering_users

    def process_answers (self,users, current_user):
        pass
class Question():
    def __init__(self,question_text=["What color are Zebras?","Where was the old Campus of Sehir University?"],answer1=Answer().text,answer2=Answer().text1,answer3=Answer().text2,correct_answers = ["2","2"]):
        self.question_text = question_text
        # self.answers = Answer().text
        self.answer1= answer1      # question and answer attirubutes
        self.answer2=answer2
        self.answer3=answer3
        self.correct_answers = correct_answers
        self.display_correctness = Answer().is_correct
    def add_answer(self,answer_text =Answer().text,answer_text1=Answer().text1,answer_text2=Answer().text2 ,is_correct =Answer().is_correct,is_correct1=Answer().is_correct1,is_correct2=Answer().is_correct2):
        self.answer_text =answer_text
        self.answer_text1 = answer_text1
        self.answer_text2 = answer_text2
        self.is_correct = is_correct            #adding answers and questions
        self.is_correct1 = is_correct1
        self.is_correct2 = is_correct2
        self.add_question = raw_input("Please write your question")
        Question().question_text.append(self.add_question)
        self.add_answer1 = raw_input("Please type your CORRECT answer.")
        Answer().text.append(self.add_answer1)
        Answer().is_correct.append(True)
        self.add_answer2 = raw_input("Please type your INCORRECT answer.")
        Answer().text1.append(self.add_answer2)
        Answer().is_correct1.append(False)
        self.add_answer3 = raw_input("Please type your INCORRECT answer.")
        Answer().text2.append(self.add_answer3)
        Answer().is_correct2.append(False)
    def display(self,question_no=1, display_answers = Answer().text ,display_answers1= Answer().text1,display_answers2=Answer().text2):
        self.question_no = question_no
        self.display_answers = display_answers
        self.display_answer1= display_answers1
        self.display_answers2 = display_answers2
        # self.display_correctness = display_correctness
        for i in range(len(self.question_text)):
            print question_no,self.question_text[i]
            print Answer().answer_no[0],Answer().text[i],Answer().is_correct[i]
            print Answer().answer_no[1],Answer().text1[i],Answer().is_correct1[i]
            print Answer().answer_no[2],Answer().text2[i],Answer().is_correct2[i]
            print "***********************************************************"
            question_no += 1
    def process_answers (self,users, current_user):
        self.users = users
        self.current_user = current_user

class Menu:
    def __init__(self, header):
        self.header = header
        self.menuitems = []

    def display(self, display_header):
        if display_header:
            print self.header
        for i in self.menuitems:
            print i

    def add_menu_item(self,text, number):
        self.menuitems.append(MenuItem(text,number))


class MenuItem:
    def __init__(self,text,number):
        self.text = text
        self.number = number

    def __repr__(self):
        return str(self.number) + ". " + self.text

    def display(self):
        print self.number,self.text

class Game():
    def __init__(self):
        self.dict_of_User_objects = dict()
        for i in range(len(User().name)):
            self.dict_of_User_objects[User().phone_number[i]] = [ User().name[i], User().balances[i] ]
        self.prize = [10000]


    def play(self, user_name,enterence):
        self.enterence=enterence
        self.name = ['abbas','busra','ellie','peyami','esma','omer','john','mumin','ebru','betul']
        print "Welcome", user_name
        print "The prize is", self.prize
        self.total_user = len(user_name)
        # self.choosing_part = raw_input("Choose the correct answer, write 1,2 or 3")
        print "******************Total player", len(self.name),"*********************"
        self.question_list = Question().question_text
        self.answer1 = Answer().text  # q1 and q2  first answers
        self.answer2 = Answer().text1  # q1 and q2 second answers
        self.answer3 = Answer().text2  # q1 and q2 third answers
        self.user_dict = {"5577":("abbas",5.4),
             "540":("busra",3.2),
             "522":("ellie",10.2),
             "502":("peyami",999.2),
             "544":("esma",1.2),
             "5551":("omer",7.2),
             "542":("john",7.2),
             "541":("mumin",0.5),
             "546":("ebru",3.2),
             "5466":("betul",3.2)} #users informations
        self.correct_answers = Question().correct_answers
        self.users_list = self.user_dict.values()[0:]
        self.question_no = 1
        for q_no in range(len(self.question_list)):
            print self.question_no, self.question_list[q_no]
            print Answer().answer_no[0], Answer().text[q_no]
            print Answer().answer_no[1], Answer().text1[q_no]
            print Answer().answer_no[2], Answer().text2[q_no]
            print "***********************************************************"
            self.question_no += 1
            self.save_here1 = []
            self.save_here2 = []
            self.save_here3 = []
            if self.user_dict[self.enterence] in self.users_list:

                self.choosing_part = raw_input("Choose the correct answer, write 1,2 or 3")
                if self.choosing_part == self.correct_answers[q_no]:
                    print "Correct answer."
                    self.save_here2.append(self.enterence)
                else:
                    # print "Wrong answer"
                    self.users_list.remove(self.user_dict[self.enterence])
            for i in range(self.total_user - 1):
                if self.user_dict[self.enterence] in self.users_list:
                    self.users_list.remove(self.user_dict[self.enterence])
                while True:
                    answer_random = random.randint(1, 3)
                    if answer_random == 2:
                        adding_random1 = random.choice(self.users_list)
                        self.save_here2.append(adding_random1)
                        break
                    elif answer_random == 1:
                        removing_users1 = random.choice(self.users_list)
                        self.users_list.remove(removing_users1)
                        self.save_here1.append(removing_users1)
                        break
                    elif answer_random == 3:
                        removing_users2 = random.choice(self.users_list)
                        self.users_list.remove(removing_users2)
                        self.save_here3.append(removing_users2)
                        break
                if self.choosing_part == "2":
                    self.users_list.append(self.user_dict[self.enterence])
            print "*****************Total player.", len(self.save_here2)
            total_user = self.total_user - (len(self.save_here1) + len(self.save_here3))
            print self.answer1[q_no], len(self.save_here1)
            print self.answer2[q_no], len(self.save_here2)  # len(save_here2)
            print self.answer3[q_no], len(self.save_here3)
            print "*********************************"
        prize_share = self.prize[0] / len(self.save_here2)
        for user in range(len(self.save_here2)):
            print self.users_list[user][0], self.users_list[user][1] + prize_share
        print "Going back to log in page"
        Game.login(self)
    def login(self):
        print "Welcome to SEHIR HADI!!"
        self.enterence = raw_input("Please type your phone number in order to sign in:")
        self.user_dict = {"5577":("abbas",5.4),
             "540":("busra",3.2),
             "522":("ellie",10.2),
             "502":("peyami",999.2),
             "544":("esma",1.2),
             "5551":("omer",7.2),
             "542":("john",7.2),
             "541":("mumin",0.5),
             "546":("ebru",3.2),
             "5466":("betul",3.2)}

        if self.enterence == "**":
            print "Going to admin menu..."
            time.sleep(1)
            Game.show_admin_menu(self)
        elif self.enterence == "00":
            print "Goodbye"
            exit(0)
        elif self.enterence in self.dict_of_User_objects:
            Game.play(self, self.user_dict[self.enterence][0], self.enterence)
        else:
            print "Phone number does not exist! Please try again... "
            Game.login(self)

    def show_admin_menu(self):
        # Game.build_admin_menu(self)
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
        # self.huso = raw_input("please push 1 tus")
        self.build_admin_menu()

    def build_admin_menu(self):
        self.admin_menu_builder = raw_input("Please choose your option.")
        # print "admin menu done"
        if self.admin_menu_builder == "1":
            to_select_prize = raw_input("Please enter your prize for the competition.")
            print "Setting prize..."
            time.sleep(1.0)
            del self.prize[0]  # setting prize part
            self.prize.append(int(to_select_prize))
            print "The prize is:", int(to_select_prize)
            print "Going back to admin menu."
            Game.build_admin_menu(self)
        elif self.admin_menu_builder == "2":
            print "Questions loading..."
            questions_shower = Question()
            questions_shower.display()
            Game.build_admin_menu(self)
        elif self.admin_menu_builder == "3":
            print "Adding question menu loading..."
            time.sleep(1)  # to add questions
            self.add_question = raw_input("Please write your question")
            Question().question_text.append(self.add_question) #adding question
            self.add_answer1 = raw_input("Please type your CORRECT answer.")
            Answer().text.append(self.add_answer1)
            Answer().is_correct.append(True)
            Question().correct_answers.append("1")
            self.add_answer2 = raw_input("Please type your INCORRECT answer.")
            Answer().text1.append(self.add_answer2)
            Answer().is_correct1.append(False)
            self.add_answer3 = raw_input("Please type your INCORRECT answer.")
            Answer().text2.append(self.add_answer3)
            Answer().is_correct2.append(False)
            Game.build_admin_menu(self)
        elif self.admin_menu_builder == "4":
            print "Deleting question menu loading..."
            delete = raw_input("Which index do you want to delete.")
            for i in range(len(Question().question_text)):
                if int(delete) - 1 == i:
                    Question().question_text.pop(i)
                    Answer().text.pop(i)
                    Answer().text1.pop(i)  # deleting questions
                    Answer().text2.pop(i)
                    Answer().is_correct.pop(i)
                    Answer().is_correct1.pop(i)
                    Answer().is_correct2.pop(i)
            Game.build_admin_menu(self)
        elif self.admin_menu_builder == "5":
            print "Going to users data"
            time.sleep(1)  # to see users data
            a = Game().dict_of_User_objects
            for i in a.items():
                print i
            Game.build_admin_menu(self)
        elif self.admin_menu_builder == "6":
            print "Logging out from the admin menu..."
            time.sleep(1)  # to start the game
            class1 = Game()
            class1.login()
            #to get into game
        else:
            print "This is not a valid option please write correct option."
            self.build_admin_menu()

    def distribute_prize(self):
        print "distribute"
class1 = Game()
class1.login()