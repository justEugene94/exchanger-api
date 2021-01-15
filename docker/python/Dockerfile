FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    firefox-esr \
    chromium \
    git-core \
    xvfb \
    xsel \
    unzip \
    python-pytest \
    libncurses5 \
    libxml2-dev \
    libxslt-dev \
    libz-dev \
    xclip

# GeckoDriver v0.29.0
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz" -O /tmp/geckodriver.tgz \
    && tar zxf /tmp/geckodriver.tgz -C /usr/bin/ \
    && rm /tmp/geckodriver.tgz

# chromeDriver v87
RUN wget -q "https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ADD ./xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

# create symlinks to chromedriver and geckodriver (to the PATH)
RUN ln -s /usr/bin/geckodriver /usr/bin/chromium-browser \
    && chmod 777 /usr/bin/geckodriver \
    && chmod 777 /usr/bin/chromium-browser

RUN mkdir /code

WORKDIR /code

ADD ./requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt

ADD . /code/