#!/bin/bash
# Azure App Service 시작 스크립트

# PORT 환경 변수가 설정되어 있으면 사용하고, 없으면 기본값 8000 사용
PORT="${PORT:-8000}"

# Streamlit 앱 실행
python -m streamlit run app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false

