import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("DEEPSEEK_API_KEY")
base_url=os.getenv("DEEPSEEK_BASE_URL")
model=os.getenv("MODEL_NAME")

headers={
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
}

payload={
    "model":model,
    "temperature":0.7,
    "messages":[
        {"role":"system","content":"你是简短回答助手"},
        {"role":"user","content":"简单介绍一下你是什么AI Agent"}
    ]
}

resp=requests.post(f"{base_url}/chat/completions",headers=headers,json=payload)
print("状态码：",resp.status_code)
print("返回原始文本：",resp.text)
result=resp.json()
answer=result["choices"][0]["message"]["content"]
print("LLM返回结果",answer)
