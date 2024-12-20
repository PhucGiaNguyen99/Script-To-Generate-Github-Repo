import requests

session = requests.Session()
session.auth = ("YOUR_GITHUB_USERNAME", "YOUR_GITHUB_TOKEN")
payload = {"name": "test-requests", "description": "Created with the requests library"}
api_url = "https://api.github.com/user/repos"
response_1 = session.post(api_url, json=payload)
if response_1:
    data = {
        "message": "Add README via API",
        # The 'content' needs to be a base64 encoded string
        # Python's standard library can help with that
        # You can uncover the secret of this garbled string
        # by uploading it to GitHub with this script :)
        "content": "UmVxdWVzdHMgaXMgYXdlc29tZSE=",
    }
    repo_url = response_1.json()["url"]
    readme_url = f"{repo_url}/contents/README.md"
    response_2 = session.put(readme_url, json=data)
else:
    print(response_1.status_code, response_1.json())

html_url = response_2.json()["content"]["html_url"]
print(f"See your repo live at: {html_url}")
session.close()
