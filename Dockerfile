FROM selenium/standalone-chrome:latest

USER root

WORKDIR /app

# Установка Python и зависимостей
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && apt-get clean

RUN ln -s /usr/bin/python3.10 /usr/bin/python

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "tests/test_login_page.py", "-v"]