print("Welcome to the Team Manager")
team_manager = True
roster = []
while team_manager is True:
    print("\n===========Main Menu===========")
    print("1. Display Team Roster.")
    print("2. Add Member.")
    print("3. Remove Member.")
    print("4. Edit Member.")
    print("9. Exit Program.\n")
    user_selection = int(input("Selection> "))
    def roster_display_1():
        print(*roster, sep = "\n")
    def add_member_2():
        member_name = str(input("Enter new member's name: "))
        roster.append(member_name)
    def remove_member_3():
        remove_member = str(input("Enter member name to be removed: "))
        roster.remove(remove_member)
    def modify_member_4():
        old_name = str(input("Enter the name of the memeber you want to edit: "))
        old_name_selection = roster.index(old_name)
        new_name = input("Enter the new name of the member: ")
        roster[old_name_selection] = new_name
    def exit_program_9():
        print("Exiting Program...")
    if user_selection == 9:
            exit_program_9()
            break
    elif user_selection == 1:
        roster_display_1()
    elif user_selection == 2:
        add_member_2()
    elif user_selection == 3:
        remove_member_3()
    elif user_selection == 4:
        modify_member_4()

"""Test Values and Output---
Welcome to the Team Manager

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 2
Enter new member's name: Nathan

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 2
Enter new member's name: Toby

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 1
Nathan
Toby

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 3
Enter member name to be removed: Toby

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 1
Nathan

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 4
Enter the name of the memeber you want to edit: Nathan
Enter the new name of the member: Nathan Braun

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 1
Nathan Braun

===========Main Menu===========
1. Display Team Roster.
2. Add Member.
3. Remove Member.
4. Edit Member.
9. Exit Program.

Selection> 9
Exiting Program..."""