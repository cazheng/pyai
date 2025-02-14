import requests

url = "https://api.siliconflow.cn/v1/images/generations"

payload = {
    "model": "deepseek-ai/Janus-Pro-7B",
    "prompt": "beautiful girl with Bikini, poster",
    "seed": 4999999999
}
headers = {
    # With my token
    #"Authorization": "Bearer sk-nfddkgvcxubmntusvbqsosujlzcnjkcjmphzgfctpgkeymnq",
    # With fwj token
    "Authorization": "Bearer sk-xafmegjniqzbzgtttfgqbhqksqhiekweylozorjyknfznqiu",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

if response.status_code == 200:
    # 解析JSON数据
    data = response.json()
    image_url = data["images"][0]["url"]  # 假设JSON中包含图像的URL

    # 下载图像
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open("image.png", "wb") as file:
            file.write(image_response.content)
        print("图像已下载为 image.png")
    else:
        print(f"图像下载失败，状态码：{image_response.status_code}")
else:
    print(f"API调用失败，状态码：{response.status_code}")
    
print(response.text)