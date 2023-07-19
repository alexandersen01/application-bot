import tiktoken

def tokens_in_words(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

with open('application_paretoH23.txt', 'r') as f:
    example = f.read()

print(tokens_in_words(example, 'p50k_base'))
