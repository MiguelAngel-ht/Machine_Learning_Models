from greetings import *
from functions import *

def load_json(answers, questions, requireds, x_json):
    
  x = ''
  for i in range(len(questions)):
      aux = ",{"
      aux += """ "response_type" : "question""" + str(i) + """","""
      aux += """ "user_input" : """ + str(questions[i]) + ""","""
      aux += """ "bot_response" : " """ + str(answers[i][0]) + """","""
      aux += """ "required_words" : """ + str(requireds[i]) + """}"""
      x += aux
  
  x_json += x + ']}'
  X_json = x_json.replace("\'",'"')
  return X_json


# LOAD DATA FROM TXT FILES

answers = load_answers()
questions = load_questions()
requireds = load_requireds()
X_json = load_json(answers, questions, requireds, x_json)

response_data = json.loads(X_json)              # CREATE JSON
response_data = response_data['data']


# FUNCTION TO GET BETTER RESPONSES 

def get_response(input_string):
    split_message = re.split(r'\s+|[,;!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_string(input_string)


