#EASY, MEDIUM  AND HARD LEVEL PARAGRAPHS
easy= """An immense mausoleum of white marble, built in ____1____ between
1631 and 1648 by order of the Mughal emperor ____2____  in memory of his 
favourite wife ____3____ , the Taj Mahal is the jewel of Muslim art in
____4____  and one of the universally admired masterpieces of the world's 
heritage. It is one of the Seven ____5____ of the world """

#answer list 
easy_answers=["agra","shah jahan","mumtaz mahal","india","wonders"]



medium= """Tesla Motors, American electric- ____1____ manufacturer.
It was founded in 2003 by American entrepreneurs ____2____ , Martin Eberhard and Marc Tarpenning
and was named after Serbian American inventor ____3____ Tesla. Tesla Motors was formed to
develop an ____4____ sports car. The company's HQ is in ____5____ . """

#answer list 
medium_answers=["automobile","elon musk","nikola","electric","california"]



hard= """Tata Motors Limited (formerly TELCO, short for Tata ____1____ and Locomotive Company) headquartered
in ____2____ , is an Indian multinational automotive manufacturing company and a member
of the ____3____  Group. Its products include passenger cars, trucks, vans, coaches, buses, sports cars, 
construction equipment and military vehicles.Tata Motors has been ranked 5th in 2017 Responsible Business Rankings 
developed by IIM Udaipur.Tata Motors entered the passenger vehicle market in 1991 with the launch of the Tata ____4____ . 
Tata Motors acquired the South Korean truck manufacturer Daewoo Commercial Vehicles Company in 2004 and 
purchased British luxury brands ____5____ and Land Rover from Ford in 2008. """

#answer list 
hard_answers=["engineering","mumbai","tata","sierra","jaguar"]



def game_difficulty():
    ''' the user is prompted to enter the level of difficulty at which he wants to play
    the function prints the levels available and asks the user to enter one of them or exit the game'''

    difficulty = raw_input("""\n    Welcome to the Game
    Enter 1,2,3 based on difficulty you want to play at:
    easy for easy (level 1)
    medium for medium (level 2)
    hard for hard (level 3)
    exit for exit\n""")
    if difficulty == "easy":
        
        begin_game(easy, easy_answers)
    
    elif difficulty == "medium":
        
        begin_game(medium, medium_answers)
    
    elif difficulty == "hard":
        
        begin_game(hard, hard_answers)

    elif difficulty == "exit":
        exit()
    
    else:
        print '\nPlease enter from one of the choices mentioned above!!\n'
        
        game_difficulty()


def begin_game(question, answer_tray):
    '''this function takes the question and the corresponding answer list as the input

    arguments:
    question-- the question para that follows according to the difficulty level chosen by the user
    answer tray--- the answers of the chosen paragraph

    output:
    the function begins the game \, evaluates each answer and the prints congratulations at the end
    when all the questions have been answered correctly'''
    blanks_total = 5
    blank_index_no = 0

    while blank_index_no < blanks_total:
        print question
        print "\nWrite your answer for blank number",str(blank_index_no + 1)," :"," "
        user_answer = raw_input().lower()
        if user_answer == answer_tray[blank_index_no] :
            #checking is users answer matches with the actual answer

            question = update(question,user_answer,blank_index_no)
            blank_index_no = blank_index_no + 1   
            '''incrementing blank_no_index to move to the next blank, after 
            the previous blank has been corrrectly answered'''
            
        else:
            print '\nWrong Answer. Try Again\n\n\n\n\n'
            
    print question
    print "\n\n*****************Congratulations on completing the game*****************\n\n"
    game_difficulty()
 



def update(question,user_answer,blank_index_no):
    '''to update the question paragraph. After the anser has been checked the blank is replaced 
     the answer entered by the user

     arguments:
     question-- based on difficulty level
     user_answer---answer entered by the user
     blank_index_no-- the blank for which the answer has been submitted


     output:
     it returns the question paragraph after replacing the blank with the corrresponding  answer'''

    question = question.split()
    location = question.index("____" + str(blank_index_no + 1) + "____")
    question[location] = question[location].replace('____'+str(blank_index_no + 1)+'____',user_answer)
    question = ' '.join(question)
    print "Your answer is correct\n\n\n"   
    return question


game_difficulty()



