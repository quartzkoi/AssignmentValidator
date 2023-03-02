# Assignment Validator: Statement of Work

## Purpose

Client Matthew Pogue of Wichita State University, Wichita, KS, is seeking assistance from 
Trent Smith, an independent contractor, in developing software to assist in fascilitating and grading of tests and assignments. 
The purpose of the software will be to conduct a test for studnets, and then analyze the given answers 
to grade their accuracy for the educator.

## Scope of Work

Code will be appended to the GitHub project (\<AssignmentValidator>), in the form of a pull request from a separate branch. 
Provider will transfer any documentation created, source code, and any additional documents that might be useful in additional development.
Deliverables will be transferred to the client before the last day March 2023. 
If problems in development arise, extension can be discussed and agreed upon between the client and the provider in good will.

## Deliverables

A 'testReader' class will be used to read the provided document, and separate each line into three public arrays: Question, Correct_Answer, and Decoy_Answers.
A fourth/fifth array, correct_Answers and incorrect_Answers, will be created to save questions the student has answered
- Any additional helper functions will be available to call as a public function.
A GUI application will be used to administer the questions to the student, who will complete applicable questions.
-The students answers will be saved through a new public array, student_Answer, and compared to the Correct_Answer and Decoy_Answers
--If student_Answer matches Correct_Answer, the given question will be added to the correct_Answers array; if else, it will be added to incorrect_Answers
After all questions have been answered, the correct_Answers and incorrect_Answers will be saved into a new file "results.txt", for educators use. If requested, the results will be printed out for student.

## Timeline

Updates will be sent after class meetings on Tuesdays and Thursdays via request. Expected timeline of completion goes as followed:
- **Thursday, March 2nd**: Researching Tkinter, reading documentation, and documenting technical requirements.
- **Tuesday, March 7th**: APathfinding research done, general technical requirements written down and sent through email.
- **Thursday, March 9th**: Code has begun being written, with initial testing, followed by additional questions
- **Tuesday March 14th**: Code has been written and implemented following a series of bug-fixing.
- **Thursday March 16th**: General implementation finished, ready to submit a pull request to github repository.

## Compensation

Compensation from the client to the provider will be in the form of a one-time payment to the provider at the end of the contract.
Compensation of a passing grade to be delivered upon completion and transference of deliverables.