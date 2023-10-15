# Ice Breaker

## Setup virtual environment
`python -m venv env`

## Activate virtual environment
`env\Scripts\activate.bat`

## Install libraries
```
pip install langchain
pip install black
```

- langchain: framework to build llm powered apps
- black: code formatter

## Add env file
- Create .env file
- 'Run and Debug' > Create JSON file > Add key value
  - `"envFile": "${workspaceFolder}/.env"`

## Format using Black
`python -m black ice-breaker.py`
