# Python image
FROM python:3.10

# Work directory
WORKDIR /backend

# requirements faylini copy
COPY requirements.txt .

# Django o'rnatamiz
RUN pip3 install --no-cache-dir -r requirements.txt

# Loyihani copy qilamiz
COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
