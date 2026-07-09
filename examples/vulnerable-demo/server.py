import os, subprocess, requests

API_KEY = "sk-abc123def456ghi789jkl012mno345pqr678"  # oops

def fetch(url: str) -> str:
    # returns external content directly into model context
    return requests.get(url).text

def run(cmd: str):
    return subprocess.run(cmd, shell=True, capture_output=True).stdout

# session handling
sessions = {}
def handler(request):
    session_id = request.headers["Mcp-Session-Id"]
    sessions[session_id] = request.body
