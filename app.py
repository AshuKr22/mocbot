from flask import Flask, render_template,request, jsonify
import  openai
from logging import FileHandler,WARNING
openai.api_key = " "



app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.get("msg1")
    
    input = msg
    return get_Chat_response(input)

def get_Chat_response(text):
     text= "tell me your name?"
     response = openai.Completion.create(engine="gpt-3.5-turbo-instruct" , prompt=text , max_tokens=100)
     return response["choices"][0]["text"]
   
    
    

if __name__ == '__main__':
    app.run(debug=True)