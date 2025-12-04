# Import the TextBlob library for sentiment analysis
from textblob import TextBlob

# Display a welcome message
print("👋 Welcome to the AI Mood Detector!")

# Ask the user for their name
name = input("What's your name? ")
print("Nice to meet you",name)

print("Let's find out the sentiment of your sentences.")

while True:
    # Ask the user to enter a sentence
    sentence = input("📝 Your sentence: ")
    if sentence.lower() == "exit":
        print("Good Bye, {name}")
        break
    
# Create a TextBlob object for sentiment analysis
    blob = TextBlob(sentence).sentiment

# Get the sentiment polarity score
# Polarity ranges from -1 (negative) to +1 (positive)

    sentiment = blob.polarity
    print(sentiment)


# Check the polarity value and print the result  
    if sentiment > 0:
        print("😊 Positive sentiment detected!\n")
    elif sentiment < 0:
        print("😞 Negative sentiment detected!\n")
    else:
        print("😐 Neutral sentiment detected!\n")