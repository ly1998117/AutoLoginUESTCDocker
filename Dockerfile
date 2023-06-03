FROM python:3.10-slim
COPY src /Login
ENV NETWORK=uestc
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /Login
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["python", "always_online.py"]