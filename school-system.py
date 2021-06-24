import os
import time
import csv
from colorama import Fore, Back
from tabulate import tabulate
studentsList = []

with open("file.csv","r",newline="") as dataFile:
    reader = csv.reader(dataFile)
    for row in reader:
        studentsList.append(row)

def clear_the_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def title():
    print(f'''
    {Fore.CYAN + "="*55 + Fore.RESET}
                    {Fore.GREEN}Student Management System{Fore.RESET}
    {Fore.CYAN + "="*55 + Fore.RESET}
    ''')
def menu():
    print(f'''
        {Fore.YELLOW}╒{"═"*38}╕{Fore.RESET}
                       {Fore.RED}INSTRUCTIONS
        {Fore.YELLOW}╘{"═"*38}╛{Fore.RESET}
            {Fore.RED}{"_"*34}
            {Fore.RED}|{Fore.RESET}{Back.MAGENTA}  Press 1 to Search Student     {Back.RESET}{Fore.RED}|{Fore.RESET}
            {Fore.RED}|{Fore.RESET}{Back.MAGENTA}  Press 2 to Add Student        {Back.RESET}{Fore.RED}|{Fore.RESET}
            {Fore.RED}|{Fore.RESET}{Back.MAGENTA}  Press 3 to Delete Student     {Back.RESET}{Fore.RED}|{Fore.RESET}
            {Fore.RED}|{Fore.RESET}{Back.MAGENTA}  Press 4 to see Students List  {Back.RESET}{Fore.RED}|{Fore.RESET}
            {Fore.RED}|{Fore.RESET}{Back.MAGENTA}  Press 5 to Exit               {Back.RESET}{Fore.RED}|{Fore.RESET}
            {Fore.RED}{"‾"*34}{Fore.RESET}
    ''')

clear_the_screen()
while True:
    title()
    menu()
    action = input(f"{Fore.GREEN}Please Enter a Value to Perform an Action {Fore.RED}[{Fore.GREEN}1{Fore.RED}-{Fore.GREEN}5{Fore.RED}]{Fore.GREEN} : {Fore.YELLOW}")
    if action== "1":
        rollNum = input(f"{Fore.GREEN}Please Input Student Roll Number{Fore.RED}: {Fore.YELLOW}")
        for i in range(len(studentsList)):
            try:
                if studentsList[i][1] == rollNum:
                    clear_the_screen()
                    print(f''' 
                            {Fore.BLUE}┏━  {"="*12}  ━┓{Fore.RESET}
                                {Fore.GREEN}STUDENT DATA
                            {Fore.BLUE}┗━  {"="*12}  ━┛{Fore.RESET}
                    ''')
                    print(f'\t\t\t{Fore.YELLOW}╒{"="*25}╕{Fore.RESET}')
                    print(f"\t\t\t   {Fore.RED}Name:{Fore.RESET}    {Fore.MAGENTA}{studentsList[i][0]}{Fore.RESET}")
                    print(f"\t\t\t   {Fore.RED}Roll No:{Fore.RESET} {Fore.MAGENTA}{studentsList[i][1]}{Fore.RESET}") 
                    print(f"\t\t\t   {Fore.RED}Age:{Fore.RESET}     {Fore.MAGENTA}{studentsList[i][2]}{Fore.RESET}")
                    print(f"\t\t\t   {Fore.RED}Class:{Fore.RESET}   {Fore.MAGENTA}{studentsList[i][3]}{Fore.RESET}")
                    print(f"\t\t\t   {Fore.RED}Section:{Fore.RESET} {Fore.MAGENTA}{studentsList[i][4]}{Fore.RESET}")
                    print(f'\t\t\t{Fore.YELLOW}╘{"="*25}╛{Fore.RESET}')
                    input(f'''
                    {Fore.BLUE}┏━  {"="*21}  ━┓{Fore.RESET}
                        {Fore.GREEN}Hit Enter To Continue 
                    {Fore.BLUE}┗━  {"="*21}  ━┛{Fore.RESET}
                        ''')
                    clear_the_screen()
                    break
            except:
                    print(f'''
                             ╒{"="*32}╕
                              Please Enter a Valid Roll Number
                             ╘{"="*32}╛
                    ''')
    elif action == "2":
        clear_the_screen()
        student = []
        print(f'''       
                            {Fore.BLUE}┏━  {"="*16}  ━┓{Fore.RESET}
                                {Fore.GREEN}ADDING A STUDENT
                            {Fore.BLUE}┗━  {"="*16}  ━┛{Fore.RESET}
                        ''')
        student.append(input(f"{Fore.GREEN}Please Enter Student Name{Fore.RED}:{Fore.YELLOW} "))
        student.append(input(f"{Fore.GREEN}Please Input Student Roll Number{Fore.RED}:{Fore.YELLOW} "))
        student.append(input(f"{Fore.GREEN}Please Enter Student Age{Fore.RED}:{Fore.YELLOW} "))
        student.append(input(f"{Fore.GREEN}Please Enter Student Class{Fore.RED}:{Fore.YELLOW} "))
        student.append(input(f"{Fore.GREEN}Please Enter Student Section{Fore.RED}:{Fore.YELLOW} "))
        studentsList.append(student)
        clear_the_screen()
        print(f'''
        {Fore.BLUE}╒{"="*26}╕
         {Fore.GREEN}Student Added Successfully
        {Fore.BLUE}╘{"="*26}╛{Fore.RESET}
        ''')
        time.sleep(3)
        clear_the_screen()
    elif action == "3":
        rollNum = input(f"{Fore.GREEN}Please Input Student Roll Number{Fore.RED}:{Fore.YELLOW} ")
        for i in range(len(studentsList)):
            if studentsList[i][1] == rollNum:
                del studentsList[i]
                clear_the_screen()
                print(f'''
                {Fore.RED}╒{"="*28}╕
                 {Fore.YELLOW}Student Removed Successfully
                {Fore.RED}╘{"="*28}╛{Fore.RESET}
                ''')
                time.sleep(3)
                clear_the_screen()
                break
    elif action == "4":
        clear_the_screen()
        print(f'''       
                        {Fore.BLUE}┏━  {"="*15}  ━┓
                             {Fore.RED}STUDENTS LIST
                        {Fore.BLUE}┗━  {"="*15}  ━┛{Fore.RESET}
{"‾"*74}
        ''')
        print(tabulate(studentsList, headers=['| Name |','| Roll No |','| Age |','| Class |','| Section |']))    
        print(f'''
{"‾"*74}
        ''')
        time.sleep(3)
    elif action == "5":
        with open("file.csv","w",newline="") as dataFile:
            writer = csv.writer(dataFile,delimiter=",")
            for i in range(len(studentsList)):
                writer.writerow(studentsList[i])
        exit()
    else:
        print("Input a Valid Action Number")