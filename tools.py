from langchain_core.tools import tool

@tool
def read_file(path: str) -> str:
    """Read file contents"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

@tool
def write_file(path: str, content: str) -> str:
    """Write content to file"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"Successfully wrote to {path}"

@tool
def run_code(code: str) -> str:
    """Execute Python code"""
    import subprocess, sys, tempfile, os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tf:
        tf.write(code)
        temp_path = tf.name
    try:
        result = subprocess.run([sys.executable, temp_path], capture_output=True, text=True, timeout=15)
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    finally:
        os.remove(temp_path)