FROM python:3.9
COPY . /app
WORKDIR /app/Context-Aware-Recommendation
# RUN pip install -r ../requirements.txt
CMD [ "uvicorn ../Context-Aware-Recommendation.main:app --reload" ]