import json
import random
import re
from datetime import datetime


with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

conversation_history = []
user_name = None


def clean_text(text):

    text = text.lower().strip()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


def detect_intent(user_input):

    cleaned = clean_text(user_input)


    name_match = re.search(r"\bmy name is ([a-zA-Z]+)\b", user_input, re.IGNORECASE)
    if name_match:
        return "set_name", name_match.group(1)

    if cleaned in ["what is my name", "whats my name", "tell me my name"]:
        return "get_name", None


    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_clean = clean_text(pattern)


            if cleaned == pattern_clean or pattern_clean in cleaned:
                return intent["tag"], None

    return "fallback", None


def get_response(intent_tag):

    for intent in data["intents"]:
        if intent["tag"] == intent_tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that. Please try again."


def chatbot_response(user_input):
    global user_name

    intent, value = detect_intent(user_input)

    if intent == "set_name":
        user_name = value
        return f"Nice to meet you, {user_name}! I will remember your name during this session."

    if intent == "get_name":
        if user_name:
            return f"Your name is {user_name}."
        return "You have not told me your name yet. You can say: My name is Kaushal."

    if intent == "time":
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    return get_response(intent)


def save_history():

    with open("conversation_history.txt", "w", encoding="utf-8") as file:
        for line in conversation_history:
            file.write(line + "\n")


def main():
    print("=" * 50)
    print("          AI CHATBOT")
    print("=" * 50)
    print("Type 'exit' to close the chatbot.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        if user_input.lower() == "exit":
            bot_reply = "Goodbye! Have a nice day."
            print("Bot:", bot_reply)

            conversation_history.append(f"You: {user_input}")
            conversation_history.append(f"Bot: {bot_reply}")
            save_history()
            break

        bot_reply = chatbot_response(user_input)

        print("Bot:", bot_reply)

        conversation_history.append(f"You: {user_input}")
        conversation_history.append(f"Bot: {bot_reply}")

    print("\nConversation history saved in conversation_history.txt")


if __name__ == "__main__":
    main()
