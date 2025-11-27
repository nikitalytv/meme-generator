FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y \
    fonts-dejavu-core && \
    pip install --no-cache-dir flask pillow
ENV PORT=5000
EXPOSE 5000
CMD ["python", "app.py"]
