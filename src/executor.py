"""
Cuneiform AI 실행기 (Executor)
- 역할: 생성된 프롬프트를 Claude API에 전송하고 결과 반환
"""

import anthropic
import os
from dotenv import load_dotenv


class AIExecutor:
    def __init__(self, api_key=None):
        load_dotenv()
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def execute(self, prompt, max_tokens=500):
        """프롬프트를 AI에 전송하고 결과 반환"""
        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=max_tokens,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            result = message.content[0].text
            return result
            
        except Exception as e:
            return f"오류 발생: {e}"
