FROM python:3.12.9-slim

WORKDIR /app

COPY ./src .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["/bin/bash"]