# coding: utf-8
# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, request, jsonify
import fasttext as ft
from pretrain import keitaiso
from pretrain import nouns_extract
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

# Load the model
model = ft.load_model("./fasttext_with_Pretrain.model")
print("model loaded!")
 
@app.route('/predict_extract_nouns',methods=['POST'])
def predict():
    
    print("begin")
    data = request.get_json(force = True)
    text = data['predict']
    #形態素解析
    predictText = keitaiso(text)
    predictText = " ".join(nouns_extract(predictText))
    #予測
    labels, probs = model.predict(predictText.strip(), k= 10)
    for label, prob in zip(labels, probs):
        print(label, prob)
    result_dict = dict(zip(labels,probs))
    #確率が0.0001以下のを除く
    result_dict = {k:v for k, v in result_dict.items() if v >= 0.0001}
    #result_json = json.dumps(result_dict)
    return jsonify(result_dict)


if __name__ == '__main__':
    try:
        app.run(host= "0.0.0.0",port=5001, debug=True)
    except:
    	print("Server is exited unexpectedly. Please contact server admin.")
