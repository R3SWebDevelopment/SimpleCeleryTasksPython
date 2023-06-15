FROM python as base

RUN apt-get update

FROM base

WORKDIR /src

COPY src/ /src/

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["flask", "--app", "app", "run", "--host=0.0.0.0"]