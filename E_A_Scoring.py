import pandas as pd

def score_emotions(row):
    emotional_score = 0
    if row['How often do you notice tone or sentiment shifts in conversations online?'] == 'Often':
        emotional_score += 2
    elif row['How often do you notice tone or sentiment shifts in conversations online?'] == 'Sometimes':
        emotional_score += 1

    if row['Have you ever reached out to someone online for emotional support?'] == 'Yes':
        emotional_score += 1

    if row['How often do you offer emotional support to friends or strangers online?'] == 'Often':
        emotional_score += 2
    elif row['How often do you offer emotional support to friends or strangers online?'] == 'Sometimes':
        emotional_score += 1

    if row['How do you feel after providing emotional support online?'] == 'Satisfied':
        emotional_score += 2
    elif row['How do you feel after providing emotional support online?'] == 'Drained':
        emotional_score -= 1

    if row['Do you believe that social media platforms influence the way you process emotions?'] == 'Yes':
        emotional_score += 1

    return emotional_score

# Function to categorize emotional awareness
def categorize_emotional_awareness(score):
    if score >= 8:
        return "Very High Emotional Awareness"
    elif 6 <= score <= 7:
        return "High Emotional Awareness"
    elif 4 <= score <= 5:
        return "Moderate Emotional Awareness"
    elif 2 <= score <= 3:
        return "Low Emotional Awareness"
    else:
        return "Uncategorized"

# Questions for the user
questions = [
    {
        "question": "How often do you notice tone or sentiment shifts in conversations online?",
        "options": ["Never", "Rarely", "Sometimes", "Often"],
        "key": "How often do you notice tone or sentiment shifts in conversations online?"
    },
    {
        "question": "Have you ever reached out to someone online for emotional support?",
        "options": ["No", "Yes"],
        "key": "Have you ever reached out to someone online for emotional support?"
    },
    {
        "question": "How often do you offer emotional support to friends or strangers online?",
        "options": ["Never", "Rarely", "Sometimes", "Often"],
        "key": "How often do you offer emotional support to friends or strangers online?"
    },
    {
        "question": "How do you feel after providing emotional support online?",
        "options": ["Indifferent", "Drained", "Satisfied"],
        "key": "How do you feel after providing emotional support online?"
    },
    {
        "question": "Do you believe that social media platforms influence the way you process emotions?",
        "options": ["No", "Yes"],
        "key": "Do you believe that social media platforms influence the way you process emotions?"
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
user_data['Emotional Score'] = user_data.apply(score_emotions, axis=1)

# Get the total score and categorize it
total_score = user_data['Emotional Score'].sum()
category = categorize_emotional_awareness(total_score)

# Display the results
print("\n--- Results ---")
print(f"Your Total Emotional Awareness Score: {total_score}")
print(f"Your Emotional Awareness Level: {category}")
