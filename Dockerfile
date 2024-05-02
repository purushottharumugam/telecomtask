FROM python:3.11
COPY . /app
WORKDIR /app
RUN useradd -ms /bin/bash myuser
RUN chown -R myuser:myuser /app
RUN pip install -r requirements.txt
WORKDIR /app/telecom
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
