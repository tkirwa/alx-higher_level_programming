#!/usr/bin/env python3
import os

filename = os.environ.get('PYFILE')
if not filename:
    print("Error: PYFILE environment variable not set")
    exit(1)

if not filename.endswith('.py'):
    print("Error: PYFILE must end with '.py'")
    exit(1)

output_filename = filename[:-3] + 'pyc'
print(f"Compiling {filename}...")
with open(filename, 'rb') as source_file:
    with open(output_filename, 'wb') as bytecode_file:
        code = compile(source_file.read(), filename, 'exec')
        bytecode_file.write(code)

print(f"Bytecode saved as {output_filename}")
