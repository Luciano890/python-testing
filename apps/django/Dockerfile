FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app_test/manage.py", "runserver", "0.0.0.0:8000"]
