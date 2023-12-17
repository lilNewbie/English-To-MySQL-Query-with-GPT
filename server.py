import os
import openai
from openai import OpenAI, AzureOpenAI
from flask import Flask, render_template, request, jsonify
import json
import requests
import mysql.connector
from secrets import get_keys

openai_api_key, azure_api_key, azure_api_version = get_keys()
model = 'gpt-3.5-turbo-0613'
client = OpenAI(api_key=openai_api_key)
client2 = AzureOpenAI(
    azure_endpoint="https://dager1.openai.azure.com/",
    api_key=azure_api_key,
    api_version=azure_api_version
    )

#load the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password=""
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
        message = request.data.decode('utf-8')
    else:
        message = request.args.get("message")

    message=json.loads(message)
    tools = message['tools']
    msg = [{"role":"user","content":message['message']}]

    response="hehe"
    if 'sql' in message['message'].lower():
        response = client2.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=msg,
        tools=tools,
        tool_choice="auto",
    )
    
    response_content = response.choices[0].message.tool_calls[0].function.arguments
    r_str = response_content.split(":")
    r_str = r_str[1][1:-2]
    
    print(r_str)
    return r_str

if __name__ == "__main__":
    app.run(debug=True)
