"""
Cuneiform 프롬프트 생성기 (Generator)
- 역할: AST를 Claude API용 자연어 프롬프트로 변환
"""

class PromptGenerator:
    def __init__(self, ast):
        self.ast = ast
    
    def generate(self):
        """AST를 AI 프롬프트로 변환"""
        prompts = []
        
        for task in self.ast:
            prompt = self._generate_task_prompt(task)
            prompts.append(prompt)
        
        return "\n\n".join(prompts)
    
    def _generate_task_prompt(self, task):
        """개별 작업을 프롬프트로 변환"""
        lines = []
        
        lines.append(f"Task: {task.name}")
        
        if task.purpose:
            lines.append(f"Purpose: {task.purpose}")
        
        if task.output:
            lines.append(f"\nPlease generate the output as specified: {task.output}")
        
        return "\n".join(lines)


# 테스트
if __name__ == "__main__":
    from lexer import Lexer
    from parser import Parser
    
    code = '''
작업: 인사말
설명: 첫 번째 테스트
출력: "안녕하세요"
'''
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    generator = PromptGenerator(ast)
    prompt = generator.generate()
    
    print("생성된 프롬프트:")
    print("=" * 60)
    print(prompt)
