# Granify Coding Assignment

Sohyun Park

sohyun2@ualberta.ca

## 1. Project Description
This project is to evaluate the overall understanding of the process of generating object data and storing it in a database. For this purpose, the candidate should create objects named Cat and Dog, and test data transaction with a fake database connection.

## 2. File Structure and Functions
For this assignment, I used python (Python 3.6.8) because it is the programming language that I feel most comfortable using. For Part 1 of the assignment, I converted the ruby code in the assignment description to python code.

### 2-1. Cat

* Cat class in Part 1: Code conversion from ruby to python.

* Cat class in Part 2 and 3: 

1. An initial name can be set (default value is an empty string).

2. `speak()` function will give you a say "Meow".

3. `setName()` method will keep a list of all the names the cat has ever had.

4. `getNames()` method will return a list of all the names the cat has ever had.

5. The cat’s age increases by 1 every five times it speaks.

6. `getAverageNameLength()` will return the average length of all the names the cat has ever had.

7. The cat’s initial age to a random number between 5 and 10.

8. `newSpeak()` method will obtaion an argument. If not supplied, the cat still says “meow”.
If supplied, the cat prints the value of the argument.

### 2-2. Dog

* Dog class in Part 2 and Part 3: Mostly the same with the Cat class, but instead of favouriteFood related functions it has a skill related functions, which represents the trained skills of a dog. In addition, instead of `speak()` and `newSpeak()`, the Dog class has `walk()` function. The `walk()` function get the distance mile that the dog walks, and if the total walk distance is more than 30, than the dog's age increases by 1. Default value of the distance mile is 0.

### 2-3. Data

* Data class in Part 1: Code conversion from ruby to python.

* Data class in Part 2: No change from the class of Part 1.

* Data class in Part 3: `commit()` and `rollback()` functions return transaction id. This transaction id is necessary to debug the transaction in the database.

### 2-4. functions.py in Part 3

The file contains `saveTest(catName, dogName)`, `savePetShop()`, and `logStats(message)` as required. In `saveTest(catName, dogName)` and `savePetShop()`, I used "AttributeError" for exception handling, which should be transaction error in the real database. `logStats(message)` will give the user a log file which contains transaction id and if the transaction is successful or not.

## 3. Instructions to run the codes
Please open your terminal for code execution. The location to run the code is indicated in the subsections below. There is no special libarary or framework required except random. 

### 3-1. Part 1

**Location for the execution**: granify_ParkS/Coding_Tasks/part1

command line: `python main.py`

expected output: Interpreter output

Name is currently
Name has been changed to Garfield
Connecting to database
Inserting Garfield into table Cat

### 3-2. Part 2

**Location for the execution**: granify_ParkS/Coding_Tasks/part2

command line: `python test.py`

expected output: Unit test results

The program will ask you to give some inputs to do the unit test. The input should be an integer for the Test 1, a string for Test 2, and an integer for Test 5.

### 3-3. Part 3

**Location for the execution**: granify_ParkS/Coding_Tasks/part3

command line: `python test.py`

expected output: Unit test results

The program will provide a log file named **STDOUT.log**.

## 4. Thoughts

The assignment description is ambiguous, so it is difficult to accurately grasp the examiner's intention. For example, it is said that the candidates don't need to use a physical connection with a database. But if we want to test if the rollback function works well as intended, we need at least a toy database for testing.

## 5. Questions?

Please reach out to me using the email address: sohyun2@ualberta.ca.
