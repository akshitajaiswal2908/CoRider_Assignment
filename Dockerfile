FROM python:3.12-slim
WORKDIR /
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]
