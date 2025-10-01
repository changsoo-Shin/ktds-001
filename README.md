# 🧳 AI 여행 플래너

Azure OpenAI와 LangChain을 활용한 지능형 여행일정 추천 서비스입니다.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red.svg)](https://streamlit.io)
[![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-GPT--4-green.svg)](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 프로젝트 개요

MS Azure AI 서비스를 활용한 올인원 여행 계획 도우미입니다. 사용자가 원하는 여행지, 기간, 스타일, 예산을 입력하면 AI가 최적화된 맞춤형 여행일정을 자동으로 생성합니다. 이미지 분석을 통한 여행지 추천, 실시간 날씨 정보, AI 채팅 상담까지 제공하는 종합 여행 플래닝 서비스입니다.

### 🌐 데모 사이트
- **프로덕션 URL**: https://travelguide01-ayg8egfwgebscmc5.koreacentral-01.azurewebsites.net

## ✨ 주요 기능

### 🗺️ 맞춤 여행일정 생성
- **스마트 일정 생성**: 여행지, 기간, 스타일, 예산에 맞춘 AI 기반 최적 일정 생성
- **다양한 여행 스타일**: 관광 중심, 휴양 중심, 문화 체험, 맛집 탐방, 자연 탐험, 쇼핑 등
- **예산별 추천**: 저예산(일 5만원 이하), 중간(일 5-10만원), 고급(일 10만원 이상)
- **날짜 지정**: 사용자가 원하는 여행 시작일 설정 가능
- **일정 내보내기**: 생성된 일정을 텍스트 파일로 다운로드
- **RAG 기술**: LangChain과 Azure OpenAI를 활용한 정확한 여행 정보 제공

### 📸 AI 이미지 분석
- **비전 AI 분석**: Azure Computer Vision을 활용한 고급 이미지 인식
- **자동 장소 인식**: 업로드한 사진에서 랜드마크, 풍경, 건축물 등 자동 감지
- **스마트 추천**: 이미지 특성을 분석하여 유사한 특색의 여행지 추천
- **태그 기반 분류**: 이미지에서 추출된 태그를 기반으로 여행 스타일 파악

### 💬 AI 여행 상담 챗봇
- **실시간 대화**: GPT-4 기반 자연스러운 대화형 인터페이스
- **맞춤형 조언**: 여행 계획, 관광지 정보, 현지 문화 등 다양한 질문 답변
- **대화 히스토리**: 이전 대화 내용을 기억하는 컨텍스트 유지
- **친근한 응답**: 이모지와 친근한 톤으로 사용자 경험 향상

### 🌤️ 실시간 날씨 정보
- **현재 날씨**: OpenWeatherMap API를 통한 전 세계 도시 날씨 정보
- **상세 기상 데이터**: 온도, 체감온도, 습도, 날씨 설명
- **여행 준비 도움**: 날씨에 따른 여행 준비물 조언

## 🚀 설치 및 실행

### 사전 요구사항
- Python 3.11 이상
- Azure OpenAI 서비스 구독 (필수)
- Azure Computer Vision 서비스 (선택)
- OpenWeatherMap API 키 (선택)
- Git

### 1. 로컬 개발 환경 설정

#### 1.1 프로젝트 클론
```bash
# 프로젝트 클론
git clone https://github.com/changsoo-Shin/ktds-css.git
cd ktds-001

# 또는 ZIP 파일 다운로드 후 압축 해제
```

#### 1.2 가상환경 생성 및 활성화
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

#### 1.3 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

주요 패키지:
- `streamlit>=1.39.0` - 웹 애플리케이션 프레임워크
- `langchain-openai>=0.2.0` - LangChain OpenAI 통합
- `azure-ai-vision-imageanalysis>=1.0.0` - Azure Computer Vision
- `python-dotenv>=1.0.0` - 환경 변수 관리
- `requests>=2.32.0` - HTTP 요청
- `Pillow>=10.0.0` - 이미지 처리

### 2. 환경 변수 설정

#### 2.1 환경 변수 파일 생성
프로젝트 루트 디렉토리에 `.env` 파일을 생성합니다:
```bash
# Windows
copy env.sample .env

# macOS/Linux
cp env.sample .env
```

#### 2.2 환경 변수 설정
`.env` 파일을 열고 실제 값으로 수정합니다:

```env
# Azure OpenAI 설정 (필수)
AZURE_ENDPOINT=https://your-resource-name.openai.azure.com/
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_VERSION=2024-02-15-preview

# Azure Computer Vision 설정 (선택사항 - 이미지 분석용)
COMPUTER_VISION_KEY=your_computer_vision_key_here
COMPUTER_VISION_ENDPOINT=https://your-computer-vision-resource.cognitiveservices.azure.com/

# OpenWeatherMap API (선택사항 - 날씨 정보용)
WEATHER_API_KEY=your_openweathermap_api_key_here

# Azure AI Search 설정 (선택사항 - RAG 기능 고급화용)
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_KEY=your_azure_search_key_here
AZURE_SEARCH_INDEX_NAME=travel_destinations
```

**필수 API 키 발급 방법:**
1. **Azure OpenAI** (필수)
   - [Azure Portal](https://portal.azure.com)에서 Azure OpenAI 리소스 생성
   - "Keys and Endpoint"에서 키와 엔드포인트 복사
   - GPT-4 모델 배포 필요

2. **Azure Computer Vision** (선택)
   - Azure Portal에서 Computer Vision 리소스 생성
   - API 키와 엔드포인트 복사

3. **OpenWeatherMap** (선택)
   - [OpenWeatherMap](https://openweathermap.org/api)에서 무료 계정 생성
   - API 키 발급

### 3. 애플리케이션 실행
```bash
streamlit run app.py
```

브라우저가 자동으로 열리며 `http://localhost:8501`에서 앱을 확인할 수 있습니다.

### 4. Azure App Service 배포

Azure App Service에 배포하려면 [DEPLOYMENT.md](DEPLOYMENT.md) 문서를 참조하세요.

주요 배포 단계:
1. Azure App Service 리소스 생성 (Python 3.11 런타임)
2. 환경 변수를 Azure Portal에서 설정
3. GitHub Actions 또는 Azure CLI로 배포
4. `startup.sh`가 자동으로 Streamlit 서버 시작

**배포 URL**: https://travelguide01-ayg8egfwgebscmc5.koreacentral-01.azurewebsites.net

## 📁 프로젝트 구조

```
ktds-001/
├── app.py                          # 메인 Streamlit 애플리케이션
├── config.py                       # 환경 설정 및 API 키 관리
├── travel_rag.py                   # RAG 기반 여행일정 생성 시스템
├── image_analyzer.py               # Azure Computer Vision 이미지 분석
├── image_analyzer_safe.py          # 안전한 이미지 분석 (폴백 포함)
├── weather_service.py              # OpenWeatherMap 날씨 서비스
├── weather_service_mock.py         # 날씨 서비스 모의 객체 (테스트용)
├── weather_service_alternative.py  # 대체 날씨 서비스 구현
├── requirements.txt                # Python 패키지 의존성
├── env.sample                      # 환경 변수 샘플 파일
├── startup.sh                      # Azure App Service 시작 스크립트
├── README.md                       # 프로젝트 설명 (본 문서)
├── DEPLOYMENT.md                   # Azure 배포 가이드
├── .gitignore                      # Git 무시 파일 목록
└── venv/                           # Python 가상환경 (로컬 개발용)
```

### 주요 파일 설명

- **app.py**: Streamlit 기반 메인 UI 및 사용자 인터페이스
- **travel_rag.py**: LangChain과 Azure OpenAI를 활용한 RAG(Retrieval Augmented Generation) 시스템
- **image_analyzer.py / image_analyzer_safe.py**: Azure Computer Vision을 이용한 이미지 분석 및 여행지 추천
- **weather_service.py**: 실시간 날씨 정보 제공
- **config.py**: 모든 API 키와 설정을 중앙에서 관리

## 🛠️ 기술 스택

### Core Technologies
- **Frontend Framework**: Streamlit 1.39.0
  - 빠른 프로토타이핑과 배포를 위한 Python 기반 웹 프레임워크
  - 반응형 UI 컴포넌트와 실시간 상호작용

- **AI & Machine Learning**
  - **Azure OpenAI Service**: GPT-4 기반 자연어 처리
  - **LangChain**: AI 애플리케이션 개발 프레임워크
  - **Azure Computer Vision**: 이미지 분석 및 객체 인식

### Cloud Services & APIs
- **Azure App Service**: 프로덕션 호스팅
- **Azure OpenAI**: 대규모 언어 모델 (GPT-4)
- **Azure Computer Vision**: 이미지 분석 서비스
- **Azure AI Search**: (선택) 고급 RAG 기능
- **OpenWeatherMap API**: 실시간 날씨 데이터

### Development Tools
- **Python 3.11+**: 주 개발 언어
- **python-dotenv**: 환경 변수 관리
- **Git**: 버전 관리
- **GitHub**: 코드 저장소 및 협업

## 📝 사용 가이드

### 1. 맞춤 여행일정 생성

1. **기본 정보 입력** (사이드바)
   - 🏙️ 여행지: 방문하고 싶은 도시나 지역 입력 (예: 파리, 도쿄, 제주도)
   - 📅 여행 시작일: 달력에서 날짜 선택
   - 📅 여행 기간: 슬라이더로 1-14일 중 선택
   - 🎯 여행 스타일: 관광, 휴양, 문화, 맛집, 자연, 쇼핑 중 선택
   - 💰 예산: 저예산/중간/고급 중 선택

2. **일정 생성**
   - "🚀 여행일정 생성하기" 버튼 클릭
   - AI가 맞춤형 일정 생성 (약 10-30초 소요)
   - 생성된 일정 검토

3. **일정 다운로드**
   - "📄 일정 다운로드" 버튼으로 텍스트 파일 저장
   - 여행 중 오프라인으로도 확인 가능

### 2. 이미지 기반 여행지 추천

1. **이미지 업로드**
   - "📸 이미지 분석" 탭 선택
   - 여행하고 싶은 장소의 사진 업로드 (JPG, PNG, JPEG)
   - 권장 크기: 1-5MB

2. **AI 분석**
   - "🔍 이미지 분석하기" 버튼 클릭
   - Azure Computer Vision이 이미지 내용 분석
   - 장소 유형, 특징, 분위기 파악

3. **추천 확인**
   - AI가 제시하는 유사한 특색의 여행지 리스트 확인
   - 새로운 여행 아이디어 발굴

### 3. AI 여행 상담

1. **채팅 시작**
   - "💬 AI 상담" 탭 선택
   - 환영 메시지 확인

2. **질문하기**
   - 채팅창에 여행 관련 질문 입력
   - 예시:
     - "제주도 3박 4일 여행 추천해줘"
     - "파리에서 꼭 가봐야 할 박물관은?"
     - "일본 여행 시 주의사항 알려줘"

3. **대화 지속**
   - 이전 대화 내용을 기억하는 컨텍스트 유지
   - 추가 질문으로 더 자세한 정보 얻기

### 4. 날씨 확인

- 여행일정 생성 탭에서 "날씨 확인" 버튼 클릭
- 현재 날씨 정보와 여행 준비 조언 확인

## ⚠️ 주의사항 및 제약사항

### 필수 요구사항
- ✅ Azure OpenAI API 키 필수 (필수 기능 동작을 위함)
- ✅ 안정적인 인터넷 연결 필요
- ✅ 최신 웹 브라우저 권장 (Chrome, Edge, Firefox, Safari)

### 선택적 요구사항
- Azure Computer Vision 키 없이는 이미지 분석 기능 미사용
- OpenWeatherMap 키 없이는 날씨 기능 미사용

### 사용 제한
- Azure OpenAI API 사용량에 따른 비용 발생
- 일부 Azure 서비스는 지역별 가용성 제한
- 이미지 파일 크기 제한 (10MB 이하 권장)

### 데이터 보안
- 사용자 입력 데이터는 세션 종료 시 삭제
- API 키는 서버 환경 변수로 안전하게 관리
- 업로드된 이미지는 분석 후 저장되지 않음

## 🐛 문제 해결 (Troubleshooting)

### 앱이 실행되지 않는 경우
```bash
# Python 버전 확인 (3.11 이상 필요)
python --version

# 가상환경 활성화 여부 확인
which python  # macOS/Linux
where python  # Windows

# 패키지 재설치
pip install --upgrade -r requirements.txt
```

### API 오류 발생 시
1. `.env` 파일의 API 키가 올바른지 확인
2. Azure Portal에서 해당 서비스가 활성화되어 있는지 확인
3. API 키의 권한 및 사용량 제한 확인

### 이미지 분석 오류
- 이미지 파일 형식 확인 (JPG, PNG만 지원)
- 파일 크기 확인 (10MB 이하 권장)
- Computer Vision API 키 설정 확인

### 날씨 정보 표시 안 됨
- OpenWeatherMap API 키 확인
- 도시 이름을 영어로 입력 시도
- Mock 서비스로 자동 폴백 (개발용)

### 성능 이슈
- 브라우저 캐시 삭제
- 다른 Streamlit 세션 종료
- 서버 재시작: `Ctrl+C` 후 다시 실행

## 🚀 향후 개선사항

### 1. 📊 스마트 예산 관리 시스템
항공권, 숙박, 식사, 관광 등 여행 비용을 세부적으로 계산하고 관리하는 기능을 추가합니다. 실시간 항공권 가격(Skyscanner API), 숙박 정보(Booking.com API), 환율 정보를 통합하여 사용자가 예산 내에서 최적의 여행 계획을 수립할 수 있도록 지원합니다.

### 2. 🗺️ 지도 기반 시각화 및 경로 최적화
Google Maps 또는 Kakao Map API를 통합하여 추천된 여행지를 지도에 표시하고, 이동 경로를 시각화합니다. 여러 장소를 방문할 때 최적의 동선을 자동으로 계산하여 시간과 교통비를 절약할 수 있도록 합니다.

### 3. 📱 모바일 반응형 디자인 및 PWA
모바일 기기에서도 최적화된 사용자 경험을 제공하기 위해 반응형 디자인을 구현하고, PWA(Progressive Web App) 기능을 추가합니다. 오프라인에서도 저장된 여행 일정을 확인하고, 앱처럼 설치하여 사용할 수 있습니다.

### 4. 🤖 개인화 AI 추천 시스템
사용자의 여행 기록, 선호도, 평가를 학습하여 점점 더 정확한 맞춤형 추천을 제공합니다. Azure AI Search를 활용한 벡터 검색 기반 고급 RAG를 구현하여 실제 여행자 리뷰와 최신 여행 트렌드를 반영한 일정을 생성합니다.

### 5. 🌐 다국어 지원 및 글로벌 확장
영어, 일본어, 중국어 등 다양한 언어를 지원하여 글로벌 사용자에게 서비스를 제공합니다. 각 국가의 문화와 특성을 고려한 현지화된 여행 정보와 추천을 제공하여 해외 여행객도 쉽게 이용할 수 있도록 합니다.

## 📊 현재 개발 상태

### 완료된 기능 ✅
- **여행일정 생성**: Azure OpenAI + LangChain 기반 맞춤형 일정 생성
- **이미지 분석**: Azure Computer Vision을 활용한 여행지 추천
- **AI 채팅 상담**: GPT-4 기반 실시간 여행 상담
- **날씨 정보**: OpenWeatherMap API 통합
- **Azure 배포**: App Service를 통한 프로덕션 환경 구축

### 진행 중 🔄
- **고급 RAG 기능**: Azure AI Search 통합 작업 중
- **UI/UX 개선**: 사용자 피드백 반영 중
- **성능 최적화**: 응답 속도 개선 작업

### 계획 중 📝
- **모바일 반응형**: 모바일 기기 최적화
- **다국어 지원**: 영어, 일본어, 중국어 지원
- **예산 계산기**: 세부 여행 비용 분석 기능
- **지도 통합**: 여행지 위치 시각화

## 🔗 참고 자료

### 공식 문서
- [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/) - Azure OpenAI API 문서
- [LangChain Documentation](https://python.langchain.com/) - LangChain 프레임워크 가이드
- [Streamlit Documentation](https://docs.streamlit.io/) - Streamlit 웹 프레임워크
- [Azure Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/) - Computer Vision API
- [OpenWeatherMap API](https://openweathermap.org/api) - 날씨 데이터 API

### 배포 및 설정
- [배포 가이드](DEPLOYMENT.md) - Azure App Service 배포 상세 가이드
- [환경 변수 샘플](env.sample) - 설정 파일 예시

## 💬 문의 및 지원

### 문제 발생 시
문제가 발생하거나 질문이 있으신가요?

1. **문서 확인**: 먼저 [배포 가이드](DEPLOYMENT.md)와 [문제 해결](#-문제-해결-troubleshooting) 섹션을 확인해주세요
2. **이슈 등록**: [GitHub Issues](https://github.com/changsoo-Shin/ktds-css/issues)에 문제를 상세히 보고해주세요
3. **피드백**: 개선 아이디어나 제안사항도 환영합니다

### 도움이 되는 정보
이슈를 등록할 때 다음 정보를 포함하면 더 빠른 해결이 가능합니다:
- 운영체제 및 Python 버전
- 오류 메시지 전체 내용
- 재현 가능한 단계
- 스크린샷 (UI 관련 문제인 경우)

---

**Made with ❤️ using Azure AI Services**

*이 프로젝트는 KTDS MS AI 개발 과정의 일환으로 개발되었습니다.*
