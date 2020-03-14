class rosterClass:
    name = ""
    phone_number = 0
    jersey_number = 0

    def __init__(self, name, phone_number, jersey_number):
        self.name = name
        self.phone_number = phone_number
        self.jersey_number = jersey_number

    def display_info(self):
        print("Player name: ", self.name,)
        print("Player Phone Number: ", self.phone_number)
        print("Player Jersey Number: ", self.jersey_number)


def display_menu():
    print("\n===========Main Menu===========")
    print("1. Display Team Roster.")
    print("2. Add Member.")
    print("3. Remove Member.")
    print("4. Edit Member.")
    print("5. Save Data.")
    print("6. Load Data.")
    print("9. Exit Program.\n")
    return int(input("Selection > "))


def display_roster(roster):
    if len(roster) == 0:
        print("No current members in memory.")
    else:
        for x in roster.keys():
            roster[x].display_info()


def add_member(roster):
    new_name = input("Enter new member's name: ")
    new_phone_number = int(input("Enter new member's phone number: "))
    new_jersey_number = int(input("Enter new member's jersey number: "))
    roster[new_name] = rosterClass(new_name, new_phone_number, new_jersey_number)
    return roster


def remove_member(roster):
    remove_name = input("Enter member to be removed: ")
    if remove_name in roster:
        del roster[remove_name]
    else:
        print("Member not found.")
    return roster


def edit_member(roster):
    old_name = input("Enter member to be edited: ")
    if old_name in roster:
        new_name = input("Enter new member's name: ")
        new_phone_number = int(input("Enter new member's phone number: "))
        new_jersey_number = int(input("Enter new member's jersey number: "))
        roster[old_name] = rosterClass(new_name, new_phone_number, new_jersey_number)
    else:
        print("Member not found.")
    return roster


def save(roster):
    filename = input("Filename to save: ")
    print("Saving data...")
    outfile = open(filename, "wt")
    for x in roster.keys():
        new_name = roster[x].name
        new_phone_number = roster[x].phone_number
        new_jersey_number = roster[x].jersey_number
        outfile.write(new_name + "," + new_phone_number + "," + new_jersey_number + "\n")
    print("Data saved.")
    outfile.close()


def load(roster):
    roster = []
    filename = input("Filename to load: ")
    infilename = open(filename, "rt")
    print("Loading data...")
    while True:
        readfile = infilename.readline()
        if not readfile:
            break
        readfile = readfile[:1]
        name, phone_number, jersey_number = readfile.split(",")
        roster[name] = rosterClass(name, phone_number, jersey_number)
        print("Data Loaded Successfully.")
    infilename.close()
    return roster


print("Welcome to the Team Manager")
roster = {}
menu_selection = display_menu()
while menu_selection != 9:
    if menu_selection == 1:
        display_roster(roster)
    elif menu_selection == 2:
        roster = add_member(roster)
    elif menu_selection == 3:
        roster = remove_member(roster)
    elif menu_selection == 4:
        roster = edit_member(roster)
    elif menu_selection == 5:
        roster = save(roster)
    elif menu_selection == 6:
        roster = load(roster)
    menu_selection = display_menu()
print("Exiting Program...")
