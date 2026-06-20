\# Personal Learning Tracker



A simple Python-based terminal application that helps learners track their problem-solving progress across coding platforms.



\## Overview



Learning new skills requires consistency and proper tracking. Personal Learning Tracker helps users maintain a record of solved problems, track learning progress, and view useful statistics about their practice habits.



This project was built using core Python concepts such as functions, loops, file handling, dictionaries, exception handling, and input validation.



\## Features



\### Add Completed Problems



Record details of a solved problem including:



\* Problem Name

\* Topic

\* Platform

\* Difficulty Level

\* Time Taken

\* Date Solved



\### View Progress



Display all previously recorded problems with:



\* Problem Name

\* Topic

\* Platform

\* Difficulty

\* Time Taken

\* Date Solved



\### Progress Dashboard



Automatically generates statistics such as:



\* Total Problems Solved

\* Difficulty-wise Counts



&#x20; \* Easy

&#x20; \* Medium

&#x20; \* Hard

\* Topic-wise Counts

\* Platform-wise Counts

\* Fastest Solved Problem

\* Slowest Solved Problem

\* Average Solving Time



\### Input Validation



The application validates:



\* Menu choices

\* Topic selection

\* Platform selection

\* Difficulty selection

\* Time taken input

\* Empty problem names



\### Error Handling



Handles:



\* Missing progress file

\* Empty progress file



\## Technologies Used



\* Python 3

\* File Handling

\* Dictionaries

\* Functions

\* Exception Handling



\## Project Structure



```text

Personal-Learning-Tracker/

│

├── personal_learning_tracker.py

├── progress\_tracker.txt

└── README.md

```



\## Sample Record Format



```text

Two Sum|Arrays|Leetcode|Easy|15|20 June 2026

```



\## Learning Outcomes



This project helped practice:



\* Python fundamentals

\* Data storage and retrieval

\* Dictionary-based statistics

\* Program design

\* Input validation

\* Error handling



\## Future Improvements (To Be Added)



\### Planned Features



\* JSON-based storage instead of plain text files

\* Search problems by name

\* Search problems by topic

\* Delete existing entries

\* Edit existing entries

\* Most practiced topic

\* Least practiced topic

\* Average solving time by topic

\* Average solving time by difficulty

\* Sort records by date

\* Sort records by solving time

\* Export progress report

\* Progress streak tracking

\* Monthly statistics dashboard

\* CSV export support

\* SQLite database integration

\* Graphical User Interface (Tkinter)



\## How to Run



1\. Clone the repository



```bash

git clone https://github.com/Dinesh655-dev/personal-learning-tracker.git

```



2\. Navigate to the project folder



```bash

cd personal-learning-tracker

```



3\. Run the program



```bash

python personal_learning_tracker.py

```



\## Author



Built as a learning project while practicing Python programming and problem solving.


Requirements
-----------
Python 3.x
