import requests

url = "http://127.0.0.1:5000/api/jobs/recommended"
payload = {
    "skills": ["python", "flask", "sql"],
    "experience": 2,
    "career_goal": "Backend Developer"
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)

try:
    print("Output (JSON):", response.json())
except Exception:
    print("Output (Raw):", response.text)
