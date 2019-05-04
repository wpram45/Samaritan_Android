
from flask import  Flask
import _thread
from flask import Flask,render_template,redirect,request,url_for,session
from flask_socketio import SocketIO,send,emit
import json
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from ast import literal_eval


app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/19'
app.config["CACHE_TYPE"] = "null"




socketio = SocketIO(app)








@app.route("/sendvoice",methods=['POST'])

def set_respond():
    respond="..."




    voice_string=str.split(request.data.decode(),":")[1][:-1]

    #value_dict=json.loads(data.decode())
  #  print(value_dict["value"])
     #print(value_dict["value"])


    chatbot = ChatBot('Samaritan')

# Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
    text=chatbot.get_response(voice_string)

 # print(text)


       # session["variable"]=text

    respond=text
    #global answer
   # answer=str(respond)







       # q.put(respond)
   # global thread_start
    #if thread_start==False:
     #   thread_start=True
      #  _thread.start_new_thread( background_stuff,(respond,))



    print(respond)

    #thinking=False
    return str(respond)







if __name__ =="__main__":

    socketio.run(app,host="0.0.0.0")




