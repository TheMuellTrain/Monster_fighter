import random
player_name = ''
player = {}
monster ={}


def engine(game_running, play_again):
    player_name = input("What is your name?")
    player = {'name': player_name, 'player_attack': 0, 'player_heal': 16, 'player_health': 100}
    monster = {'name': 'Diddy', 'monster_attack': 0, 'monster_health': 100}
    while game_running == True:
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        choice = input()
        if choice == '1':
            player['player_attack'] = random.randint(0,12)
            monster['monster_attack'] = random.randint(0,15)
            print(player['name']+ ' has hit ' + str(player['player_attack']))
            monster['monster_health'] = monster['monster_health']- player['player_attack']
            if monster['monster_health']>= 0:
                print(monster['name'] + " now has health of: " + str(monster['monster_health']))
                print(monster['name']+ " is fighting back")
                print(monster['name'] + ' has hit ' + str(monster['monster_attack']))
                player['player_health'] = player['player_health']-monster['monster_attack']
                if player['player_health']>=0:
                    print(player['name'] + ' now has health of: ' + str(player['player_health']))
        elif choice == '2':
            print(player['name'] + ' drinks health potion')
            player['player_health'] = player['player_health']+player['player_heal']
            print(player['name']+ ' your health has increased to:'+ str(player['player_health']))
        else:
            print('Invalid input')
        if player['player_health']<=0:
            print('Oh no! '+ player['name'] + ' you lost!')
            game_running = False
            print('would you like to play again?')
            print('1) Yes')
            print('2) No')
            play_choice = input()
            if play_choice == '1':
                return main()
            else:
                return exit()
        elif monster['monster_health']<=0:
            print('Congratulation '+player['name']+ ' you won!')
            game_running = False
            print('would you like to play again?')
            print('1) Yes')
            print('2) No')
            play_choice = input()
            if play_choice == '1':
                return main()
            else:
                return exit()
        else:
            continue
def main():
    engine(True, True)
if __name__== "__main__":
  main()

