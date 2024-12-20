import streamlit as st
import joblib

# Load the emotion classification model
pipe_lr = joblib.load(open("model/emotion.pkl", "rb"))

# Define emotion-based customer behavior
emotions_emoji_dict = {
    "anger": "😠",
    "disgust": "🤮",
    "fear": "😱",
    "happy": "🤗",
    "joy": "😂",
    "neutral": "😐",
    "sad": "😔",
    "sadness": "😔",
    "shame": "😳",
    "surprise": "😮"
}

negative_emotions = {"anger", "disgust", "fear", "sad", "sadness", "shame"}
positive_emotions = {"happy", "joy", "surprise"}

def predict_emotion(text):
    """Predict the emotion of a given text."""
    result = pipe_lr.predict([text])
    return result[0]

def run():
    st.title("Emotion Recognizer and Customer Behavior Predictor")
    
    st.subheader("Enter Text to Analyze")
    user_input = st.text_area("Your text here...")

    if st.button("Analyze Emotion"):
        if user_input:
            # Predict emotion
            predicted_emotion = predict_emotion(user_input)
            emoji = emotions_emoji_dict.get(predicted_emotion, "")

            # Determine customer behavior
            if predicted_emotion in negative_emotions:
                behavior = "Customer will discontinue."
            elif predicted_emotion in positive_emotions:
                behavior = "Customer will continue."
            else:
                behavior = "Neutral behavior."

            # Display results
            st.write(f"**Emotion:** {predicted_emotion} {emoji}")
            st.write(f"**Behavior Prediction:** {behavior}")
        else:
            st.warning("Please enter text for analysis.")

if __name__ == "__main__":
    run()