import nltk
from nltk.stem.lancaster import *

stemmer =LancasterStemmer()
training_data = []
training_data.append({"class":"Air-Conditioning", "sentence":"can you lower my room temperature?","response":"For Air Conditioning related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"Air-Conditioning", "sentence":"can you increase my room temperature?","response":"For Air Conditioning related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"Air-Conditioning", "sentence":"i need to adjust room temperature","response":"For Air Conditioning related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"Air-Conditioning", "sentence":"i request for AC support?","response":"For Air Conditioning related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})

training_data.append({"class":"goodbye", "sentence":"have a nice day","response":"Thank you for visiting Anytime Service Desk"})
training_data.append({"class":"goodbye", "sentence":"see you later","response":"Thank you for visiting Anytime Service Desk"})
training_data.append({"class":"goodbye", "sentence":"bye","response":"Thank you for visiting Anytime Service Desk"})
training_data.append({"class":"goodbye", "sentence":"talk to you soon","response":"Thank you for visiting Anytime Service Desk"})

training_data.append({"class":"House-Keeping", "sentence":"can you clean my workstation?","response":"For House-Keeping related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"House-Keeping", "sentence":"can you clean my WS?","response":"For House-Keepingg related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"House-Keeping", "sentence":"can you clean ?","response":"For House-Keeping related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})
training_data.append({"class":"House-Keeping", "sentence":"i request for cleaning of room?","response":"For House-Keeping related issues please raise a ticket at https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"})

training_data.append({"class":"Greeting", "sentence":"Hello","response":"Hey user ! Welcome to Virtusa \n How can I help you"})
training_data.append({"class":"Greeting", "sentence":"Hi","response":"Hey user ! Welcome to Virtusa \n How can I help you"})
training_data.append({"class":"Greeting", "sentence":"Wassup ?","response":"Hey user ! Welcome to Virtusa \n How can I help you"})
training_data.append({"class":"Greeting", "sentence":"What's up?","response":"Hey user ! Welcome to Virtusa \n How can I help you"})
training_data.append({"class":"Greeting", "sentence":"Hey?","response":"Hey user ! Welcome to Virtusa \n How can I help you"})

training_data.append({"class":"Wishes", "sentence":"Good Morning"})
training_data.append({"class":"Wishes", "sentence":"Good Evening"})
training_data.append({"class":"Wishes", "sentence":"Morning"})
training_data.append({"class":"Wishes", "sentence":"Good Night"})
training_data.append({"class":"Wishes", "sentence":"Night"})
training_data.append({"class":"Wishes", "sentence":"Good Afternoon"})
training_data.append({"class":"Wishes", "sentence":"Afternoon"})
training_data.append({"class":"Wishes", "sentence":"Evening"})




response={"Air-Conditioning":["For Air Conditioning related issues please raise a ticket at" ,"https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"],
         "goodbye":"Thank you for visiting Anytime Service Desk","House-Keeping": ["For House-Keeping related issues please raise a ticket at ","https://virtusa.service-now.com/sp?id=sc_category&sys_id=c24ff37adb2f3a405eb551b0cf961902"],None:"Sorry I can't understand you,please try again","Greeting":"Hey user ! Welcome to Virtusa \n How can I help you"   }
# capture unique stemmed words in the training corpus
corpus_words = {}
class_words = {}
# turn a list into a set (of unique items) and then a list again (this removes duplicates)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepare a list of words within each class
    class_words[c] = []

# loop through each sentence in our training data
for data in training_data:
    # tokenize each sentence into words
    for word in nltk.word_tokenize(data['sentence']):
        # ignore a some things
        if word not in ["?", "'s"]:
            # stem and lowercase each word
            stemmed_word = stemmer.stem(word.lower())
            # have we not seen this word already?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # add the word to our words in class list
            class_words[data['class']].extend([stemmed_word])


def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
    # tokenize each word in our new sentence
    for word in nltk.word_tokenize(sentence):
        # check to see if the stem of the word is in any of our classes
        if stemmer.stem(word.lower()) in class_words[class_name]:
            # treat each word with relative weight
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score

def classify(sentence):
    high_class = None
    high_score = 0
    # loop through our classes
    for c in class_words.keys():
        # calculate score of sentence for each class
        score = calculate_class_score(sentence, c,show_details=False)
        # keep track of highest score
        if score > high_score:
            high_class = c
            high_score = score

    return high_class #high_score
#print(classify("can you clean my place?"))
#print(classify("bye good night"))
def solution(user):
    resp=classify(user)
    if resp=='Wishes':
        return user+"!"
    else:
        return (response[resp])