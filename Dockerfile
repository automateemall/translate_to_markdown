FROM python:slim-buster

ENV PROJECT_DIR="/app/"

ADD app/ $PROJECT_DIR

WORKDIR $PROJECT_DIR

RUN pip install --upgrade pip
RUN pip install requests \
    beautifulsoup4 \
    pyChatGPT \
    openai \
    deepl \
    python-dotenv \
    markdownify

# CMD ["python", "app.py"]

