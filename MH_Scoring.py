import pandas as pd

def score_emotions(row):
    mental_health_score = 0
    
    if row['How often do you engage in discussions about mental health or emotional well-being online?'] == 'Never':
        mental_health_score += 0
    elif row['How often do you engage in discussions about mental health or emotional well-being online?'] == 'Rarely':
        mental_health_score += 1
    elif row['How often do you engage in discussions about mental health or emotional well-being online?'] == 'Sometimes':
        mental_health_score += 2
    elif row['How often do you engage in discussions about mental health or emotional well-being online?'] == 'Often':
        mental_health_score += 3

    if row['How has online content impacted your mental health in the past year?'] == 'Positively':
        mental_health_score += 3
    elif row['How has online content impacted your mental health in the past year?'] == 'Negatively':
        mental_health_score -= 2
    elif row['How has online content impacted your mental health in the past year?'] == 'No impact':
        mental_health_score += 1

    if row['Have you ever taken a break from social media for your mental health?'] == 'Yes':
        mental_health_score += 2
    elif row['Have you ever taken a break from social media for your mental health?'] == 'No':
        mental_health_score += 0

    return mental_health_score


def categorize_mental_health_impact(score):
    if score < 3:
        return "Negative Impact on Mental Health"
    elif 3 <= score <= 5:
        return "Minimal Impact"
    elif 6 <= score <= 8:
        return "Moderate Impact (positive or neutral)"
    elif score >= 9:
        return "High Positive Impact"
    else:
        return "Uncategorized"


questions = [
    {
        "question": "How often do you engage in discussions about mental health or emotional well-being online?",
        "options": ["Never", "Rarely", "Sometimes", "Often"],
        "key": "How often do you engage in discussions about mental health or emotional well-being online?"
    },
    {
        "question": "How has online content impacted your mental health in the past year?",
        "options": ["Positively", "Negatively", "No impact"],
        "key": "How has online content impacted your mental health in the past year?"
    },
    {
        "question": "Have you ever taken a break from social media for your mental health?",
        "options": ["Yes", "No"],
        "key": "Have you ever taken a break from social media for your mental health?"
    },
]


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


user_data = pd.DataFrame([user_responses])


user_data['Mental Health Impact Score'] = user_data.apply(score_emotions, axis=1)


total_score = user_data['Mental Health Impact Score'].sum()
category = categorize_mental_health_impact(total_score)


print("\n--- Results ---")
print(f"Your Total Mental Health Impact Score: {total_score}")
print(f"Your Mental Health Impact Level: {category}")
