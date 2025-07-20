# Gunakan base image Python
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /.

# Salin file dependency
COPY requirements.txt .

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh source code ke container
COPY . .

# Expose port (ubah sesuai aplikasi kamu)
EXPOSE 8000

# Jalankan aplikasi (ubah sesuai perintah aplikasi kamu)
CMD ["python", "app.py"]
