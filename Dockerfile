FROM python:3.9 AS base
WORKDIR /app

COPY ./data_collectors /app/data_collectors
COPY ./data_storage /app/data_storage

FROM base AS App_Sumo
WORKDIR /app

COPY ./docker/App_Sumo /app
RUN pip install -r requirements.txt
CMD python main.py

FROM base AS Product_Hunt
WORKDIR /app

COPY ./docker/Product_Hunt /app
RUN pip install -r requirements.txt
CMD python main.py

FROM base AS SaaS_Worthy
WORKDIR /app

COPY ./docker/SaaS_Worthy /app
RUN pip install -r requirements.txt
CMD python main.py

