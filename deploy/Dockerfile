FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install additional dependencies
RUN pip install transformers

# Copy FastAPI app code into container
#can copy the requirement file 
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /app 
COPY . /app
CMD ["python", "app.py"]