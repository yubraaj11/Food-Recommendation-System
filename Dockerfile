FROM python:3.9-slim    
WORKDIR /app
COPY .  .
EXPOSE 8000
# CMD [ "uvicorn", "Context-Aware-Recommendation", ".", "main:app", "--reload" ]
