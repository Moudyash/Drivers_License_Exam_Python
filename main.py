
import random

'''
Mohammed Yehia Ashour
1301195595
'''
def correct_answers():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D',
                       'A']

    return correct_answers


def user_answers():
    answers_list = []
    answeslist = ["A", "B", "C"]
    while len(answers_list) <= 19:
        answers_list.append(random.choice(answeslist))
    return answers_list


def check_Answers(correct_list, answers_list):
    count = 0
    print("user answer",answers_list)
    print("correct answer",correct_list)

    wrong_answers = []
    for i in range(20):
        if correct_list[i] == answers_list[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count += 0
    if count < 15:
        print('You failed')
    else:
        print('You passed')
    print(' number of correct answers', count)
    print(' number of incorrect answers ', 20 - count)
    print(' incorrect answered question :',  wrong_answers)


def main():
    correct_list = correct_answers()
    answers_list = user_answers()
    check_Answers(correct_list, answers_list)
    user_choice=int(input("please select a choice: \n 1:Test another student\n 2:Exit\n"))
    if user_choice==1:
        main()
    else: quit()

main()

