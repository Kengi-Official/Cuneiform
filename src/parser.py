"""
Cuneiform 파서 (Parser)
- 역할: 토큰 리스트를 AST(추상 구문 트리)로 변환
"""

class ASTNode:
    """AST 노드 베이스 클래스"""
    pass


class TaskNode(ASTNode):
    def __init__(self, name, purpose=None, inputs=None, process=None, output=None):
        self.name = name
        self.purpose = purpose
        self.inputs = inputs or []
        self.process = process or []
        self.output = output
    
    def __repr__(self):
        return f"TaskNode(name={self.name!r}, purpose={self.purpose!r}, output={self.output!r})"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
    
    def current_token(self):
        """현재 토큰 반환"""
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None
    
    def advance(self):
        """다음 토큰으로 이동"""
        self.current += 1
    
    def expect(self, token_type):
        """특정 타입의 토큰을 기대하고 확인"""
        token = self.current_token()
        if token and token.type == token_type:
            self.advance()
            return token
        raise SyntaxError(f"Expected {token_type}, got {token.type if token else 'EOF'}")
    
    def skip_newlines(self):
        """줄바꿈 건너뛰기"""
        while self.current_token() and self.current_token().type == 'NEWLINE':
            self.advance()
    
    def parse_task(self):
        """작업 블록 파싱"""
        self.skip_newlines()
        
        # '작업:' 확인
        self.expect('TASK')
        self.expect('COLON')
        
        name_token = self.expect('IDENTIFIER')
        name = name_token.value
        
        self.skip_newlines()
        
        # 선택적 필드들
        purpose = None
        inputs = []
        process = []
        output = None
        
        while self.current_token() and self.current_token().type != 'EOF':
            token = self.current_token()
            
            if token.type == 'PURPOSE':
                self.advance()
                self.expect('COLON')
                purpose_token = self.current_token()
                if purpose_token:
                    purpose = purpose_token.value
                    self.advance()
                self.skip_newlines()
            
            elif token.type == 'OUTPUT':
                self.advance()
                self.expect('COLON')
                output_token = self.current_token()
                if output_token:
                    output = output_token.value
                    self.advance()
                self.skip_newlines()
                break  # 출력이 마지막
            
            else:
                self.advance()
        
        return TaskNode(name, purpose, inputs, process, output)
    
    def parse(self):
        """전체 프로그램 파싱"""
        tasks = []
        
        while self.current_token() and self.current_token().type != 'EOF':
            task = self.parse_task()
            tasks.append(task)
        
        return tasks


# 테스트
if __name__ == "__main__":
    from lexer import Lexer
    
    code = '''
작업: 인사말
설명: 첫 번째 테스트
출력: "안녕하세요"
'''
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    
    for task in ast:
        print(task)
