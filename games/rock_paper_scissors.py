import random
alternatives = ['rock', 'scissors', 'paper']
play_again='yes'
while play_again=='yes':
    
    print('Welcome to my game, rock, scisscors and paper. \n' \
      'Choose your weapon below')
    answer = input('\n rock \n scissors \n paper \n: ')
    computer_ans = random.choice(alternatives)
    
    if answer==computer_ans:
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('tie')
        
    if (computer_ans=='rock' and answer=='scissors') \
        or (computer_ans=='scissors' and answer=='paper') \
        or (computer_ans=='paper' and answer=='rock'):
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('you loose')
    
    
    if (computer_ans=='scissors' and answer=='rock') \
        or (computer_ans=='paper' and answer=='scissors') \
        or (computer_ans=='rock' and answer=='paper'):
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('you win')
    
    if (answer!='scissors') and (answer != 'rock') and (answer!='paper'):
        print('computer:' + computer_ans + ' vs ' + 'you:' + answer)
        print('That\'s not a valid answer')
        
    
    play_again=input('play_again? yes=yes/no: ')
    


    