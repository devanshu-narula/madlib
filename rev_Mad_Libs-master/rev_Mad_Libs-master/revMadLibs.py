# 3 Questions on the basis of increasing difficulty
data={
    'easy':{
        'phrase':'''
        In Game of __1__, Tyrion is introduced as the third and youngest child
        of wealthy and powerful __2__ Lannister, the former __3__ of the King, and
        Joanna Lannister, who dies giving birth to him. Tyrion's elder sister
        __4__ is the Queen of Westeros by virtue of her marriage to King Robert
        Baratheon, and brother __5__ is one of the Kingsguard, the royal bodyguard.
        ''',
        'answers':['thrones','tywin','hand','cersei','jamie']},

    'medium':{
        'phrase':'''
        In Game of Thrones, Daenerys is sold off by her __1__, Viserys and Illyrio
        Mopatis to marry Khal Drogo, a __2__ warlord, in exchangefor an army for
        Viserys. At that time, Daenerys befriends Jorah __3__, an exiled Westerosi
        knight, and is given three petrified __4__ eggs as a wedding gift. Though
        initially terrified of Drogo, the marriage turns out to be a happy one,
        and Daenerys grew to love him and began to take to __5__ customs,
        finding strength and determination for the first time.
        ''',
        'answers':['brother','dothraki','mormont','dragon','dothraki']},

    'hard':{
        'phrase':'''
        In Game of Thrones, __1__ Snow is introduced as the 14-year-old bastard
        son of Eddard "Ned" __2__, Lord of __3__, and half-brother to
        Robb, Sansa, Rickon, Bran and __4__. Jon is described as having strong
        Stark features with a lean build, long face, dark brown hair and grey
        eyes. Jon is resented by Ned's wife __5__, who views him as a
        constant reminder of Ned's infidelity.
        ''',
        'answers':['jon','stark','winterfell','arya','catelyn']}
    }

# Following functions handles the gameplay
def play_game(updated_que,blank_number):
    '''The functions handle the question statement updation corresponding to
    which blank is being answered.
    updated_que:    question statement after every response of user.
    blank_number:   the blank user is currently giving the response of.'''
    total_blanks=5
    while blank_number<=total_blanks:
        print '\n'+str(blank_number)+'\n'
        ans=raw_input(updated_que['phrase']).lower()
        if ans==updated_que['answers'][blank_number-1]:# this conditions check if the answer is correct
            updated_que['phrase']=updated_que['phrase'].replace('__'+str(blank_number)+'__',ans)# updating the question statement
            blank_number=blank_number+1
            play_game(updated_que,blank_number)# proceeding to next blank
        elif ans=='quit':
            exit()
        else:
            print '\nTry Again\n'
            play_game(updated_que,blank_number)# handling the wrong answer response
    print '\n'+updated_que['phrase']+'\nThanks for playing. You may exit by entering quit or choose another question.\n'
    start_game()


def start_game():
    '''The game starts here'''
    level=raw_input('\nWhich question you want to go for?\n easy, medium or hard?\nEnter quit to exit anytime.\n').lower()
    if level in data:
        play_game(data[level],1)
    elif level=='quit':
        exit()
    else:
        print '\nYou got a typo!'
        start_game()

print '\nWelcome to the MADLIB'
start_game()
