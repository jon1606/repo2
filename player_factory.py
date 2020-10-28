from player import Player
from os.path import isfile


class Player_factory:

    def excisting_checker(self, username):
        return isfile(f"player_{username}.txt")

    def sign_up(self):
        print("Let's sign you up:\n")
        username = input('Enter the username you want: ')
        password = input('enter the password you want: ')
        confirmation = input('repeat your password: ')
        while password != confirmation:
            print('The passwords do not match, try again: \n')
            confirmation = input('Repeat your password: ')

        print(f'DEBUG:: the password is: {password}')

        player = Player(username, password, 1, 1)
        player.save()
        player.__print__()
        return player

    def player_maker(self, username):
        file_name = f'player_{username}.txt'

        user_file = open(file_name, 'r')
        file_txt = user_file.readlines()
        username = file_txt[0][:-1]
        password = file_txt[1][:-1]
        level = file_txt[2][:-1]
        class_num = file_txt[3][:-1]

        player = Player( username, password, level, class_num)
        return player

    def log_in(self):
        user_excisting = False
        username = "kuku"
        while not user_excisting:
            username = input('Enter your username: ')
            user_excisting = self.excisting_checker(username)
            if not user_excisting:
                print('This user does not exist, try again...\n')

        player = self.player_maker(username)
        real_password = player.password

        password = None
        while password != real_password:
            password = input('Enter your password: ')
            print(f'The real password is:{real_password}, the provided password is:{password}')
            if password != real_password:
                print('The password is incorrect, try again...')

        return player

