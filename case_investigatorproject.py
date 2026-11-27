#Willen Abriol, Xavier Lleva, Ramon Bulao
#Case Investigator Project
#8 Ilang-Ilang
from datetime import datetime

cases = []
suspects = []

def add_case(): #adds investigation cases
    print("|-- ADD INVESTIGATION CASE --|")
    new_case = input("Enter new investigation case: (0 to exit) ")
    if new_case == "0":
        return
    if new_case == "":
        print("Case cannot be empty.")
        return
    if new_case in cases:
        print("Case already exists.")
        return
    
    now = datetime.now()
    cases.append(new_case)
    print(f"Case {new_case} added at {now.strftime('%m/%d/%Y %H:%M:%S')}")

def inspect_case(): #display cases, add suspects, or display suspects
    while True:
        print("|-- CASES AND SUSPECTS --|")
        print("(1) Display cases")
        print("(2) Add a suspect to a case")
        print("(3) Display suspects")
        print("(0) Go back")

        choice = input("> ").strip()
        if choice == "1":
            if not cases:
                print("No cases available.")
            else:
                for i in range(len(cases)):
                    print(f"{i+1}. {cases[i]}")

        elif choice == "2":
            if not cases:
                print("Add a case before registering a suspect.")
                continue
            case_name = input("Enter the case name: ").strip()
            if case_name not in cases:
                print("Case not found.")
                continue
            suspect_name = input("Enter the suspect's name: ").strip()
            if suspect_name == "":
                print("Suspect name cannot be empty.")
            else:
                suspects.append(f"{case_name} -> {suspect_name}")

        elif choice == "3":
            if not suspects:
                print("There are no suspects yet.")
            else:
                for i in range (len(suspects)):
                    print(f"{i+1}. {suspects[i]}")
        elif choice == "0":
            return
        else:
            print("Command not found.")

def credits(): #give credits to the authors
    print("Case Investigator Program")
    print("Created by: Willen Abriol, Xavier Lleva, Ramon Bulao.")

def main_menu(): #main menu that transports you back here whenever you finish managing cases and suspects
    while True:
        print("|-- MAIN MENU --|")
        print("(1) Add an investigation case")
        print("(2) Manage cases and suspects")
        print("(3) Credits")
        print("(0) Exit")
        choice = input("> ").strip()

        if choice == "1":
            add_case()
        elif choice == "2":
            inspect_case()
        elif choice == "3":
            credits()
        elif choice == "0":
            print("Program closed. See you soon!")
            break
        else:
            print("Command not found.")

#three lines only, but the def functions handle the rest.
print("Welcome to the Case Investigator Project!")
print("Add Cases, Suspect People, View Current Investigations, And Make Clarifications.")
main_menu()

#We made this project mainly because we wanted to track our cases, whether minor or major, like finding your wallet missing or someone destroying your personal belongings.
#This is useful whenever you want to keep track of those problems and be able to see it clearly in an organized manner.
#By using def functions, a datetime import to keep track of the time, and multiple if-else branched statements for our options, we are able to create this program.