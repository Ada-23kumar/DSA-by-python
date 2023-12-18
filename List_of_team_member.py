# Define a class Team with instance object variable a list of team member names.
# Provide methods to input member names and display member names.

class Team:
    def __init__(self):
        self.list_of_team_member_names = []
    def input_member_names(self):
        while True:
            member_name = input('Enter name if you want quit enter q Or Q ')
            if member_name.lower()=='q':
                break

            self.list_of_team_member_names.append(member_name)
    def display_member_names(self):
        for i in self.list_of_team_member_names:
            print(i)


obj = Team()
obj.input_member_names()
obj.display_member_names()



# class Team:
#     def __init__(self):
#         self.list_of_team_member_names=[]
    
#     def input_member_names(self):
#         while True:
#             member_name=input('Enter name if you want quit enter q Or Q  ')
#             if member_name.lower()=='q':
#                 break
           
#             self.list_of_team_member_names.append(member_name) 
#     def display_member_names(self):
#         for i in self.list_of_team_member_names:
#             print(i)
        
# obj=Team()

# obj.input_member_names()
# obj.display_member_names() 