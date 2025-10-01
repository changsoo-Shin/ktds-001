# Azure App Service 배포 가이드

## 배포 URL
- **프로덕션 URL**: https://travelguide01-ayg8egfwgebscmc5.koreacentral-01.azurewebsites.net

## 1. 필수 파일 확인

배포에 필요한 파일들이 모두 준비되어 있습니다:
- ✅ `requirements.txt` - Python 패키지 의존성
- ✅ `startup.sh` - Azure App Service 시작 스크립트
- ✅ `.streamlit/config.toml` - Streamlit 설정
- ✅ `app.py` - 메인 애플리케이션

## 2. Azure Portal 설정

### 2.1 애플리케이션 설정 (Configuration)

Azure Portal > App Service > Configuration > Application settings에서 다음 환경 변수를 설정하세요:

```
AZURE_ENDPOINT=<your-azure-openai-endpoint>
OPENAI_API_KEY=<your-openai-api-key>
OPENAI_API_VERSION=2024-02-15-preview

COMPUTER_VISION_KEY=<your-computer-vision-key>
COMPUTER_VISION_ENDPOINT=<your-computer-vision-endpoint>

WEATHER_API_KEY=<your-weather-api-key>

# 선택사항 (Azure AI Search 사용 시)
AZURE_SEARCH_ENDPOINT=<your-search-endpoint>
AZURE_SEARCH_KEY=<your-search-key>
AZURE_SEARCH_INDEX_NAME=travel_destinations
```

### 2.2 일반 설정 (General Settings)

Azure Portal > App Service > Configuration > General settings에서:

1. **스택 설정**:
   - Stack: Python
   - Python Version: 3.11 이상

2. **시작 명령어** (Startup Command):
   ```
   bash startup.sh
   ```

3. **Always On** (권장):
   - 항상 켜짐: On (앱이 유휴 상태에서도 깨어있게 유지)

## 3. 배포 방법

### 방법 1: GitHub Actions (권장)

1. GitHub 저장소와 연동:
   - Azure Portal > Deployment Center
   - Source: GitHub 선택
   - 저장소와 브랜치 선택
   - Azure가 자동으로 GitHub Actions 워크플로우 생성

2. 코드를 push하면 자동 배포:
   ```bash
   git add .
   git commit -m "Deploy to Azure"
   git push origin main
   ```

### 방법 2: Azure CLI

```bash
# Azure CLI 설치 후 로그인
az login

# 앱에 배포
az webapp up --name travelguide01-ayg8egfwgebscmc5 \
             --resource-group <your-resource-group> \
             --runtime "PYTHON:3.11"
```

### 방법 3: VS Code Azure Extension

1. VS Code에서 Azure Extension 설치
2. Azure 계정 로그인
3. App Service 우클릭 > Deploy to Web App

### 방법 4: Git 배포

```bash
# Azure 원격 저장소 추가
az webapp deployment source config-local-git --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>

# Git으로 배포
git remote add azure <deployment-url>
git push azure main
```

## 4. 배포 후 확인

### 4.1 로그 확인

```bash
# 실시간 로그 스트리밍
az webapp log tail --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>
```

또는 Azure Portal > Log stream에서 확인

### 4.2 애플리케이션 동작 확인

1. 브라우저에서 접속:
   https://travelguide01-ayg8egfwgebscmc5.koreacentral-01.azurewebsites.net

2. 주요 기능 테스트:
   - ✅ 메인 페이지 로드
   - ✅ 여행일정 생성
   - ✅ 이미지 분석
   - ✅ AI 상담 채팅

### 4.3 문제 해결

**앱이 시작되지 않는 경우:**
1. Log stream에서 오류 메시지 확인
2. 환경 변수가 올바르게 설정되었는지 확인
3. startup.sh 파일의 실행 권한 확인

**502 Bad Gateway 오류:**
1. 시작 명령어가 올바른지 확인
2. PORT 환경 변수를 올바르게 사용하는지 확인
3. 앱이 0.0.0.0 주소로 바인딩되는지 확인

**모듈을 찾을 수 없다는 오류:**
1. requirements.txt가 올바른지 확인
2. 배포 로그에서 패키지 설치가 성공했는지 확인

## 5. 성능 최적화

### 5.1 App Service Plan 업그레이드
- Basic 또는 Standard 플랜 사용 권장
- Always On 기능 활성화

### 5.2 애플리케이션 최적화
- 세션 상태 최소화
- 이미지 크기 제한
- 캐싱 활용

## 6. 비용 관리

- **Free/Shared Tier**: 개발/테스트용
- **Basic Tier (B1)**: 소규모 프로덕션 (~₩50,000/월)
- **Standard Tier (S1)**: 중규모 프로덕션 (~₩100,000/월)

## 7. 보안 체크리스트

- ✅ 환경 변수에 API 키 저장 (코드에 하드코딩 금지)
- ✅ HTTPS 강제 활성화
- ✅ 민감한 정보를 .gitignore에 추가
- ✅ 정기적으로 의존성 업데이트

## 8. 유용한 명령어

```bash
# 앱 재시작
az webapp restart --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>

# 앱 중지
az webapp stop --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>

# 앱 시작
az webapp start --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>

# 배포 이력 확인
az webapp deployment list-publishing-profiles --name travelguide01-ayg8egfwgebscmc5 --resource-group <your-resource-group>
```

## 지원

문제가 발생하면:
1. Azure Portal의 Log Stream 확인
2. Diagnostics and solve problems 도구 사용
3. Azure Support 문의

