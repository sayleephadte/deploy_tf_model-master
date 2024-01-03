## Prerequisites

* Installing required libraries
```sh
python3 -m pip install requirements.txt
```

## Execution

* execute the main file
```sh
python3 main.py
```

* open url on browser http://localhost:8000

## Directory Structure:

* templates: contains all html and css files
* main.py: main python file that runs the flask server
* nmt_model: contains file that load the model and translate text

## NGROK hosting

(Refer: https://ngrok.com/docs/getting-started/)

1. run the server `python3 main.py`

2. install ngrok agent

    Linux:

    ```sh
    curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
    sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
    sudo tee /etc/apt/sources.list.d/ngrok.list && \
    sudo apt update && sudo apt install ngrok
    ```

    Windows: `choco install ngrok`

3. Connect agent to ngrok account `ngrok config add-authtoken TOKEN`

4. Start ngrok `ngrok http 8000`
