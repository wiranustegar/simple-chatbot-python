import re
import long_responses as Long

def message_probability(user_massage, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Counts in predefined message
    for word in user_massage:
        if word in recognised_words:
            message_certainty += 1

    #Calculates percentage of recognised words massage by user
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_massage:
            has_required_words = False
            break

    if has_required_words or single_response:
        return  int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, singe_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, singe_response, required_words)

    #=============== Response ==================
    response('Halo!', ['hello', 'halo', 'hi', 'hai', 'hola'], singe_response=True)
    response('My name is SimpleChatBot. What\'s your name?', ['your', 'name'], required_words=['name'])
    response('It\'s going well, thank you!. How about you?', ['how', 'are', 'you', 'whats', 'up'], required_words=['how'])
    response('Thank you!', ['i', 'like', 'it'], required_words=['like', 'do'])
    response('Good Morning!', ['good', 'morning'], required_words=['morning'])
    response('Good Night!', ['good', 'night'], required_words=['night'])

    response(Long.R_ASKING, ['where', 'are', 'you', 'from'], required_words=['where', 'you'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return Long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_massage = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_massage)
    return response

#Testing responses
while True:
    print('Bot: ' + get_response(input('You: ')))