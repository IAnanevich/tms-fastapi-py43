FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

#
RUN pip3 install pipenv

#COPY requirements.txt .
COPY Pipfile .
COPY Pipfile.lock .

#RUN pip3 install -r requirements.txt
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
