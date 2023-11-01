FROM python:3.11-slim

# load api
RUN groupadd apigroup && useradd -m -g apigroup -s /bin/bash api
RUN echo "api ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir -p /home/fastapi/app/api
WORKDIR /home/fastapi/app/api
COPY main.py .
COPY requirements.txt .
COPY prod.sh .
RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R api:apigroup /home/fastapi
ENTRYPOINT [ "sh", "/home/fastapi/app/api/prod.sh" ]
USER api