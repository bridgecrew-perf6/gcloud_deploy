# gcloud_deploy
Hello! This is a very simple Flask app (an emoji parser) for purposes of testing Google Cloud's App Engine.   
As of writing, the url is live (i.e. the attempt worked), but as of reading, 🤷

The site uses Python/Flask and has two basic endpoints:

/?emoji={emoji_name}    
This returns a welcome message where {emoji_name} is one of the emoji strings returned by /all.    
If emoji_name == None, it gives a welcome message.   
Sample route: https://bpoeter-trial.uc.r.appspot.com/?emoji=snake

/all   
Returns a dictionary of all the emojis and their names from emojis.txt.   
You can use any of these in the ?emoji= route above.   
Sample usage: https://bpoeter-trial.uc.r.appspot.com/all

