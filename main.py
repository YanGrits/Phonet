from os import path
from flask import Flask, send_from_directory, request, jsonify
import Transcription2
import Transcription


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/x-icon')


@app.route('/', methods=['GET'])
def getIndex() -> 'html':
    return app.send_static_file('html/index.html')


@app.route('/transcript', methods=['POST'])
def postTransript() -> str:
    text = request.form['userText']
    pickedLetters = request.form['pickedLetters']
    transcriptionMode = request.form['transcriptionMode']

    print(pickedLetters)

    if transcriptionMode == 'phonetic':
        result = Transcription.transcript_the_text_phonetic(
            text, pickedLetters)
    else:
        result = Transcription2.transcript_the_text_phonematic(
            text, pickedLetters)

    return jsonify(transcriptedText=result)
