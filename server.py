import os
import openai
from openai import OpenAI, AzureOpenAI
from flask import Flask, render_template, request, jsonify
import json
import requests
import mysql.connector
from secrets1 import get_keys

openai_api_key, azure_api_key, azure_api_version, db_pwd = get_keys()
model = 'gpt-3.5-turbo-1106'

client = OpenAI(api_key=openai_api_key)

client2 = AzureOpenAI(
    azure_endpoint="https://dager1.openai.azure.com/",
    api_key=azure_api_key,
    api_version=azure_api_version
    )

#load the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_pwd
)

app = Flask(__name__)

def database_call(query):
    return query

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response", methods=['GET', 'POST'])
def get_response():
    if request.method == 'POST':
        #message = request
        message = request.data.decode('utf-8')
    else:  # This handles the GET request case
        message = request.args.get("message")

    message=json.loads(message)
    tools = message['tools']
    msg = [{ "role": "system","content": "Given the following SQL tables, your job is to write queries given a users request.\n  \n  create table mood_table(\n  sno int not null,\n  name varchar(20),\n  mood varchar(15),\n  primary key (sno)\n  );"}]
    msg.append({"role":"user","content":message['message']})

    response="hehe"
    if 'sql' in message['message'].lower():
        response = client.chat.completions.create(
            model=model,
            messages=msg,
            temperature=0.7,
            max_tokens=64,
            top_p=1
        )
        
    
    response_content = response.choices[0].message.content
    return response_content

if __name__ == "__main__":
    app.run(debug=True)
