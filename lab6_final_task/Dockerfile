FROM python:3.11-slim

WORKDIR /project

COPY lab6_final_task/requirements.txt lab6_final_task/requirements.txt

RUN pip install --no-cache-dir -r lab6_final_task/requirements.txt

COPY lab6_final_task lab6_final_task

EXPOSE 8000

CMD ["uvicorn", "lab6_final_task.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
