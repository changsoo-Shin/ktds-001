import random
from typing import Dict, Any
from datetime import datetime

class MockWeatherService:
    """API 문제 시 사용할 모의 날씨 서비스"""
    
    def __init__(self):
        self.mock_data = {
            "Seoul": {
                "temperature": random.randint(5, 25),
                "description": "맑음",
                "humidity": random.randint(40, 80),
                "wind_speed": random.randint(2, 15)
            },
            "Tokyo": {
                "temperature": random.randint(8, 28),
                "description": "구름 조금",
                "humidity": random.randint(45, 85),
                "wind_speed": random.randint(1, 12)
            },
            "Paris": {
                "temperature": random.randint(3, 20),
                "description": "흐림",
                "humidity": random.randint(50, 90),
                "wind_speed": random.randint(3, 18)
            }
        }
    
    def get_current_weather(self, city: str) -> Dict[str, Any]:
        """모의 날씨 데이터 반환"""
        try:
            # 입력된 도시에 해당하는 데이터가 있으면 사용, 없으면 기본값
            if city in self.mock_data:
                data = self.mock_data[city]
            else:
                # 랜덤 데이터 생성
                data = {
                    "temperature": random.randint(0, 30),
                    "description": random.choice(["맑음", "구름 조금", "흐림", "비", "눈"]),
                    "humidity": random.randint(30, 90),
                    "wind_speed": random.randint(1, 20)
                }
            
            return {
                "city": city,
                "country": "KR" if city in ["Seoul", "서울"] else "Unknown",
                "temperature": data["temperature"],
                "feels_like": data["temperature"] + random.randint(-2, 2),
                "humidity": data["humidity"],
                "description": data["description"],
                "icon": "01d",  # 기본 아이콘
                "wind_speed": data["wind_speed"],
                "visibility": random.randint(5, 15)
            }
            
        except Exception as e:
            return {"error": f"모의 날씨 정보 생성 중 오류: {str(e)}"}
    
    def get_weather_advice(self, weather_data: Dict[str, Any]) -> str:
        """날씨에 따른 여행 조언 생성"""
        if "error" in weather_data:
            return "날씨 정보를 확인할 수 없어 여행 조언을 제공할 수 없습니다."
        
        temp = weather_data.get("temperature", 0)
        description = weather_data.get("description", "")
        
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
        if "비" in description:
            advice.append("☔ 비가 올 예정입니다. 우산을 준비하세요.")
        elif "눈" in description:
            advice.append("❄️ 눈이 올 예정입니다. 미끄러운 길에 주의하세요.")
        elif "구름" in description or "흐림" in description:
            advice.append("☁️ 흐린 날씨입니다. 사진 촬영 시 조명을 고려하세요.")
        
        return "\n".join(advice) if advice else "일반적인 여행 준비를 하시면 됩니다."

