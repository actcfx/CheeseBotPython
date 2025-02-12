# 使用官方的 Python 基礎映像
FROM python:3.13.2-slim

# 設置工作目錄
WORKDIR /app

# 複製當前目錄的內容到容器的 /app 目錄
COPY . /app

# 安裝依賴包
RUN pip3 install --no-cache-dir -r requirements.txt

# 運行主程序
CMD ["python", "main.py"]
