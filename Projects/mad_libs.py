import time,re

print('Hello, and welcome to my first simple project!\nI hope you like it! Have fun!')
print()
time.sleep(2)

def enter_info():
    global boy_name, vegetable, teacher_name, girl_name, vegetable1, boy_name1, vegetable2
    while True:
        try:
            boy_name = input("Enter a boy's first name: ")
            if re.match(r'^[A-Z][a-z]+$', boy_name) is None:
                raise NameError
        except NameError:
            print('Not a valid name. Enter again!')
        else:
            break
    while True:
        try:
            teacher_name = input("Enter a teacher's first name: ")
            if re.match(r'^[A-Z][a-z]+$', teacher_name) is None:
                raise NameError
        except NameError:
            print('Not a valid name. Enter again!')
        else:
            break
    while True:
        try:
            girl_name = input("Enter a girl's first name: ")
            if re.match(r'^[A-Z][a-z]+$', girl_name) is None:
                raise NameError
        except NameError:
            print('Not a valid name. Enter again!')
        else:
            break
    while True:
        try:
            boy_name1 = input("Enter a boy's first name: ")
            if re.match(r'^[A-Z][a-z]+$', boy_name1) is None:
                raise NameError
        except NameError:
            print('Not a valid name. Enter again!')
        else:
            break            
    vegetable = input('Enter a vegetable: ')
    vegetable1 = input('Enter a vegetable(1): ')
    vegetable2 = input('Enter a vegetable(2): ')
    print()
    time.sleep(2)
    mad_lib_story()

def mad_lib_story():
    print('This is a story called: Parents!')
    print(f"Once upon a time there was a little boy named {boy_name}. He was not like all the other children,\n"
    "because he had a very big secret. Everyday he went to school hoping no one had discovered the\n"
    f"truth. You see {boy_name}'s parents were really {vegetable}. How he turned out to be a normal boy, he didnt't know.\n\n"
    "It was report card time, the trickiest time of the year, because that was when the teachers\n"
    f"usually wanted to meet all of the students' parents. {boy_name} always did his best in school so that his\n"
    "parents wouldn't have to meet his teacher.\n\n"
    f"This year was no exception, except that {teacher_name} always wanted to meet everyone's parents. Sure\n"
    f"enough, at the bottom of his report card, an interview time had been scheduled. {boy_name} was devastated! How would he explain?\n\n"
    "When he brought his report card home, his parents were excited. Finally they would get to meet\n"
    f"one of {boy_name}'s teachers.\n\n"
    f"That evening {boy_name} and his parents walked to the school. All the while {boy_name} was dying inside. How,\n"
    f"oh how, would he explain!? Hey, wait a minute! When he looked around he saw {girl_name}, the most\n"
    f"popular girl in class and her parents were {vegetable1} and walking towards the gym where was {boy_name1} and his\n"
    f"parents were {vegetable2}.\n\n"
    f"Wow, what a relief, {boy_name} wasn't so different after all!\n"
    "~The End~")

enter_info()