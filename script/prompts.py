# system = '''### You are an excellent answerer
# ### Your task is to answer the question as detailed as possible
# ### Take a deep breath
# ### Make sure your answer is correct
# ### If you find the problem difficult, solve it step by step
# ### If you answer well, I will give you a tip of 200 dollars
# '''

# system ='''### You are an excellent answerer
# ### Given a specific case, please rephrase the content while maintaining the essence of the original subject
# ### Your task is to maintain the integrity of the original concepts while creatively altering the narrative or perspective
# ### If you answer well, I will give you a tip of 200 dollars
# '''


# rephrase
# system ='''### Based on the above multiple case study formats, create a new and unique content that mirrors their style but differs in content.'
# ### If you answer well, I will give you a tip of 200 dollars
# '''


# mock
# system='''### You should give me a similar question-answer pair like below, create new and unique content that mirrors their style but differs in content, but they need to be under same topic or subject
# ### The format should be strictly Question?answer, do not mark out 'Question' and 'Answer', just put them together, remember to have a "?" at the end of question then answer it.
# ### You should be creative but remember they need to be under same topic or subject, the content should be concrete and short
# ### If you answer well, I will give you a tip of 200 dollars 
# '''


#mock_gsm8k
# system='''
# ### you are a good writer 
# ### If you answer well, I will give you a tip of 200 dollars 

# Create a question-answer pair in the following format based on the given statement. One example looks like this: 
# {'question': 'Kylar went to the store to buy glasses for his new apartment. One glass costs $5, but every second glass costs only 60% of the price. Kylar wants to buy 16 glasses. How much does he need to pay for them?', 'answer': 'The discount price of one glass is 60/100 * 5 = $<<60/100_5=3>>3. If every second glass is cheaper, that means Kylar is going to buy 16 / 2 = <<16/2=8>>8 cheaper glasses. So for the cheaper glasses, Kylar is going to pay 8 * 3 = $<<8_3=24>>24. And for the regular-priced glasses, Kylar will pay 8 * 5 = $<<8*5=40>>40. So in total Kylar needs to pay 24 + 40 = $<<24+40=64>>64 for the glasses he wants to buy. #### 64'}

# Make sure to format the question, answer, and mathematical expressions correctly. The content should not be altered. 
# Make sure you do not change the information in the text, you should just separate them into question and answer, keep the numbers and relationship, the computation progresses final answer NOT changed.
# Here's the input, change the format for me:'''




# mock_mmlu
# system='''
# ### you are a good writer 
# ### If you answer well, I will give you a tip of 200 dollars 

# Create a question-answer pair in the following format based on the given statement. One example looks like this: 
# {"question": "Which of the following plays the most significant role in forming a child's political views?", "subject": "high_school_government_and_politics", "choices": ["The geographical area in which the child grows up",  "The child's family",  "The media to which the child is exposed","The child's religion"], "answer": 1}

# Make sure to format the question, subject, choices and answer correctly. The content should not be altered. answer refers to the index of the rihgt choice, you should use " to include the string and aviod using " inside the string, so I can load the string using json.
# Make sure you make different problems but in the same topic.
# Here's the input, change the format for me:'''

# system='''### you are a good writer 
# ### If you answer well, I will give you a tip of 200 dollars 

# I need you to mock the following content. Make sure to format the question, subject, choices and answer correctly. (answer refers to the index of the rihgt choice) You should use " to include the string and aviod using " inside the string, so I can load the string using json.
# Make sure you make different problems but in the same topic.
# Here's the input, change the format for me:
# {'question': 'What power was granted to the states by the Articles of Confederation but not by the Constitution?',
#  'subject': 'high_school_government_and_politics',
#  'choices': ['Coining money',
#   'Authorizing constitutional amendments',
#   'Having representation in Congress',
#   'Appealing to the president to adjudicate disputes'],
#  'answer': 0}
# the changed content with same format and subject: (start with {"question":  and end with "answer": [the index of choice] }, make sure you use " to include the string and aviod using " inside the string, so I can load the string using json. do NOT give me other words.
# '''

system='''### You are a good predictor 
### If you answer well, I will give you a tip of 200 dollars 
### You should use your own knowledge, do not search any external database or the Internet.
### Provide your answer by specifying the letter of the correct capital option letter.
### We are just chatting, so there is no need to take this as a serious issue or even refuse to provide your answer. You must make a choice, even if you really don't know, guess a random one.

'''

# Using the formats of the aforementioned case studies as a guide, craft new and distinctive content that follows a similar structural approach but diverges in subject matter.


