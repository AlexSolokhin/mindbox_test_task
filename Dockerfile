FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /mindbox_test_task
RUN pip install --upgrade pip

COPY requirements.txt /mindbox_test_task/
COPY product_api /mindbox_test_task/product_api
COPY session_id /mindbox_test_task/session_id

RUN python -m pip install -r /mindbox_test_task/requirements.txt

WORKDIR /mindbox_test_task/product_api/product_catigorizer

RUN python manage.py migrate
RUN python manage.py loaddata categories.json
RUN python manage.py loaddata goods.json

EXPOSE 5000

CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
