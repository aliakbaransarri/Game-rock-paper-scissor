from config import GAME_CHOICE, RULES, score_board
import random


def get_user_choice():
    user_input = input("Enter Your Choice (r, p, s): ")
    if user_input not in GAME_CHOICE:
        print ("Oops!!, wrong choice, try again please...")
        return get_user_choice()
    return user_input


def get_system_choice():
    return random.choice(GAME_CHOICE)


def find_winner(user, system):
    match = {user, system}
    
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))] 


def update_score_board (result):
    if result['user'] == 3:
        score_board['user'] += 1
        msg = 'You win'
    else:
        score_board['system'] += 1
        msg = 'You lose'

    print("#" * 30)
    print("##", f'user: {score_board["user"]}'.ljust(24), "##")
    print("##", f'system: {score_board["system"]}'.ljust(24), "##")
    print("##", f'last game: {msg}'.ljust(24), "##")
    print("#" * 30)


def play():
    
    result = {'user': 0, 'system': 0}
    
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner  = find_winner(user_choice, system_choice)
        
        if winner == user_choice:
            msg = 'You win'
            result['user'] += 1
        elif winner == system_choice:
            msg = 'You lose'
            result['system'] += 1
        else:
            msg = 'Draw'
        print (f"User choice:{user_choice}\nSystem choice:{system_choice}\nresult: {msg}")
        
    update_score_board (result) 


play_again = input("Do you want to play again? (y/n)")
if play_again == 'y':
    play()

