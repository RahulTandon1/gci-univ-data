**About**
GCI Task description here:
https://codein.withgoogle.com/tasks/5901948314714112

TL;DR
Given input of evalutions of students/applicants in the form of ".ods" files, 
sort the applicants from best to worst and write it to a txt file/.ods file
// I just chose .txt file cause it was easier for me to be honest. Plus I was doing the task last minute.

**Given Variability**
ODF files with different 
- names, 
- marks,
- student count etc.

**Sources of Help**
https://www.w3schools.com/
https://www.rapidtables.com/tools/notepad.html // for thinking out
https://github.com/pyexcel/pyexcel-ods3

**Installation**
run ```pip3 install -r requirements.txt```

**Run and Test it**
run ```python3 index.py```
and then check the file called "output.txt"

To use any other data sets please place it in ```sample-data``` or alternatively change the paths of files in the start ```index.py``` where the following comment is present: ```# setting up data in variables```

**Contents**
1. sample-data - folder containing sample data
2. requirements.txt - requirements for running the project
3. sample-sheet - a sample I used to understand how the 'pyexcel_ods3' module/library/package works in terms of reading data. I thought it would be useful for the reader in he/she wanted to understand why the indexing in the program (index.py) works
4. index.py - the heart of the project which used function from "functions.py" to make the whole project work.
5. functions.py - contains functions used in "index.py". Helps make the code more readable and understandable
6. output.txt - the file to which output (list of the applicants from best to worst) is written.
 


**Initial Algo / Pseudcode**
1. Create a list of students dictionaries with 
    - TERM 1, 2, 3, 4 Marks
    - IELTS Scores
    - Interview Score
2. Compute final scores (cumulative scores) and add them to the dictionary
3. Rank students
4. Print out to file.

**Stuff to Note**
- First two rows always avoid
- Order of stubjects:
Algebra	Physics	PE	Chemistry	Geometry	Biology	Programming
- Marks which would be in fraction form come in decimial form
- Not calculating avg resulting in error and calculating it got correct ans, so finding avg. Apparently, it was all relative in the end