#!/usr/bin/env python
# coding: utf-8

# In[21]:


input_file = open('what_is_nlp.txt').read()
type(input_file)


# # The below code import the sentence tokenization library and toeknize the what_is_nlp.txt into sentences

# In[4]:


from nltk.tokenize import sent_tokenize
text = input_file #"God is Great! I won a lottery."
print(sent_tokenize(text))


# In[5]:


output_file = open('sen_output.txt','w')


# # Here the tokenized sentences in earlier step is retokenized in words

# In[23]:


from nltk.tokenize import word_tokenize
text = input_file#"God is Great! I won a lottery."
print("This tokenization prints all words including punctuation marks ")
print("-----------------------------------------------------------------------")
words_from_sentence =  word_tokenize(text)
print(word_tokenize(text))
print()


# # POS_Tagging for the words obtained in previous step

# In[26]:


import nltk
nltk.download('averaged_perceptron_tagger') 
allpos = nltk.pos_tag(words_from_sentence)


# In[31]:


allpos


# In[ ]:




