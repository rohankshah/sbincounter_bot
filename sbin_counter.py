import praw
from time import gmtime, strftime
import time
import os

def login():
    reddit = praw.Reddit(client_id = os.environ.get('client_id'),
                         client_secret = os.environ.get('client_secret'),
                        user_agent="sbincounter",
                        username = os.environ.get('username'),
                        password = os.environ.get('password'))
    print('Logged in! ')
    return reddit

def run_bot(reddit):
    fdank = reddit.subreddit('formuladank')

    count = 1
    start_time = "\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

    for comments in fdank.stream.comments(skip_existing=True):
            print(comments.body)
            if 'sbin' in comments.body.lower() or 's🅱️in' in comments.body.lower():
                count += 1
                count_path = os.path.join(os.getcwd(), 'count.txt')
                count_file = open(count_path, 'a')
                count_file.truncate(0)
                file.write(count)
            if count%10 == 0:
                bot_msg = "I am a bot that counts the number of time S BIN has been commented.\n"
                blank_space = "                                 "
                sbin_msg = "This is the " +str(count) +"th time the word 'S BIN' has been used since I started counting on " +start_time
                reply = bot_msg +blank_space +sbin_msg
                print(reply)
                comments.reply(reply)
                path = os.path.join(os.getcwd(), 'sbin_logs.txt')
                file = open(path, 'a')
                file.write(reply)
                file.write('\n')
                file.close

while True:
    reddit = login()
    run_bot(reddit)
