# TESTING CHAT BOT FROM PYTHON

from load_data import * # LOAD FUNCTIONS FROM load_data.py

def test():
  # INICIO
  print("Hello! I know stuff about chat bots.", end="")
  print("\nWhen you're done talking, just say 'goodbye','quit' or 'q' \n")
  while True:
    user_input = input("You: ")              # GET INPUT
    response = get_response(user_input)
    print("Bot:", response)             # RETURN ANSWER

    if response == "See you later!":     # BREAK CONVERSATION 
      break

# EXECUTE TESTING
test()