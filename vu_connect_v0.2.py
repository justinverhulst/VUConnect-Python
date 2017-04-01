'''
VU Connect 0.2

course_skills() ask for skills. These are added to the list course_skill_list
ask_name() asks user for name. Appends name to student_list
ask_skill() ask user for skill. This is stored in a dictionary of the form {name:{skill:value},name:{skill:value}}
test() runs the code and prints all the relevant lists and dictionaries
match() determines which students should be in a team (does not work properly yet)

NOTE: the match() function gives an error if it is used in combination with the other function. Probably the cause is a bad implementation of the variables (local vs global)

'''

name = ""
course_skill_list = []
student_list = [] # The list with all the students that are registered on VU Connect. Function ask_name() appends the name of the new user to this list
all_name_and_skill_dict = {} # Becomes a dict like {name:{skill:value},name:{skill:value}}
individual_student_skill_dict = {}
number_of_skills = 0
dict = {}

def course_skills(): #Function to add the relevant skills to course (for lecturer). Creates a list with all the skills 
    global number_of_skills
    print "Please add all the skills that are relevant for this course. When done, type 'done'."  
    while True:
        skill = raw_input("Skill: ")
        if skill.lower() == 'done':
            number_of_skills = len(course_skill_list)
            break
        else:
            course_skill_list.append(skill.lower())
        continue
        
def ask_name(): # Ask for name, appends name to student_list
    global name
    name = raw_input("\nWhat is your name?\n>>> ")
    if name in student_list:
        print "You already registered"
    elif name not in student_list:
        student_list.append(name)
        print "\nYou have been successfully subscribed to VU Connect!"
    return name   

def ask_skill(): # Ask for level of skills, relates this to name 
    global name # Make sure that the name is used that was asked for in the ask_name() function
    individual_student_skill_dict = {}   # Create dict of student skills. In this dict, key becomes the skill, value becomes skill value of individual students
    individual_student_name_and_skill_dict = {}  # Create dict of student name and skills.
    print "The skills that are relevant for this course are:\n"
    for skill in course_skill_list:   
        print skill          
    print "\nPlease rank your skills from 1 (least experience) to", number_of_skills,"(most experience). Please note that you have to make an order in the skills, so assign a different number to each skill\n "
    for skill in course_skill_list:        
        skill_value = raw_input(skill+': ') # still to be implemented: make sure that only integers can be used as input
        individual_student_skill_dict[skill] = skill_value # create dict like {skill:value} 
    individual_student_name_and_skill_dict[name] = individual_student_skill_dict # create dict like {name:{skill:value}} for individual student
    all_name_and_skill_dict.update(individual_student_name_and_skill_dict) # append all_name_and_skill_dict with skill:value of individual student            


# EXAMPLE USER LIST TO TEST MATCH FUNCTION:
# all_name_and_skill_dict = {'Didi':{'python':1,'design':2,'writing':3},'Minyi':{'python':3,'design':1,'writing':2},'Nadieh':{'python':1,'design':2,'writing':5}}
# name = "justin"
# individual_student_skill_dict = {'python':3,'design':2,'writing':1}

def match():
    global name
    value_difference = 0
    max_so_far = 0
    total_difference = 0
    iterations = 0
    best_match = ""
    user_to_match = raw_input("Please provide your name, so that I can match you with other students: ")
    if user_to_match == name:
        for key, value in all_name_and_skill_dict.iteritems():
            match_dict = value #dict of the students
            student_to_match = key
            for match_skill, match_value in match_dict.iteritems():       
                if iterations <= len(individual_student_skill_dict):
                    iterations = iterations + 1           
                else:
                    iterations = 0               
                value_difference = abs(match_dict[match_skill] - individual_student_skill_dict[match_skill])               
                total_difference = total_difference + value_difference
                if total_difference > max_so_far:
                    max_so_far = total_difference
                    best_match = student_to_match
                else:
                    total_difference = 0
        print "max:",max_so_far # Grootste verschil user & match
        print "Best Match:",best_match # De match die bij dit grootste verschil hoort  

def test(): #TEST IF EVERYTHIING WORKS
    count = 0
    course_skills()
    number_of_iterations = raw_input("\nNumber of students in this course: ")
    while True: # Loop to determine how many students should be asked for their name and skills    
        ask_name()
        ask_skill()
        count = count + 1
        if count == int(number_of_iterations):
            break
        else:
            continue
    print "--------------------------------------------------------------------"
    print "\nStudents in this course:\n"
    for name in student_list:
        print name
    print "\nSkills needed for this course:\n"
    for skill in course_skill_list:
        print skill
    print "\nOverview of all the students and their skill levels:\n"
    for key, value in all_name_and_skill_dict.iteritems():
        print str(key)+": "+str(value)
   
test()



