import tokenize
import io

def translate_code(code):
    token_map = {
        'int': 'INT',
        'float': 'FLOAT',
        'bool': 'BOOL',
        'str': 'STR',
        'print': 'show',
        'input': 'get',
        'if': 'if',
        'else': 'else',
        'type': 'category'
    }
    result = []
    tokens = tokenize.generate_tokens(io.StringIO(code).readline)
    for toknum, tokval, _, _, _ in tokens:
        tokval = token_map.get(tokval, tokval)
        result.append((toknum, tokval))
    return tokenize.untokenize(result)

def add_semicolons(code):
    lines = code.split('\n')
    new_lines = []
    for line in lines:
        stripped_line = line.strip()
        if (stripped_line.startswith('show(') or
            stripped_line.startswith('get(') or
            stripped_line.startswith('category') or
            stripped_line.startswith('ELSE')) and not stripped_line.endswith(';'):
            line += ';'
        new_lines.append(line)
    return '\n'.join(new_lines)

def execute_sora_code(code):
    translated_code = translate_code(code)
    translated_code_with_semicolons = add_semicolons(translated_code)
    #translated_code_with_semicolons = translated_code_with_semicolons.replace('if', 'if').replace('else:', 'ELSE;')
    exec(
        "INT = int\nFLOAT = float\nBOOL = bool\nSTR = str\ndef get(): return input()\ndef show(value):\n    if isinstance(value, (int, float)):\n        print(str(value))\n    elif isinstance(value, str) and value.lower() == 'category':\n        print('The type is:')\n        print(type(x))\n    else:\n        print(value)\ndef category(x) : return str(type(x))\n" +
        translated_code_with_semicolons
    )

if __name__ == "__main__":
    x = input("Enter the file name to run the sora code with extension .sora eg: example.sora\n")
    with open(x, 'r') as file:
        sora_code = file.read()
    execute_sora_code(sora_code)
