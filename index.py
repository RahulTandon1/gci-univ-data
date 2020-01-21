from pyexcel_ods3 import get_data
from functions import *

# setting up data in variables
term1_data = get_data("sample-data/Data1.ods")['Sheet1']
term2_data = get_data("sample-data/Data2.ods")['Sheet1']
term3_data = get_data("sample-data/Data3.ods")['Sheet1']
term4_data = get_data("sample-data/Data4.ods")['Sheet1']

# a single List containing all the terms' data
# used in a for loop below
TERMS_DATA = [term1_data, term2_data, term3_data, term4_data]

ielts_data = get_data("sample-data/IELTS.ods")['Sheet1']
interview_data = get_data("sample-data/Interview.ods")['Sheet1']

# initialising empty list for students dictionaries
students = list()

# base student object types:
# 'name', 'term1', 'term2', 'term3', 'term4', 'ielts', 'interview'


# set up student objects
students = intialise_students(students, term1_data)


# set up term marks
for index in range(0, len(TERMS_DATA)):
    term_data = TERMS_DATA[index]
    students = setUpTermMarks(students, term_data, index+1)
    # index + 1 because 0th el is term1 data ^

# set up ielts marks
students = setUpData(students, ielts_data, 'ielts')

# set up interview marks
students = setUpData(students, interview_data, 'interview')

'''
as of now, an element of students looks like:
{
    'name': 'Isaac newton',
    'total_of_term1': 753.0,
    'total_of_term2': 701.0,
    'total_of_term3': 716.0,
    'total_of_term4': 606.0,
    'total_of_ielts': 32.0,
    'total_of_interview': 23.0
}

Now we have to calculate a final score, where
all marks of terms contribute 40%
all marks of ielts contribte 30%
all marks of interview contribut 30%

Usually, given any fraction x/y one can say x/y of <number>
we'll do the same thing with marks.

If we had intially divided the marks, we would have gotten the decimal form of
the fractions.

But since in the ending the denominators would always end up being the same,
we did not need to divide.

So we'll just be multiplying with the respective scores to get the final score
'''

# setting up final_score for each student which will be used to order 
# them from best to worst
for student in students:

    academic_total = (student['total_of_term1'] +
                      student['total_of_term2'] +
                      student['total_of_term3'] +
                      student['total_of_term4']) * 40
    ielts_total = student['total_of_ielts'] * 30
    interview_total = student['total_of_interview'] * 30

    final_score = academic_total + ielts_total + interview_total
    student['final_score'] = final_score


# function used while sorting students in order of final_score
def final_scores(student):
    return student['final_score']


# sorting students
students.sort(key=final_scores)

# writing students to file
f = open('output.txt', 'w')
f.write('Applicants from best to worst \n\n')

# looping through students
for student in students:

    # writing name
    f.write(student['name'])

    # going to next line
    f.write('\n')

# closing file by convention
f.close()
