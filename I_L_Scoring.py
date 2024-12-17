import pandas as pd

# Function to calculate emotional score
def score_emotions(row):
    emotional_score = 0
    # Scoring logic based on responses
    if row['How often do you post your thoughts or feelings online?'] == 'Rarely':
        emotional_score += 1
    elif row['How often do you post your thoughts or feelings online?'] == 'Sometimes':
        emotional_score += 2
    elif row['How often do you post your thoughts or feelings online?'] == 'Often':
        emotional_score += 3

    if row['Have you ever felt negative emotions after viewing content online?'] == 'Never':
        emotional_score += 0
    elif row['Have you ever felt negative emotions after viewing content online?'] == 'Rarely':
        emotional_score += 1
    elif row['Have you ever felt negative emotions after viewing content online?'] == 'Sometimes':
        emotional_score += 2
    elif row['Have you ever felt negative emotions after viewing content online?'] == 'Always':
        emotional_score += 3

    if row['How do you typically respond when you feel emotionally triggered by content?'] == 'Comment':
        emotional_score += 3
    elif row['How do you typically respond when you feel emotionally triggered by content?'] == 'Share':
        emotional_score += 2
    elif row['How do you typically respond when you feel emotionally triggered by content?'] == 'Ignore':
        emotional_score += 1

    if row['Do you feel supported by your online community when expressing emotions?'] == 'Never':
        emotional_score += 0
    elif row['Do you feel supported by your online community when expressing emotions?'] == 'Rarely':
        emotional_score += 1
    elif row['Do you feel supported by your online community when expressing emotions?'] == 'Sometimes':
        emotional_score += 2
    elif row['Do you feel supported by your online community when expressing emotions?'] == 'Often':
        emotional_score += 3

    if row['Do you feel more or less anxious after spending time on social media?'] == 'More':
        emotional_score += 3
    elif row['Do you feel more or less anxious after spending time on social media?'] == 'Less':
        emotional_score -= 1
    elif row['Do you feel more or less anxious after spending time on social media?'] == 'No Change':
        emotional_score += 0

    if row['Have you experienced online harassment or negative comments directed toward your emotional expressions?'] == 'Yes':
        emotional_score += 3
    elif row['Have you experienced online harassment or negative comments directed toward your emotional expressions?'] == 'No':
        emotional_score += 0

    if row['How do you manage your emotional reactions to negative content online?'] == 'Unfollow':
        emotional_score += 1
    elif row['How do you manage your emotional reactions to negative content online?'] == 'Block':
        emotional_score += 2
    elif row['How do you manage your emotional reactions to negative content online?'] == 'Report':
        emotional_score += 3
    elif row['How do you manage your emotional reactions to negative content online?'] == 'Ignore':
        emotional_score += 0

    return emotional_score

# Function to categorize emotional impact
def categorize_impact(score):
    if 7 <= score <= 12:
        return "Minimal impact"
    elif 13 <= score <= 18:
        return "Moderate emotional impact"
    elif 19 <= score <= 24:
        return "High emotional impact"
    elif 25 <= score <= 28:
        return "Severe emotional impact"
    else:
        return "Uncategorized"

# Questions for the user
questions = [
    {
        "question": "How often do you post your thoughts or feelings online?",
        "options": ["Rarely", "Sometimes", "Often"],
        "key": "How often do you post your thoughts or feelings online?"
    },
    {
        "question": "Have you ever felt negative emotions after viewing content online?",
        "options": ["Never", "Rarely", "Sometimes", "Always"],
        "key": "Have you ever felt negative emotions after viewing content online?"
    },
    {
        "question": "How do you typically respond when you feel emotionally triggered by content?",
        "options": ["Comment", "Share", "Ignore"],
        "key": "How do you typically respond when you feel emotionally triggered by content?"
    },
    {
        "question": "Do you feel supported by your online community when expressing emotions?",
        "options": ["Never", "Rarely", "Sometimes", "Often"],
        "key": "Do you feel supported by your online community when expressing emotions?"
    },
    {
        "question": "Do you feel more or less anxious after spending time on social media?",
        "options": ["More", "Less", "No Change"],
        "key": "Do you feel more or less anxious after spending time on social media?"
    },
    {
        "question": "Have you experienced online harassment or negative comments directed toward your emotional expressions?",
        "options": ["Yes", "No"],
        "key": "Have you experienced online harassment or negative comments directed toward your emotional expressions?"
    },
    {
        "question": "How do you manage your emotional reactions to negative content online?",
        "options": ["Unfollow", "Block", "Report", "Ignore"],
        "key": "How do you manage your emotional reactions to negative content online?"
    }
]

# User input collection
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

# Create a DataFrame with the user's responses
user_data = pd.DataFrame([user_responses])

# Calculate the score
user_data['Emotional Score'] = user_data.apply(score_emotions, axis=1)

# Get the total score and categorize it
total_score = user_data['Emotional Score'].sum()
category = categorize_impact(total_score)

# Display the results
print("\n--- Results ---")
print(f"Your Total Emotional Impact Score: {total_score}")
print(f"Your Emotional Impact Level: {category}")
