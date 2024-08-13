import random
import os
from questions_set1 import questions_set1  # Import the first set of questions
from questions_set2 import questions_set2  # Import the second set of questions

def ask_question(question_num, total_questions, question, options, correct_answer, description, answer=None):
    os.system('clear')  # Clear the screen before each question
    
    # Randomize the correct answer position while keeping the numbering 1-4
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]
    shuffled_correct_answer = indices.index(correct_answer - 1) + 1
    
    # Display the question number and question out of the total
    print(f"\nQuestion {question_num} of {total_questions}\n")
    print(f"{question}\n")
    
    # Display options with correct numbering
    for idx, option in enumerate(shuffled_options, 1):
        print(f"{idx}. {option}")

    print()  # Add a blank line for spacing
    
    if answer:
        print(f"Your previous answer: {answer}")
    else:
        answer = input("Choose the correct option (1-4), or 'b' to go back: ").strip()
    
    # Handle back navigation
    if answer.lower() == 'b':
        return None, False  # Go back without saving an answer

    # Determine if the answer was correct
    correct_text = options[correct_answer - 1]
    if answer == str(shuffled_correct_answer):
        print("\nCorrect!\n")
        is_correct = True
    else:
        print("\nWrong!\n")
        print(f"The correct answer is: {correct_text}\n")
        is_correct = False
    
    # Show the description after the answer is given
    print(f"Description: {description}\n")

    input("Press Enter to continue...")  # Pause before moving to the next question

    return answer, is_correct

def select_questions_set():
    print("Select the set of questions you want to answer:")
    print("1. Question Set 1")
    print("2. Question Set 2")
    print("3. Both Sets of Questions")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return questions_set1
    elif choice == '2':
        return questions_set2
    elif choice == '3':
        return questions_set1 + questions_set2
    else:
        print("Invalid choice. Defaulting to both sets of questions.")
        return questions_set1 + questions_set2

def choose_ordering():
    print("\nHow would you like the questions to be ordered?")
    print("1. Randomized")
    print("2. In Order")
    choice = input("Enter the number of your choice: ").strip()

    if choice == '1':
        return True  # Randomize
    elif choice == '2':
        return False  # In order
    else:
        print("Invalid choice. Defaulting to randomized order.")
        return True

def main():
    score = 0
    wrong_questions = []

    selected_questions = select_questions_set()

    # Choose whether to randomize the questions or keep them in order
    randomize_order = choose_ordering()

    if randomize_order:
        random.shuffle(selected_questions)

    answers = [None] * len(selected_questions)  # To keep track of user answers
    total_questions = len(selected_questions)  # Total number of questions
    current_question = 0

    while current_question < len(selected_questions):
        q = selected_questions[current_question]
        answer, is_correct = ask_question(current_question + 1, total_questions, q["question"], q["options"], q["correct_answer"], q["description"], answers[current_question])
        
        if answer is not None:
            answers[current_question] = answer
            if is_correct:
                score += 1
            else:
                wrong_questions.append(q)
            current_question += 1  # Move to the next question
        elif current_question > 0:
            current_question -= 1  # Go back to the previous question

    print(f"\nYour final score is {score}/{total_questions}")

    # If there are unanswered questions, go back to them
    for i, answer in enumerate(answers):
        if answer is None:
            current_question = i
            break

    while current_question < len(selected_questions):
        if answers[current_question] is None:
            q = selected_questions[current_question]
            answer, is_correct = ask_question(current_question + 1, total_questions, q["question"], q["options"], q["correct_answer"], q["description"])
            if answer is not None:
                answers[current_question] = answer
                if is_correct:
                    score += 1
                else:
                    wrong_questions.append(q)
                current_question += 1
        else:
            current_question += 1

    # Offer to retry wrong questions
    if wrong_questions:
        print(f"\nYou got {len(wrong_questions)} questions wrong. Would you like to try them again? (y/n)")
        retry = input().strip().lower()
        if retry == 'y':
            print("\nRepeating wrong questions...\n")
            wrong_question_index = 0
            while wrong_question_index < len(wrong_questions):
                q = wrong_questions[wrong_question_index]
                answer, is_correct = ask_question(wrong_question_index + 1, len(wrong_questions), q["question"], q["options"], q["correct_answer"], q["description"])
                if answer is not None:
                    wrong_question_index += 1  # Move to the next question
                elif wrong_question_index > 0:
                    wrong_question_index -= 1  # Go back to the previous question

if __name__ == "__main__":
    main()
