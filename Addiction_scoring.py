import pandas as pd

# Function to calculate addiction score
def calculate_addiction_score(frequency_use, time_spent):
    # Map user inputs to scores
    frequency_scores = {"Daily": 4, "Weekly": 3, "Monthly": 2, "Rarely": 1}
    time_scores = {"18-24 hours": 4, "12-18 hours": 3, "6-12 hours": 2, "0-6 hours": 1}

    return frequency_scores[frequency_use] + time_scores[time_spent]

# Function to categorize addiction level
def categorize_addiction_level(score):
    if 2 <= score <= 3:
        return "Low"
    elif 4 <= score <= 5:
        return "Moderate"
    elif 6 <= score <= 7:
        return "High"
    elif score == 8:
        return "Severe"
    else:
        return "Uncategorized"

# User input questions
questions = [
    {
        "question": "How often do you use social media?",
        "options": ["Daily", "Weekly", "Monthly", "Rarely"],
        "key": "Frequency of Social Media Use"
    },
    {
        "question": "How many hours do you typically spend on social media per day?",
        "options": ["18-24 hours", "12-18 hours", "6-12 hours", "0-6 hours"],
        "key": "Time Spent on Social Media"
    },
]

# Collect user responses
user_responses = {}

print("Please answer the following questions:")
for q in questions:
    print(q["question"])
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(q["options"]):
                user_responses[q["key"]] = q["options"][choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Calculate total addiction score
addiction_score = calculate_addiction_score(
    user_responses["Frequency of Social Media Use"],
    user_responses["Time Spent on Social Media"]
)

# Determine addiction level
addiction_level = categorize_addiction_level(addiction_score)

# Display results
print("\n--- Results ---")
print(f"Your Total Addiction Score: {addiction_score}")
print(f"Your Addiction Level: {addiction_level}")
