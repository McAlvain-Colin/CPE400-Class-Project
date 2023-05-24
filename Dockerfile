FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git \
    && pip install pytest coverage

COPY driver.py TCP_unittest.py integreation_test.py /TCP/

WORKDIR /TCP

CMD ["python", "driver.py"]
