import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the survey response CSV
data = pd.read_csv('survey_responses.csv')

# Define scoring functions (same as before)
def score_emotions(row):
    emotional_score = 0
    if row['How often do you post your thoughts or feelings online?'] == 'Often':
        emotional_score += 2
    elif row['How often do you post your thoughts or feelings online?'] == 'Sometimes':
        emotional_score += 1
    if row['Have you ever felt negative emotions after viewing content online?'] in ['Always', 'Sometimes']:
        emotional_score -= 1
    return emotional_score

def score_awareness(row):
    awareness_score = 0
    if row['How often do you notice tone or sentiment shifts in conversations online?'] == 'Often':
        awareness_score += 2
    if row['Have you ever reached out to someone online for emotional support?'] == 'Yes':
        awareness_score += 1
    awareness_score += 1
    return awareness_score

def score_mental_health(row):
    mental_health_score = 0
    if row['How has online content impacted your mental health in the past year?'] == 'Negatively':
        mental_health_score -= 2
    if row['Do you feel more or less anxious after spending time on social media?'] == 'More':
        mental_health_score -= 1
    if row['Have you ever taken a break from social media for your mental health?'] == 'Yes':
        mental_health_score += 1
    return mental_health_score

def score_addiction(row):
    addiction_score = 0
    if row['How often do you use social media?'] == 'Daily':
        addiction_score += 3
    elif row['How often do you use social media?'] == 'Weekly':
        addiction_score += 2
    elif row['How often do you use social media?'] == 'Monthly':
        addiction_score += 1
    return addiction_score

def score_sentiment_analysis_framework(row):
    framework_score = 0
    if row['Do you think sentiment analysis tools (AI-based) can accurately assess emotions in online content?'] == 'Yes':
        framework_score += 2
    if row['How do you feel about sentiment analysis being used in mental health applications (e.g., identifying emotional distress)?'] == 'Supportive':
        framework_score += 1
    if row['Would you like to see more personalized content based on your emotional state?'] == 'Yes':
        framework_score += 1
    return framework_score

# Apply scoring
data['emotion_score'] = data.apply(score_emotions, axis=1)
data['awareness_score'] = data.apply(score_awareness, axis=1)
data['mental_health_score'] = data.apply(score_mental_health, axis=1)
data['addiction_score'] = data.apply(score_addiction, axis=1)
data['framework_score'] = data.apply(score_sentiment_analysis_framework, axis=1)

# Calculate overall sentiment
def calculate_overall(row):
    total_score = (row['emotion_score'] + row['awareness_score'] +
                   row['mental_health_score'] + row['addiction_score'] +
                   row['framework_score'])
    if total_score >= 5:
        return "Positive"
    elif 0 <= total_score < 5:
        return "Neutral"
    else:
        return "Negative"

data['overall_sentiment'] = data.apply(calculate_overall, axis=1)

# Encoding target variable (overall sentiment) for RF
label_encoder = LabelEncoder()
data['overall_sentiment_encoded'] = label_encoder.fit_transform(data['overall_sentiment'])

# Define features and target
X = data[['emotion_score', 'awareness_score', 'mental_health_score', 'addiction_score', 'framework_score']]
y = data['overall_sentiment_encoded']

# Normalize the feature data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.1, random_state=42)

# Hyperparameter tuning using GridSearchCV for Random Forest
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Best parameters from GridSearch
print("Best parameters from GridSearch:", grid_search.best_params_)

# Train the best model
rf_model = grid_search.best_estimator_

# Make predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.2f}")

# Visualize Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', xticklabels=label_encoder.classes_, yticklabels=label_encoder.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()


score_columns = ['emotion_score', 'awareness_score', 'mental_health_score', 'addiction_score', 'framework_score']
scores_data = data[score_columns]

plt.figure(figsize=(12, 8))

for idx, col in enumerate(score_columns, 1):
    plt.subplot(2, 3, idx)
    sns.histplot(scores_data[col], kde=True, bins=10, color='skyblue')
    plt.title(f'Distribution of {col.replace("_", " ").title()}')
    plt.xlabel('Score')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


overall_sentiment_count = data['overall_sentiment'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(overall_sentiment_count, labels=overall_sentiment_count.index, autopct='%1.1f%%', colors=['#66b3ff', '#99ff99', '#ff6666'])
plt.title('Distribution of Overall Sentiment')
plt.show()
