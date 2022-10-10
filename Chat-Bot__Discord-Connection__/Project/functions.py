import json
import re
import random

import spacy
import en_core_web_sm


# LOAD ANSWERS LIKE SENTECES
def load_answers():
  with open('answers.txt', 'r') as f:
      answers = [line.splitlines() for line in f]
  return answers

# LOAD QUESTIONS LIKE LIST OF WORDS
def load_questions():  
  with open('questions.txt', 'r') as f:
      strings = [line.splitlines() for line in f]
      questions = [line[0].split() for line in strings]
      for i, quest in enumerate(questions):
        for j, word in enumerate(quest):
          questions[i][j] = word.lower()          
  return questions

# LOAD REQUIRED WORDS AND EXPORT LIKE A LIST OF WORDS
def load_requireds():  
  with open('required.txt', 'r') as f:
      strings = [line.splitlines() for line in f]
      requireds = [line[0].split() for line in strings]
      for i, quest in enumerate(requireds):
        for j, word in enumerate(quest):
          requireds[i][j] = word.lower()          
  return requireds


# IF THE QUESTION IS NOT CONTAINED, SET AN ALTERNATIVE ANSWER

nlp = en_core_web_sm.load() # load english interpretator only one time
def phase3(text):
  res = ''
  doc = nlp(text)
  for ent in doc.ents:
    if ent.label_ == 'ORG':
      res = '. I don’t work for ' + str(ent.text) + "."
      break
    elif ent.label_ == 'GPE':
      res = ". I’ve never been to " + ent.text + "."
      break
    else:
      for nc in doc.noun_chunks:
        res = " anything about " + nc.text + "."
        break
  return res

# COMPLEMENT OF PHASE3 FUNCTION
def random_string(input_string):
  try:
    response = "Sorry, I don't know about" + phase3(input_string)
  except:
    response = "Sorry, I don't know about it."
  return response