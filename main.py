from configparser import ConfigParser
from misc.util import clear, input_user, normal_prefix, error_prefix
from modules.follow import follow
from modules.unfollow import unfollow

config = ConfigParser()
config.read("config.ini")
access_token = config.get("Settings", "access_token")
is_playing = True

if access_token == "your_token":
    print(error_prefix("Write in the settings.ini file your access_token from github."))
else:
    while is_playing:
        clear()
        choice = input_user()

        if type(choice) == int:
            match choice:
                case 1:
                    who_follow: str = input(normal_prefix("Enter the person you want to follow all their followers: "))

                    follow(access_token, who_follow)
                case 2:
                    unfollow(access_token)
                case _:
                    clear()

        correct_choices: list = [1, 2]

        if is_playing and type(choice) == int and choice not in correct_choices:
            input("\n" + normal_prefix("Press Enter to continue..."))
