from typing import TextIO


class Player:
    def __init__(self, username, password, level, class_num):
        self.password = password
        self.level = int(level)
        self.username = username
        self.class_num = int(class_num)

    def hello(self):
        return f"Hello {self.username}, welcome to 'It's A Numbers Game'\n"

# TODO: fix error , save all this player parameters into file
    def save(self):
        file_name = f"player_{self.username}.txt"
        user_file = open(file_name, 'w')
        user_file.write(f'{self.username}\n{self.password}\n{self.level}\n{self.class_num}\n')
        user_file.close()
        print(f'DEBUG:: the password is: {self.password}')
        return ''

    def __print__(self):
        print(f'The user is : {self.username}, password is : {self.password}, the level: {self.level}')

