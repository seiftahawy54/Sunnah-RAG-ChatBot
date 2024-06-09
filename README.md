# Simple RAG ChatBot for answering questions about sunnah
### (Bukhari Correct Book version only)

## Prerequistes
- Python `12.13.1`

## Installation Guide
- Clone `https://github.com/seiftahawy54/Sunnah-RAG-ChatBot.git` then `cd Sunnah-RAG-ChatBot`
- Add `.env` file
  - `OPENAI_KEY` to start to connect to OpenAI's LLMs.
- Install python run `pip install -r requirements.txt`
- Start By creating the db by running ```python3 create_db.py```
- Wait until db is created and ``chroma`` directory to be created.
- To Start questioning the model and retireve back answers
  - Run ```python3 query.py {Question} {Lang}```
    - Currently to get answers in Arabic Or English you should specify the language. (Auto Detector will be added later)


## Contribution
- Feel free to fork start updating or open a PR.
