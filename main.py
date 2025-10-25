"""
Cuneiform 메인 실행 파일
- 역할: .cf 파일을 읽어서 전체 파이프라인 실행
"""

import sys
from src.lexer import Lexer
from src.parser import Parser
from src.generator import PromptGenerator
from src.executor import AIExecutor


def run_cuneiform(filepath):
    """Cuneiform 파일 실행"""
    
    print(f"🔧 Cuneiform 파일 실행: {filepath}")
    print("=" * 60)
    
    # 1. 파일 읽기
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {filepath}")
        return
    
    print("\n📄 소스 코드:")
    print(source_code)
    print("=" * 60)
    
    # 2. 렉싱
    print("\n🔤 Step 1: 토큰화 중...")
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print(f"✅ {len(tokens)}개 토큰 생성")
    
    # 3. 파싱
    print("\n🌳 Step 2: AST 생성 중...")
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"✅ {len(ast)}개 작업 파싱 완료")
    
    # 4. 프롬프트 생성
    print("\n💬 Step 3: AI 프롬프트 생성 중...")
    generator = PromptGenerator(ast)
    prompt = generator.generate()
    print("생성된 프롬프트:")
    print("-" * 60)
    print(prompt)
    print("-" * 60)
    
    # 5. AI 실행
    print("\n🤖 Step 4: Claude에게 전송 중...")
    executor = AIExecutor()
    result = executor.execute(prompt)
    
    print("\n✅ Step 5: 결과")
    print("=" * 60)
    print(result)
    print("=" * 60)
    
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python main.py <파일경로>")
        print("예: python main.py examples/hello.cf_kr")
    else:
        filepath = sys.argv[1]
        run_cuneiform(filepath)
