class LexicalAnalyzer:
    # ? constructor (like `public LexicalAnalyzer(String input_file, String output_file)` in java )
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.tokens = []
    
    def read_file(self,r_file):
        with open(r_file, 'r') as file:
            return file.read()

    def analyze(self, text):
        i = 0
        while i < len(text):
            char = text[i]

            if char in ['>', '<', '=']:  
                token = char
                next_char = text[i+1] if i+1 < len(text) else ''
                
                if next_char == '=':
                    token += '='
                    i += 2
                else:
                    i += 1
                
                self.tokens.append(('cs', token))
            elif char.isspace():  
                i += 1
            else:
                raise ValueError(f"Unrecognized character: {char}")
            
    def make_tokens_file(self):
        with open(self.output_file, 'w') as file:
            for token in self.tokens:
                file.write(f"{token}\n")

    def run(self):
        try:
            text = self.read_file(self.input_file)
            self.analyze(text)
            self.make_tokens_file()
            print("Tokens file:")
            print(self.read_file(self.output_file))
        except Exception as e:
            print(f"Error: {e}")





analyzer = LexicalAnalyzer("test.txt", "token.txt")
analyzer.run()
