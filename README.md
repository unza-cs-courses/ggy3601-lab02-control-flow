# GGY3601 Lab 2: Control Flow & Functions

**Weight:** 10% of final grade
**Estimated Time:** 2-3 hours

## Purpose

This lab introduces control flow structures (conditionals and loops) and functions, which are essential for writing programs that make decisions and process data.

## Learning Outcomes

By completing this lab, you will be able to:
- LO2.1: Write conditional statements to make decisions
- LO2.2: Use for loops to iterate over sequences
- LO2.3: Use while loops for condition-based repetition
- LO2.4: Define and call functions with parameters and return values
- LO2.5: Combine control structures and functions

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and test values.**

The ASSIGNMENT.md file contains your student-specific values that you must use in your solutions. These values are unique to you and are used for automated testing.

## Repository Structure

```
.
├── src/
│   ├── lab2_classify.py       # Task 1: Grade classification with conditionals
│   ├── lab2_processing.py     # Task 2: Sample processing with for loops
│   ├── lab2_validation.py     # Task 3: Input validation with while loops
│   ├── lab2_calculator.py     # Task 4: Drilling cost calculator function
│   └── lab2_statistics.py     # Task 5: Grade statistics report
├── tests/
│   └── visible/               # Automated tests (visible to you)
├── ASSIGNMENT.md              # Your unique assignment parameters
└── README.md                  # This file
```

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique values
3. Complete each task in the `src/` directory
4. Run tests locally: `pytest tests/visible/ -v`
5. Push your code to see automated test results

## Tasks Overview

### Task 1: Grade Classification (20 marks)
Write a function that classifies ore grades using if/elif/else statements based on your unique thresholds.

### Task 2: Sample Processing (20 marks)
Use for loops to iterate through sample data and process each item.

### Task 3: Input Validation (15 marks)
Use while loops to repeatedly prompt for valid input until correct data is entered.

### Task 4: Drilling Cost Calculator (25 marks)
Create a function with parameters that calculates drilling costs based on depth and applies appropriate rate adjustments.

### Task 5: Grade Statistics Report (20 marks)
Combine loops and conditionals to generate a summary report of sample grades.

## Submission

Push your completed code to this repository before the deadline. Your score is calculated from the automated tests.

## Academic Integrity

- **ALLOWED:** Lecture notes, official Python documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software.
