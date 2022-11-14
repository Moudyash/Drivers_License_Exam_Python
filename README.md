# Drivers_License_Exam_Python
** *italicized text*Driver’s License Exam**

The local driver’s license office has asked you to create an application that grades the written portion of the driver’s license exam. The exam has 20 multiple-choice questions. The list of correct answers is given to you.

The program should create another list containing a student's answers for each of the 20 questions - this list is called `student_answers` -, The student's answers are generated randomly from A, B, C, and D. 

After the answers dictionary has been created, the program should display a message indicating whether the student passed or failed the exam. (A student must correctly answer 15 of the 20 questions to pass the exam.)

It should then display the total number of correctly answered questions, the total number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.

After finishing the student testing and displaying the result, the program should ask the user if he wants to test another student or exit - by entering 'yes' or 'no' -. (use `exit()` or `quit()` to finish the program.)

**Hint:** To randomly selects an element in a list, use the `random` module’s `choice` function. You pass a list as an argument to the function, and the function returns the randomly selected element. To use the function, be sure to import the random module. The following interactive session demonstrates:

```
>>> import random
>>> names = ['Jenny', 'Kelly', 'Chloe', 'Aubrey']
>>> winner = random.choice(names)
>>> print(winner)
Chloe
>>>
```
Also, to reorganize the order of list items you can use the `shuffle()` method from the same module. This method takes a sequence, like a list, and changes the original list, it does not return a new list.
<h1>OUTPUT</h1>
![image](https://user-images.githubusercontent.com/83330641/201609980-4809a77a-581f-4243-b21d-f4a5e49e1c61.png)

user answer ['B', 'B', 'C', 'A', 'C', 'A', 'A', 'A', 'A', 'A', 'C', 'B', 'B', 'A', 'B', 'A', 'B', 'C', 'B', 'C']
correct answer ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
You failed
 number of correct answers 4
 number of incorrect answers  16
 incorrect answered question : [0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19]
please select a choice: 
 1:Test another student
 2:Exit
