import random  #imports the random module to make random choices
alternatives = ['rock', 'scissors', 'paper'] #Create a list of weapons
play_again='yes' 
while play_again=='yes':
    
    print('Welcome to my game, rock, scisscors and paper. \n' \
      'Choose your weapon below') 
    answer = input('\n rock \n scissors \n paper \n: ') #Asking for weapons to use(answer)
    computer_ans = random.choice(alternatives)
    #Define if it becomes tie
    if answer==computer_ans:       
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('tie')
    #Define if you loose    
    if (computer_ans=='rock' and answer=='scissors') \
       or (computer_ans=='scissors' and answer=='paper') \
       or (computer_ans=='paper' and answer=='rock'):
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('you loose')
    
    #Define if you win
    if (computer_ans=='scissors' and answer=='rock') \
       or (computer_ans=='paper' and answer=='scissors') \
       or (computer_ans=='rock' and answer=='paper'):
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('you win')
    
    elif (answer!='scissors') and (answer != 'rock') and (answer!='paper'): #Define if your answer is not valid
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('That\'s not a valid answer')
        
    
    play_again=input('play_again? yes/no: ')  #Ask to play agian(yes or no)    

    


    
