from machinetranslation import translator
from translator import english_to_french,french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = english_to_french(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = french_to_english(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    return "Translation Service between English and French"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
