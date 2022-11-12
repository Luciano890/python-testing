FROM python

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install fastapi uvicorn["standard"] jinja2 tornado motor multipart

CMD ["python", "main.py"]