'''
Created on Dec. 24th, 2020
Author: /u/goldbludgeon

PRAWS Version: 7.1.0

You must install python 3.9 and PRAW v7.1.0! If you do not know how a google search will help.

Make sure to fill in the username and password fields below. Make sure you keep the quotes around the fields.

You'll need to make a "user script" in your reddit profile to run this.
Go to https://old.reddit.com/prefs/apps/
Click on "Develop an app" at the bottom.
Give it a random name. Doesn't matter.
You need to fill in the "Redirect URI" field with something so go ahead and put 127.0.0.0 in there.
Save it.

The client ID is the 14 character string under the name you gave your script.
It'll look like a bunch of random characters like this: pspYLwDoci9z_A

The client secret is the longer string next to "secret".

Replace those two fields below. Again keep the quotes around the fields.
Save this file as "clearposts.py"

Double click the file to run it.

You are good to go!

'''
import time
import praw

try:
    r = praw.Reddit(
            user_agent = "Clear Saved Posts",
            username = "YOUR_USERNAME", #replace with your username
            password = "YOUR_PASSWORD", #replace with your password
            client_id = "CLIENT_ID_FROM_USER_APPS", #replace with client ID
            client_secret = "CLIENT_SECRET_FROM_USER_APPS" #replace with client secret
            )


    for saved in r.user.me().saved(limit=1000):
        if type(saved) == type(r.submission(id = str(saved))):
            r.submission(id = str(saved)).unsave()
        if type(saved) == type(r.comment(id = str(saved))):
            r.comment(id = str(saved)).unsave()

except:
    print("Something went wrong. Did you install PRAW? Did you change the user login fields?")

else:
    print("Done! Thanks for playing!")
    time.sleep(3)
