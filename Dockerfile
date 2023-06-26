FROM python:3.9

WORKDIR /app

COPY Requirements.txt .
# RUN pip install --no-cache-dir -r Requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
