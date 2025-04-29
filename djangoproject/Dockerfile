# Python 3.11 이상 권장
FROM python:3.11-slim

# 작업 디렉토리 생성
WORKDIR /app

# 시스템 패키지 업데이트 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치용 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 포트 오픈
EXPOSE 8001

# 서버 실행 명령
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8001"]