from pyfiglet import *
from instaloader import *
from termcolor import  *

Figlet = Figlet(font="Slant")
print(Figlet.renderText("INSTA-TOOL"))
cprint(f"\t\t\t\t\t\t\t####|Created By DANNY|####", 'red')

cprint("\n************ \\\\INSTAGRAM PROFILE PICTURE DOWNLOADER\\\\************\n", 'red')

username = input("[+] Enter target victim's instagram username:--")
try:
    session = instaloader.Instaloader()
    session.download_profile(username,profile_pic_only=True)
    cprint(f"\n[+] The user \"{username}\" profile picture has been downloaded sucessfully..\n",'blue')
except:
    cprint(f"\n[-] The username \"{username}\" does't exist.Please check the username you have entered\n",'blue')
    pass






