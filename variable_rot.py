from sys import argv
from colorama import Fore, Style   

'''
Variable ROT
'''

if __name__ == "__main__":
    lower_alph = [chr(ascii_value) for ascii_value in range(97, 123)]
    upper_alph = [alph.upper() for alph in lower_alph]
    rot = int(argv[1])
    for arg in argv[2:]:
        decoded_message = ""
        for alph in arg:
            if alph in lower_alph:
                decoded_message += lower_alph[(lower_alph.index(alph)+rot)%len(lower_alph)]
            elif alph in upper_alph:
                decoded_message += upper_alph[(upper_alph.index(alph)+rot)%len(upper_alph)]
            else:
                decoded_message += alph
        print(f"{Fore.YELLOW}{arg}{Fore.RESET} => {Fore.GREEN}{Style.BRIGHT}{decoded_message}{Fore.RESET}{Style.RESET_ALL}")