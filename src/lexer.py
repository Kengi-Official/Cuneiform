"""
Cuneiform 렉서 (Lexer)
- 역할: Cuneiform 코드를 토큰으로 분해
"""

class Token:
    def __init__(self, type, value, line=1, column=1):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, {self.line}:{self.column})"


class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.source[0] if source_code else None
        
        # 한국어 키워드
        self.keywords_kr = {
            '작업': 'TASK',
            '설명': 'PURPOSE',
            '입력': 'INPUT',
            '처리': 'PROCESS',
            '출력': 'OUTPUT',
            '만약': 'IF',
            '아니면': 'ELSE',
            '반복': 'REPEAT',
        }
    
    def advance(self):
        """다음 문자로 이동"""
        self.position += 1
        self.column += 1
        
        if self.position < len(self.source):
            self.current_char = self.source[self.position]
            
            if self.current_char == '\n':
                self.line += 1
                self.column = 1
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        """공백 건너뛰기"""
        while self.current_char and self.current_char in ' \t':
            self.advance()
    
    def skip_comment(self):
        """주석 건너뛰기"""
        if self.current_char == '#':
            while self.current_char and self.current_char != '\n':
                self.advance()
    
    def read_string(self):
        """문자열 읽기"""
        value = ''
        self.advance()  # 여는 따옴표 건너뛰기
        
        while self.current_char and self.current_char != '"':
            value += self.current_char
            self.advance()
        
        self.advance()  # 닫는 따옴표 건너뛰기
        return value
    
    def read_identifier(self):
        """식별자 또는 키워드 읽기"""
        value = ''
        
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            value += self.current_char
            self.advance()
        
        return value
    
    def tokenize(self):
        """소스 코드를 토큰 리스트로 변환"""
        tokens = []
        
        while self.current_char:
            # 공백 및 주석 건너뛰기
            if self.current_char in ' \t':
                self.skip_whitespace()
                continue
            
            if self.current_char == '#':
                self.skip_comment()
                continue
            
            # 줄바꿈
            if self.current_char == '\n':
                tokens.append(Token('NEWLINE', '\\n', self.line, self.column))
                self.advance()
                continue
            
            # 콜론
            if self.current_char == ':':
                tokens.append(Token('COLON', ':', self.line, self.column))
                self.advance()
                continue
            
            # 문자열
            if self.current_char == '"':
                string_value = self.read_string()
                tokens.append(Token('STRING', string_value, self.line, self.column))
                continue
            
            # 식별자 또는 키워드
            if self.current_char.isalnum() or ord(self.current_char) > 127:  # 한글 포함
                identifier = self.read_identifier()
                
                # 키워드 확인
                token_type = self.keywords_kr.get(identifier, 'IDENTIFIER')
                tokens.append(Token(token_type, identifier, self.line, self.column))
                continue
            
            # 알 수 없는 문자
            self.advance()
        
        tokens.append(Token('EOF', None, self.line, self.column))
        return tokens


# 테스트
if __name__ == "__main__":
    code = '''
작업: 인사말
설명: 첫 번째 테스트
출력: "안녕하세요"
'''
    
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    for token in tokens:
        print(token)
