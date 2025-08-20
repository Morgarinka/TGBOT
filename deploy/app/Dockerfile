FROM python:3.12-slim

WORKDIR /bot


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV TOKEN="8460331523:AAEqOP8SBmzy-fFeyZ09qfPUoP05wfd-HxQ"


ENV FLASK_APP=run.py
ENV FLASK_ENV=production

EXPOSE 5000


CMD ["start.py"]
