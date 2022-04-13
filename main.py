import emoji
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    emoji_requested = request.args.get('emoji')
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