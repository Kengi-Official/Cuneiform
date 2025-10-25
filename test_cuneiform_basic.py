import anthropic
import os
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()

# Cuneiform 한국어 버전 간단한 예제
cuneiform_code = '''
작업: 인사말_테스트
설명: 첫 번째 Cuneiform 테스트
출력: "안녕하세요, Cuneiform입니다!"
'''

print("=" * 60)
print("🔧 Step 1: Cuneiform 코드 확인")
print("=" * 60)
print(cuneiform_code)
print("=" * 60)

# 실제로는 렉서/파서를 거쳐야 하지만, 지금은 직접 프롬프트 생성
prompt = f'''
다음은 Cuneiform이라는 자연어 기반 프로그래밍 언어 코드입니다:

{cuneiform_code}

이 코드를 실행하면 어떤 결과가 나와야 할까요?
출력 부분의 내용을 그대로 반환해주세요.
'''

print("\n🤖 Step 2: Claude에게 프롬프트 전송 중...")
print("=" * 60)

# API 키 확인
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ 오류: API 키가 설정되지 않았습니다!")
    print("   .env 파일을 확인하고 ANTHROPIC_API_KEY를 설정하세요.")
    input("\nEnter 키를 눌러 종료...")
    exit(1)

# Claude API 호출
client = anthropic.Anthropic(api_key=api_key)

try:
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = message.content[0].text

    print("\n✅ Step 3: Claude 응답")
    print("=" * 60)
    print(result)
    print("=" * 60)

    print(f"\n💰 사용 토큰: {message.usage.input_tokens} 입력 + {message.usage.output_tokens} 출력")
    print(f"💵 예상 비용: ~${(message.usage.input_tokens * 0.003 + message.usage.output_tokens * 0.015) / 1000:.4f}")

    print("\n🎉 테스트 성공!")
    print("\n다음 단계: 렉서, 파서, 프롬프트 생성기 개발")

except Exception as e:
    print(f"\n❌ 오류 발생: {e}")
    print("\nAPI 키를 확인하세요:")
    print("1. console.anthropic.com에서 키가 활성화되어 있는지")
    print("2. .env 파일에 정확히 복사했는지")
    print("3. 결제 정보가 등록되어 있는지 (초기 크레딧으로 가능)")

input("\nEnter 키를 눌러 종료...")
