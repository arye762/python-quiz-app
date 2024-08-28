# Python Quiz Application

This Python Quiz Application is designed to help users test their knowledge on various topics, particularly focused on networking concepts. The application allows users to select from different sets of questions, receive immediate feedback after each question, and retry questions they answered incorrectly.


![Python-quiz-app](https://github.com/user-attachments/assets/7a4ca4fa-097a-4793-b848-971c380d8ae3)


## Features

- **Multiple Question Sets**: Users can choose between different sets of questions (e.g., original questions, essay-related questions).
- **Immediate Feedback**: After answering a question, users are informed whether their answer was correct or incorrect, along with an explanation.
- **Retry Incorrect Questions**: Users have the option to retry questions they answered incorrectly at the end of the quiz.
- **Randomized Questions**: Questions and answer choices are presented in a randomized order to enhance the learning experience.

## Project Structure

- `quiz.py`: The main Python script that runs the quiz. It prompts the user to select a question set, asks the questions, provides feedback, and tracks scores.
- `questions_set1.py`: A Python file containing the first set of questions (e.g., original questions).
- `questions_set2.py`: A Python file containing the second set of questions (e.g., essay-related questions).
- `README.md`: This file, providing an overview of the project and instructions for setup and usage.

## Setup

Clone the Repository
   ```bash
   git clone https://github.com/arye762/python-quiz-app.git
   cd python-quiz-app
   ```
## Running the Quiz on Ubuntu

To run the Python quiz application on an Ubuntu machine, follow these steps:
a. Navigate to the Project Directory:
   ```bash
   cd /path/to/python-quiz-app
   ```
b. Run the Python Script:
   ```bash
   python3 quiz.py
   ```
This command will start the quiz, and you can follow the on-screen prompts to select a question set and begin answering questions.

## Usage 

### Select a Question Set

Upon running the quiz, you will be prompted to choose between different sets of questions:
- Option 1: Questions Set 1 (from questions_set1.py).
- Option 2: Questions Set 2 (from questions_set2.py).
- Option 3: Both sets of questions combined.

### Choose Question Ordering

After selecting a question set, you will be prompted to choose whether the questions should be presented in a randomized order or in the order they appear in the set:
- Option 1: Randomized Order
- Option 2: Sequential Order

### Answer Questions

- For each question, select the correct answer by entering the corresponding number (1-4).
- After each question, you will receive immediate feedback indicating whether your answer was correct or wrong, along with a description of the correct answer.

### Retry Incorrect Questions

- After completing the quiz, you will have the option to retry any questions you answered incorrectly.

## Disclaimer

This Python Quiz Application was conceptualized by Arie Cimafranca. The code implementation was generated with the assistance of ChatGPT.
