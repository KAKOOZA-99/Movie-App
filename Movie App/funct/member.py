import json

def new_member():
    from ast import keyword
    try:
        members_list = []
        infile = open("MemberList.txt", "r")
        line = infile.readline()
        while line:
            members_list.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("<theMembersList.txt> file is not found")
        print("Starting a new members list!")
        members_list = []

    print("Adding a member...")
    member_firstname = input("Enter member first name: >>>")
    member_middlename = input("Enter member middle name: >>>")
    member_lastname = input("Enter member last name: >>>")
    member_phone = input("Enter member phone number: >>>")
    member_dob = input("Enter member Date of Birth(Please enter Year only): >>>")
    member_subscription = input("Has member paid subscription fee(Yes/No): >>>")
    username = member_firstname + member_dob
    members_list.append([username, member_firstname, member_middlename,
                                 member_lastname,member_phone, member_dob, member_subscription])
    print("New member with username " + username + " has been added to your members")