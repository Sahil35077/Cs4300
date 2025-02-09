import subprocess

def test_hello_world():
    result = subprocess.run(["python3", "task1.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, World!"