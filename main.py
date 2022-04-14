import emoji
import json
from flask import Flask, request

WELCOME_STRING = "human! Check out /all to see which emoji strings /?emoji={emoji_string} can find"

app = Flask(__name__)

@app.route('/')
def welcome():
    emoji_requested = request.args.get('emoji')
    if not emoji_requested is None:
        if not emoji_requested[0] == ':':
            emoji_requested = ":" + emoji_requested
        if not emoji_requested[-1] == ":":
            emoji_requested = emoji_requested + ":"
    else:
        emoji_requested = WELCOME_STRING        
    message = emoji.emojize(f'Hello {emoji_requested}!')
    return message

@app.route('/all')
def all_emojis():
    emojis = {}
    with open('emojis.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            emojis[line] = emoji.emojize(line)
    return json.dumps(emojis, ensure_ascii=False)

if __name__ == '__main__':
    app.run('127.0.0.1', '65507')    