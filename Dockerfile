FROM python:3.10
COPY . .
RUN pip install pytest
CMD ["python","app.py"]