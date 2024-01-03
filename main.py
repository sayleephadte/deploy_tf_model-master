from flask import Flask, render_template, request,jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

config_file=os.path.abspath('config.env')
load_dotenv(config_file,override=True)

#load the tensorflow model
import nmt_model.model as NMT

app = Flask(__name__)
CORS(app)

MODEL_EN_KOK_PATH = os.environ['MODEL_EN_KOK_PATH']
MODEL_KOK_EN_PATH = os.environ['MODEL_KOK_EN_PATH']

#loading the models from tensorflow SavedModel format
model_ek = NMT.load_model(MODEL_EN_KOK_PATH)
model_ke = NMT.load_model(MODEL_KOK_EN_PATH,model_type='KE')

def translate(lang:str,input_text:str):

    translated_sentence = 'init'

    if lang.lower() in ['en','eng','english']:
        target_lang = 'Konkani'
        translated_sentence = model_ek(input_text).numpy().decode()
    elif lang.lower() in ['kok','gom','konkani']: 
        target_lang = 'English'
        translated_sentence = model_ke(input_text).numpy().decode()
    else:
        return "Invalid input language!"

    output = {
                'source':input_text,
                'target': translated_sentence,
                'target_lang':target_lang,
            }
    print("JSON response:\n",output)
    return jsonify(output)

# @app.before_request
# def handle_preflight():
#     if request.method == "OPTIONS":
#         res = Response()
#         res.headers['X-Content-Type-Options'] = '*'
#         return res

@app.route('/', methods=['GET', 'POST'])
def index():
    output = {
                "Message":"TranslateKar Welcomes you!",
                "Endpoints":{
                            'Two-way Translations: (GET,POST)':{
                                'endpoint':'/translate',
                                'params':['lang','input'],
                            },
                            'English to Konkani (POST)':{
                                'endpoints':'/translate/en-kok',
                                'params':['input'],
                            },
                            'Konkani to English (POST)':{
                                'endpoints':'/translate/kok-en',
                                'params':['input'],
                            },
                        },
                "Response params":
                    {   
                        'source':'(str) input string passed as request',
                        'target':'(str) translated string',
                        'target_lang':'(str) langauge of translated string'
                    },
              }
    return jsonify(output)

@app.route('/translate/', methods=['GET','POST'])
def handle_request():
    if request.method == 'GET':
        lang = request.args.get('lang')
        input_text = request.args.get('input')

    elif request.method == 'POST':
        lang = request.json['lang']  
        input_text = request.json['input']
    else:
        return "Invalid request method!"
    return translate(lang,input_text) 

@app.route('/translate/en-kok/', methods=['POST'])
def translate_EK():
    input_text = request.json['input']
    return translate("en",input_text)

@app.route('/translate/kok-en/', methods=['POST'])
def translate_KE():
    input_text = request.json['input']
    return translate("kok",input_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True,use_reloader=False)
