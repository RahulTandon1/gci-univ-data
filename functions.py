'''
About
-----
A file/module consisting of functions used in index.py
'''


'''
Exaple of how a student dictionary will like by the end of the program:
{
    'name': 'Isaac newton',
    'avg_of_term1': 753.0,
    'avg_of_term2': 701.0,
    'avg_of_term3': 716.0,
    'avg_of_term4': 606.0,
    'avg_of_ielts': 32.0,
    'avg_of_interview': 23.0
}
'''

# takes input of students list (empty at this point in the code)
# and the data of any term, we'll be passing in term1's data in this program
# returns the list of students with student dictionaries
# each comprising of only 1 key: 'name'
def intialise_students(students, term1_data):

    # NOTE: Data starts row 3 onwards

    for index in range(3, len(term1_data)):

        # e.g. term1_data[3] -> ['Sundar Pichai', 87, 63, 70, 45, 90, 53, 95]
        currentStudent = term1_data[index]

        # checking if empty row
        if len(currentStudent) == 0:
            continue
        else:

            # adding a new student dictionary with the 'name' key assigned
            students.append({
                'name': str(term1_data[index][0])   # e.g. 'Sundar Pichai'
            })

    return students


# for setting up total marks for each term
def setUpTermMarks(students, term_data, term_index):

    # iterating through rows
    # NOTE: Data starts row 3 onwards

    for index in range(3, len(term_data)):

        # getting current row
        currentStudent = term_data[index]
        # e.g. term1_data[3] -> ['Sundar Pichai', 87, 63, 70, 45, 90, 53, 95]

        # -------- checking if empty row --------
        if len(currentStudent) == 0:
            continue

        # -------- row not empty so calculate ------

        # storing total of term for current student in a variable
        term_total = float(0)

        '''
        order of subjects
        Algebra, Physics, PE, Chemistry, Geometry, Biology, Programming
        1        2        3   4           5           6       7
        0 in a blank cell
        '''

        # iterating through row
        # from 1 to avoid the name of student
        for i in range(1, len(currentStudent)):

            # NOTE -> maths & physics get double waitage
            # Position of maths+phy from above -> 1, 2, 5
            if i in [1, 2, 5]:
                term_total += 2 * float(currentStudent[i])

            # all other subjects get normal waitage
            else:
                term_total += float(currentStudent[i])

        # --- adding term average to student dictionary ---
        # students index == index - 3
        # e.g. Sundar Pichar position in students = 3 - (3) = 0
        # assigning average | avergae = total / (10 subjs * 100 marks each)
        # 10 subjs because maths(2 internal subjs) and physics got 2X value
        students[index - 3][f'avg_of_term{term_index}'] = term_total/1000

    return students


# for setting up both ielts_score and interview_score
def setUpData(students, data, dataType):

    # Iterating through students rows
    # NOTE: Data starts row 3 onwards

    for index in range(3, len(data)):

        currentStudent = data[index]
        # e.g. term1_data[3] -> ['Sundar Pichai', 5, 8, 3, 7.5]

        # checking if empty row
        if len(currentStudent) == 0:
            continue

        # -------- row not empty so compute --------
        tempTotal = float(0)

        # range from 1 to avoid name
        for i in range(1, len(currentStudent)):
            tempTotal += float(currentStudent[i])

        # students index == index - 3
        # e.g. Sundar Pichar position in students = 3 - (3) = 0
        if dataType == 'ielts':
            # assigning average | avergae = total / (4 subjs * 9 marks each)
            students[index - 3][f'avg_of_{dataType}'] = tempTotal/36
        else:
            # assigning average | avergae = total / ( 5 subjs * 10 marks each)
            students[index - 3][f'avg_of_{dataType}'] = tempTotal/50

    return students
