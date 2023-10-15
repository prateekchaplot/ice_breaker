# Ice Breaker

## Setup virtual environment
`python -m venv env`

## Activate virtual environment
`env\Scripts\activate.bat`

## Install libraries
```
pip install langchain
pip install openai
pip install googlesearch-python
```

- langchain: framework to build llm powered apps
- openai: chat model

## Add env file
- Create .env file
- 'Run and Debug' > Create JSON file > Add key value
  - `"envFile": "${workspaceFolder}/.env"`

## Format using Black
`python -m black ice-breaker.py`
