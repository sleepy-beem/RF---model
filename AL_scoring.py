import pandas as pd

# Function to calculate the score
def score_emotions(row):
    emotional_score = 0
    # Scoring logic for each question
    if row['Do you think sentiment analysis tools (AI-based) can accurately assess emotions in online content?'] == 'Yes':
        emotional_score += 3
    elif row['Do you think sentiment analysis tools (AI-based) can accurately assess emotions in online content?'] == 'No':
        emotional_score += 1

    if row['Do you think social media platforms should use sentiment analysis to moderate emotional content?'] == 'Yes':
        emotional_score += 3
    elif row['Do you think social media platforms should use sentiment analysis to moderate emotional content?'] == 'No':
        emotional_score += 1

    if row['How do you feel about your online data (emotional expressions) being used in sentiment analysis by companies?'] == 'Comfortable':
        emotional_score += 3
    elif row['How do you feel about your online data (emotional expressions) being used in sentiment analysis by companies?'] == 'Neutral':
        emotional_score += 2
    elif row['How do you feel about your online data (emotional expressions) being used in sentiment analysis by companies?'] == 'Uncomfortable':
        emotional_score += 1

    if row['How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?'] == 'Supportive':
        emotional_score += 3
    elif row['How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?'] == 'Unsure':
        emotional_score += 2
    elif row['How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?'] == 'Against':
        emotional_score += 1

    if row['Would you like to see more personalized content based on your emotional state?'] == 'Yes':
        emotional_score += 3
    elif row['Would you like to see more personalized content based on your emotional state?'] == 'No':
        emotional_score += 1

    return emotional_score

# Function to categorize attitude levels
def categorize_attitude_level(score):
    if 5 <= score <= 8:
        return "Low trust and skepticism toward AI"
    elif 9 <= score <= 12:
        return "Moderate trust and interest in AI usage"
    elif 13 <= score <= 15:
        return "High trust and support for AI-based sentiment analysis"
    elif score > 15:
        return "Strong Enthusiasm and Advocacy for AI in Sentiment Analysis"
    else:
        return "Uncategorized"

# Questions for the user
questions = [
    {
        "question": "Do you think sentiment analysis tools (AI-based) can accurately assess emotions in online content?",
        "options": ["Yes", "No"],
        "key": "Do you think sentiment analysis tools (AI-based) can accurately assess emotions in online content?"
    },
    {
        "question": "Do you think social media platforms should use sentiment analysis to moderate emotional content?",
        "options": ["Yes", "No"],
        "key": "Do you think social media platforms should use sentiment analysis to moderate emotional content?"
    },
    {
        "question": "How do you feel about your online data (emotional expressions) being used in sentiment analysis by companies?",
        "options": ["Comfortable", "Uncomfortable", "Neutral"],
        "key": "How do you feel about your online data (emotional expressions) being used in sentiment analysis by companies?"
    },
    {
        "question": "How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?",
        "options": ["Supportive", "Against", "Unsure"],
        "key": "How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?"
    },
    {
        "question": "Would you like to see more personalized content based on your emotional state?",
        "options": ["Yes", "No"],
        "key": "Would you like to see more personalized content based on your emotional state?"
    },
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
user_data['Attitude Score'] = user_data.apply(score_emotions, axis=1)

# Get the total score and categorize it
total_score = user_data['Attitude Score'].sum()
category = categorize_attitude_level(total_score)

# Display the results
print("\n--- Results ---")
print(f"Your Total Attitude Score: {total_score}")
print(f"Your Attitude Level: {category}")
