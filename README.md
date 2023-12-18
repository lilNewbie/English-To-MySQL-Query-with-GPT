# English-To-MySQL-Query-with-GPT 👨‍💻

This repository contains the files used to create this custom GPT which converts natural language (English) into MySQL queries and then responds based on the information retrieved.

## Features

- Chatbot-like interface using Streamlit
- Uses the OpenAI's Completions API
- Uses a Flask API which retrieves queries from the [Chat Complations API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) and accesses the MySQL database


## Run Locally

Clone the project

```bash
  git clone https://github.com/lilNewbie/English-To-MySQL-Query-with-GPT.git
```

Go to the project directory

```bash
  cd English-To-MySQL-Query-with-GPT
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Update the following API Keys in the `secrets1.py` file.

`openai_api_key`
`azure_api_key`
`azure_api_version`
`db_pwd`
`azure_ep`

I have added an option to use Azure OpenAI's API key along with OpenAI's API Key
```python
client = OpenAI(api_key=openai_api_key)

client2 = AzureOpenAI(
    azure_endpoint=azure_ep,
    api_key=azure_api_key,
    api_version=azure_api_version
    )
```

Run the web-app

```bash
  streamlit run sqlquery.py
```

Run the server
```bash
  flask --app server.py run
```

## Demo
Type in your query in English and wait!
![sqlImage](https://github.com/lilNewbie/English-To-MySQL-Query-with-GPT/assets/90834922/100b2e2c-27fa-4b32-a526-44aef4b509b7)

I printed the SQL queries and the responses when testing the app
![sqlImage2](https://github.com/lilNewbie/English-To-MySQL-Query-with-GPT/assets/90834922/3c5622f4-e91a-4e94-8e6c-8d6890bd879e)



