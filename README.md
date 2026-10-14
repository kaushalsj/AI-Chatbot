# AI Chatbot

## Task 1 – AI Chatbot

This project is a simple rule-based AI chatbot built using Python.

It recognizes predefined user intents using keyword/pattern matching and returns suitable responses.

## Features

- More than 10 supported intents
- Natural-language style keyword matching
- Multi-turn conversation support
- Remembers the user's name during the current session
- Fallback response for unknown input
- Console-based chat interface
- Conversation history logging
- Uses an external `intents.json` dataset

## Technologies Used

- Python 3.x
- JSON
- Regular Expressions (`re`)
- Basic NLP / pattern matching

## Project Structure

```text
AI_Chatbot/
│
├── chatbot.py
├── intents.json
├── README.md
├── conversation_history.txt   # created after running the chatbot
└── screenshots/
    └── sample_conversation.txt
```

## Supported Intents

1. Greeting
2. Goodbye
3. Thanks
4. Bot Name
5. Age
6. Help
7. Weather
8. Time
9. Joke
10. College
11. Programming
12. User Name Memory / Multi-turn conversation
13. Fallback

## How to Run

1. Make sure Python 3.x is installed.
2. Keep `chatbot.py` and `intents.json` in the same folder.
3. Open Command Prompt or terminal in the project folder.
4. Run:

```bash
python chatbot.py
```

5. Start chatting with the bot.
6. Type `exit` to close the chatbot.

After exiting, the chatbot saves the conversation in:

```text
conversation_history.txt
```

## Example Conversation

```text
You: Hi
Bot: Hello! How can I help you?

You: My name is Kaushal
Bot: Nice to meet you, Kaushal! I will remember your name during this session.

You: What is my name?
Bot: Your name is Kaushal.

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: exit
Bot: Goodbye! Have a nice day.
```

## Fallback Example

```text
You: asdfghjkl
Bot: Sorry, I didn't understand that. Please try again.
```

## Testing

The chatbot can be tested with at least 20 inputs such as:

```text
Hi
Hello
Hey
Good morning
Thank you
Thanks
What is your name?
How old are you?
Help
I need help
What time is it?
Tell me the time
Tell me a joke
Make me laugh
What is the weather?
College admission
Tell me about Python
What is programming?
My name is Kaushal
What is my name?
Bye
```

## Assignment Requirements Covered

- At least 10 intents: Yes
- Natural language processing / keyword matching: Yes
- Multi-turn conversation: Yes
- Fallback response: Yes
- Chat interface: Yes, console-based
- Conversation history: Yes
- Intent dataset: Yes, `intents.json`
- Sample conversation: Yes
