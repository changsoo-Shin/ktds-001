import requests
import json
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from config import Config

class WeatherServiceAlternative:
    def __init__(self):
        # WeatherAPI.com 무료 API 키 (더 안정적)
        self.api_key = "your_weatherapi_key"  # WeatherAPI.com에서 발급
        self.base_url = "http://api.weatherapi.com/v1"
    
    def get_current_weather(self, city: str) -> Dict[str, Any]:
        """현재 날씨 정보 조회 - WeatherAPI 사용"""
        try:
            url = f"{self.base_url}/current.json"
            params = {
                "key": self.api_key,
                "q": city,
                "lang": "ko"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temperature": data["current"]["temp_c"],
                "feels_like": data["current"]["feelslike_c"],
                "humidity": data["current"]["humidity"],
                "description": data["current"]["condition"]["text"],
                "icon": data["current"]["condition"]["icon"],
                "wind_speed": data["current"]["wind_kph"],
                "visibility": data["current"]["vis_km"]
            }
            
        except Exception as e:
            return {"error": f"날씨 정보를 가져올 수 없습니다: {str(e)}"}

    def get_weather_advice(self, weather_data: Dict[str, Any]) -> str:
        """날씨에 따른 여행 조언 생성"""
        if "error" in weather_data:
            return "날씨 정보를 확인할 수 없어 여행 조언을 제공할 수 없습니다."
        
        temp = weather_data.get("temperature", 0)
        description = weather_data.get("description", "")
        humidity = weather_data.get("humidity", 0)
        wind_speed = weather_data.get("wind_speed", 0)
        
        advice = []
        
        # 온도 기반 조언
        if temp < 0:
            advice.append("❄️ 매우 추운 날씨입니다. 따뜻한 옷을 준비하세요.")
        elif temp < 10:
            advice.append("🧥 쌀쌀한 날씨입니다. 겉옷을 챙기세요.")
        elif temp < 25:
            advice.append("🌤️ 쾌적한 날씨입니다. 야외 활동에 좋습니다.")
        elif temp < 35:
            advice.append("☀️ 더운 날씨입니다. 자외선 차단제와 충분한 수분을 준비하세요.")
        else:
            advice.append("🔥 매우 더운 날씨입니다. 실내 활동을 권장합니다.")
        
        # 날씨 설명 기반 조언
        if "비" in description or "rain" in description.lower():
            advice.append("☔ 비가 올 예정입니다. 우산을 준비하세요.")
        elif "눈" in description or "snow" in description.lower():
            advice.append("❄️ 눈이 올 예정입니다. 미끄러운 길에 주의하세요.")
        elif "구름" in description or "cloud" in description.lower():
            advice.append("☁️ 흐린 날씨입니다. 사진 촬영 시 조명을 고려하세요.")
        
        # 습도 기반 조언
        if humidity > 80:
            advice.append("💧 습도가 높습니다. 통풍이 잘 되는 옷을 입으세요.")
        
        # 바람 기반 조언
        if wind_speed > 10:
            advice.append("💨 바람이 강합니다. 모자나 스카프를 고정하세요.")
        
        return "\n".join(advice) if advice else "일반적인 여행 준비를 하시면 됩니다."

