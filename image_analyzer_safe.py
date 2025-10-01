import os
from typing import Dict, Any, List
from PIL import Image
import streamlit as st
from config import Config

class SafeImageAnalyzer:
    def __init__(self):
        # Computer Vision API가 없으면 기본 기능만 제공
        self.has_vision_api = bool(Config.COMPUTER_VISION_KEY and Config.COMPUTER_VISION_ENDPOINT)
        
        if self.has_vision_api:
            try:
                from azure.core.credentials import AzureKeyCredential
                from azure.ai.vision.imageanalysis import ImageAnalysisClient
                from azure.ai.vision.imageanalysis.models import VisualFeatures
                
                self.credential = AzureKeyCredential(Config.COMPUTER_VISION_KEY)
                self.client = ImageAnalysisClient(
                    endpoint=Config.COMPUTER_VISION_ENDPOINT, 
                    credential=self.credential
                )
                self.VisualFeatures = VisualFeatures
            except ImportError:
                self.has_vision_api = False
    
    def analyze_travel_image(self, image_data: bytes) -> Dict[str, Any]:
        """여행 관련 이미지 분석 - 안전한 방식"""
        if not self.has_vision_api:
            return {
                "caption": "이미지 분석 기능을 사용하려면 Azure Computer Vision API 키가 필요합니다.",
                "confidence": 0.0,
                "tags": [],
                "objects": [],
                "note": "Computer Vision API가 설정되지 않았습니다."
            }
        
        try:
            # 단계별로 Visual Features 테스트
            analysis = {
                "caption": "이미지를 분석할 수 없습니다.",
                "confidence": 0.0,
                "tags": [],
                "objects": []
            }
            
            # 1. 캡션과 태그만 먼저 시도
            try:
                result = self.client.analyze(
                    image_data=image_data,
                    visual_features=[
                        self.VisualFeatures.CAPTION,
                        self.VisualFeatures.TAGS
                    ],
                    model_version="latest"
                )
                
                # 캡션 정보
                if result.caption:
                    analysis["caption"] = result.caption.text
                    analysis["confidence"] = result.caption.confidence
                
                # 태그 정보
                if result.tags:
                    analysis["tags"] = [
                        {
                            "name": tag.name,
                            "confidence": tag.confidence
                        }
                        for tag in result.tags.list
                    ]
                    
            except Exception as e:
                st.warning(f"캡션/태그 분석 중 오류: {str(e)}")
            
            # 2. 객체 분석 시도 (별도로)
            try:
                result_objects = self.client.analyze(
                    image_data=image_data,
                    visual_features=[
                        self.VisualFeatures.OBJECTS
                    ],
                    model_version="latest"
                )
                
                # 객체 정보
                if result_objects.objects:
                    analysis["objects"] = [
                        {
                            "name": obj.tags[0].name if obj.tags else "unknown",
                            "confidence": obj.tags[0].confidence if obj.tags else 0.0,
                            "bounding_box": obj.bounding_box
                        }
                        for obj in result_objects.objects.list
                    ]
                    
            except Exception as e:
                st.warning(f"객체 분석 중 오류: {str(e)}")
            
            return analysis
            
        except Exception as e:
            return {"error": f"이미지 분석 중 오류가 발생했습니다: {str(e)}"}
    
    def suggest_destinations_from_image(self, analysis: Dict[str, Any]) -> List[str]:
        """이미지 분석 결과를 바탕으로 여행지 추천"""
        suggestions = []
        
        # 태그 기반 추천
        travel_tags = ["building", "architecture", "nature", "mountain", "beach", "city", "temple", "castle", "park", "water", "sky", "landscape"]
        for tag in analysis.get("tags", []):
            if tag["name"].lower() in travel_tags and tag["confidence"] > 0.6:
                suggestions.append(f"{tag['name']}이 있는 여행지")
        
        # 객체 기반 추천
        travel_objects = ["car", "bus", "train", "airplane", "boat", "bicycle", "building", "person", "tree"]
        for obj in analysis.get("objects", []):
            if obj["name"].lower() in travel_objects and obj["confidence"] > 0.6:
                suggestions.append(f"{obj['name']}을 볼 수 있는 여행지")
        
        # 캡션 기반 추천
        caption = analysis.get("caption", "").lower()
        if any(word in caption for word in ["mountain", "산"]):
            suggestions.append("산이 있는 여행지")
        elif any(word in caption for word in ["beach", "sea", "ocean", "바다"]):
            suggestions.append("바다가 있는 여행지")
        elif any(word in caption for word in ["city", "building", "도시", "건물"]):
            suggestions.append("도시 여행지")
        elif any(word in caption for word in ["nature", "forest", "자연", "숲"]):
            suggestions.append("자연이 아름다운 여행지")
        
        return list(set(suggestions))  # 중복 제거
    
    def create_annotated_image(self, image_data: bytes, analysis: Dict[str, Any]) -> Image.Image:
        """분석 결과가 표시된 이미지 생성"""
        try:
            import io
            image = Image.open(io.BytesIO(image_data))
            return image
        except Exception as e:
            st.error(f"이미지 처리 중 오류: {str(e)}")
            return None

