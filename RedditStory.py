import praw
import threading
import time
import random
import story

def stream():
    for c in subreddit.stream.comments():
        commentList.append(c)

def commentReply():
    while(True):
        message = story.tree[0]['message'] + '\n\t'
        randNum = random.randrange(len(commentList) - 20,len(commentList))
        commentList[randNum].reply(message)
        print('replied to \n' + commentList[randNum].body)
        authorList.append(commentList[randNum].author)
        time.sleep(900)

def checkMail():
    while True):
        for mail in r.get_unread(limit=None):
            if (mail.author is in authorList):
                #check game state for author
                #read comment contents
                #if valid
                    #send next state
                #else send 'not valid'
            else:
                mail.mark_as_read()

def getMessage(branch):
    message = story.tree[branch]['message'] 
    options = []
    for op in story.tree[branch]['options'].keys():
        options.append(op)
    

    
    

        
commentList = []
authorDictionary = {}
replyList = []

UA = 'Reddit Text Adventure demo, Created by Me'
r = praw.Reddit(UA)

user = 'TestyTest42'
password = 'tUbUCSEQ7p9mbcYC'

r.login(user, password, disable_warning=True)

subreddit = ''myPrivateSubreddit42'

streamThread = threading.Thread(target=stream)
streamThread.start()
print('Stream started')

commentThread = threading.Thread(target=commentReply)
commentThread.start()
print('Comment started')


    


def Message(branch):
	message = story.tree[branch]['message'] + '\n\n'
	for op in story.tree[branch]['options'].keys():
		message += '* ' + op + '\n\n'
	return message

    comments[1].reply(Message(0))
Comment(id='datrccv')
