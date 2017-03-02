import tweepy
import random
from tkinter import *

def make_tweet():
	ag = open('againstme.txt', 'r')
	jb = open('JebBush.txt', 'r')
	ag_read = ag.read()
	jb_read = jb.read()
	ag_read = ag_read.split('\n')
	jb_read = jb_read.split('\n')
	ag_tweet = random.choice(ag_read)
	jb_tweet = random.choice(jb_read)

	tweet.config(text = ag_tweet + ' / ' + jb_tweet)

def send_tweet():
	auth = tweepy.OAuthHandler('g50EQnY1xcE2dnqfjrpPP4LM9', 'D6T4Qg7gkpxo1AKvvqxzblivUwUhDKQ6rxXSHKbBewmVrjqdlL')
	auth.set_access_token('825470930688364550-P9EOzcwAJnJoL9tpEZ4VzthTgOBjJ82', 'xJjXSMtX8zHI0kV7D5em4MOn8q7xXwMCe0YVt95FfipU3')
	api = tweepy.API(auth)
	status = tweet.cget('text')
	api.update_status(status)

def save_tweet():
	to_save = tweet.cget('text')
	saved_tweets = open('saved_tweets.txt', 'a+')
	saved_tweets.write(to_save + '\n')
	saved_tweets.close()	

root = Tk()

root.title('Against Jeb!')

gbutton = Button(root, text = 'Generate Quote', command = make_tweet)
gbutton.pack()

tweet = Label(root)
tweet.pack()

sbutton = Button(root, text = 'Send Tweet', command = send_tweet)
sbutton.pack()

savebutton = Button(root, text = 'Save', command = save_tweet)
savebutton.pack()

photo = PhotoImage(file = "jeb.pgm")
Jeb_pic = Label(root, image = photo)
Jeb_pic.image = photo
Jeb_pic.pack()

root.mainloop()






