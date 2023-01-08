FROM python:3

WORKDIR /usr/src/app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY welcome.py .

CMD python welcome.py
