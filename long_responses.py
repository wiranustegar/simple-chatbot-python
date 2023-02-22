import random

R_ASKING = "I am from nowhere, somebody create me to answer your question only"

def unknown():
    response = ['Sorry, could you please repeat that?',
                "...",
                "Sound about right",
                "What does that mean?"][random.randrange(4)]
    return response