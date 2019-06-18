# def input(x):
#     return 'this function returned ' + x
# from nltk.chat.util import Chat, reflections
from chatapp import Database_connection
#import chatbot
# import math


conversations={}
class MyClass:
    def __init__(self,val):
        self.val=val
def chatty(user):

    # print(
    #     "Welcome To Virtusa!!!\nPlease type lowercase English language to start a conversation.\nType 'quit' to leave ")  # default message at the start

    print(user)
    #
    mydict=Database_connection.sql(user)
    print(mydict)
    return mydict
    #conversation(user)
# def conversation(user):
#
#     chat = Chat(pairs, reflections)
#     chat.converse()
#