

import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables
yourkey = 'f53dbf0f' #defined my botkey 
bot_id = '5902734806:AAHPMTY931Nzslg-SkuU43Na6VuVozxrn5o' #defined my bot id 

bot = telebot.TeleBot(bot_id) #this is the bot (i think)

@bot.message_handler(commands=['start', 'hello']) #keywords that'll get my boi going 
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, "hello! i am a (slightly slow) bot programmed to provide you with information on any movie that you would like. I can also export these details in the form of a CSV file") #this is what he'll tell the user

@bot.message_handler(commands=['stop', 'bye']) #keywords that'll get my boi stopped
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'okayy byee, come back again!') #what he'll say



@bot.message_handler(func=lambda message: botRunning, commands=['help', 'commands']) #main commands to get info about a movie 
def helpProvider(message):
    bot.reply_to(message, '1.0 you can use \"/movie your_movie\" command to get the details of a particular movie. For eg: \"/movie the shawshank redemption\"\n\n2.0. you can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. you can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie']) #if the user wants movie info, pull api info from the omdb website 
def getMovie(message):
    bot.reply_to(message, "hold on just one sec, i'll get you info on that movie...")
    response_API = requests.get('https://www.omdbapi.com/')


# TODO: 1.2 Get movie information from the API
    movie_name = message.text
    print (movie_name)
    text2 = movie_name.replace('/movie ', '')
    print(text2)


    global moviedetails
    moviedetails = []
    reqs = requests.get(f"https://www.omdbapi.com/?apikey=f53dbf0f&t={text2}") #the GET request with my api key 
    

    # TODO: 1.3 Show the movie information in the chat window

    data = json.loads(reqs.text)
    print(data)
    moviedetails.append(data['Title'])
    moviedetails.append(data['Year'])
    moviedetails.append(data['Runtime'])
    moviedetails.append(data['imdbRating'])
    moviedetails.append(data['Director'])
    caption = "Title: "+moviedetails[0] + '\n' + "Year of release: " + moviedetails[1] + '\n' + "Runtime: " + moviedetails[2] + '\n' + "IMDB Rating: " + moviedetails[3] + '\n' + moviedetails[4]

    print ("reached")
    photo_url = data["Poster"]
    #photo_request = requests.get(photo_url)    
    bot.send_photo(message.chat.id, photo_url, caption=caption)
    

    
# TODO: 2.1 Create a CSV file and dump the movie information in it
    csvheader = ['title','year', 'director', 'imdbRating']
    with open ('telegram_movie.csv','w', encoding = 'UTF8', newline = '') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(csvheader)
        writer.writerow(moviedetails)

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    #TODO: 2.2 Send downlodable CSV file to telegram chat
    moviedocdownloadable = open ('telegram_movie.csv', 'rb')
    bot.send_document(message.chat.id, moviedocdownloadable)

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.infinity_polling()
