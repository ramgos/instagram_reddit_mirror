#!/bin/bash

FROM python:3.7

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod a+x run.sh

CMD ["./run.sh"]