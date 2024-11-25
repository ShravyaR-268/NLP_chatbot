import re
import random
from spellchecker import SpellChecker

# Initialize the SpellChecker object
spell = SpellChecker()

# Sample responses
responses = {
    "What's your name?": ["I am ELIZA, your friendly chatbot!", "I'm ELIZA, your virtual assistant."],
    "hello": ["Hi there! How can I help you?", "Hello! How are you feeling today?"],
    "I need (.*)": ["Why do you need {0}?", "Would it really help you to get {0}?"],
    "I am (.*)": ["Why are you {0}?", "How long have you been {0}?"],
    "quit": ["Goodbye! Take care!", "It was nice talking to you!"],
    "I feel (.*)": ["Why do you feel {0}?", "What makes you feel {0}?", "Tell me more about why you're feeling {0}."],
    "I'm (.*)": ["What made you feel {0}?", "How long have you been feeling {0}?", "Why do you think you are {0}?"],
    "You are (.*)": ["I am what you perceive me to be.", "Why do you say I am {0}?", "Could I be {0} in your mind?"],
    "I don't know": ["Why don't you know?", "What is it that you're unsure about?", "Can you think of anything that might help?"],
    "I can't (.*)": ["Why do you think you can't {0}?", "What would make it possible for you to {0}?", "What would help you achieve {0}?"],
    "Why (.*)": ["Why do you ask?", "What makes you curious about {0}?", "That's a good question. Why do you think {0}?"],
    "Because (.*)": ["Interesting. Why do you think that is?", "How does that make you feel?", "Could there be another reason?"],
    "Tell me (.*)": ["What would you like to know about {0}?", "Why do you want to hear about {0}?", "Could you tell me more about {0}?"],
    "I'm tired": ["What has made you tired?", "How long have you been feeling tired?", "Do you need to rest?"],
    "I'm angry": ["What has made you angry?", "How do you feel when you're angry?", "Can you think of a way to calm down?"],
    "I'm happy": ["That's wonderful! What made you happy?", "How does it feel to be happy?", "Can you share why you're happy?"],
    "I miss (.*)": ["What do you miss about {0}?", "Why do you miss {0}?", "How long has it been since you missed {0}?"],
    "I love (.*)": ["That's great! Why do you love {0}?", "How does it feel to love {0}?", "Can you explain what makes {0} special?"],
    "I hate (.*)": ["What is it about {0} that makes you hate it?", "Why do you feel so strongly about {0}?", "How does it affect you to hate {0}?"],
    "I'm scared": ["What are you afraid of?", "Why does this scare you?", "Can you think of anything that might help ease your fear?"],
    "I have (.*)": ["How does having {0} make you feel?", "What would you do with {0}?", "Why is {0} important to you?"],
    "Can you (.*)": ["Why do you want me to {0}?", "What do you think would happen if I {0}?", "Do you think I can actually {0}?"],
    "Do you (.*)": ["Why are you asking if I {0}?", "What do you expect me to say about {0}?", "Why do you want to know if I {0}?"],
    "I'm not (.*)": ["Why do you think you're not {0}?", "What makes you feel you're not {0}?", "Could there be another perspective on being {0}?"],
    "I'm (.*) today": ["What has made you feel {0} today?", "Is it a good {0} day for you?", "How are you coping with feeling {0} today?"],
    "What if (.*)": ["What would happen if {0}?", "What do you think could change if {0}?", "How does thinking about {0} make you feel?"],
    "I think (.*)": ["What makes you think {0}?", "How long have you been thinking about {0}?", "Do you think that might be the best way to look at {0}?"],
    "Can you help me": ["Of course! How can I assist you?", "What can I do for you?", "I'm happy to help! What do you need?"],
    "I'm confused": ["What part of the situation is confusing?", "Why do you feel confused?", "Can I clarify anything for you?"],
    "I don't understand": ["What part don't you understand?", "Can I explain that better?", "Let's talk about what you don't get."],
    "I'm feeling (.*)": ["What makes you feel {0}?", "What would make you feel better?", "Is there something specific causing you to feel {0}?"],
    "What do you think": ["I'm not sure. What do you think?", "It's interesting that you ask. What do you think about it?", "Why do you think that way?"],
    "I can't believe (.*)": ["What makes it hard for you to believe {0}?", "Why do you find it unbelievable?", "What would make you believe it?"],
    "I'm not sure": ["What part are you unsure about?", "Can I help you figure it out?", "Why do you feel unsure?"],
    "I want (.*)": ["Why do you want {0}?", "What do you hope will happen if you get {0}?", "What makes {0} so important to you?"],
    "What happened": ["What do you think happened?", "Can you tell me more about what happened?", "How do you feel about what happened?"],
}

# Function to correct spelling
def correct_spelling(text):
    words = text.split()
    misspelled = spell.unknown(words)
    corrected_words = []

    for word in words:
        if word in misspelled:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)

    return ' '.join(corrected_words)

# Chatbot function that processes user input
def eliza_response(user_input):
    # Correct spelling before processing
    user_input = correct_spelling(user_input)

    # Search for patterns and generate a response
    for pattern, responses_list in responses.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            response = random.choice(responses_list)
            return response.format(*[match.group(i + 1) for i in range(len(match.groups()))])

    return "I'm here to listen. Tell me more."

