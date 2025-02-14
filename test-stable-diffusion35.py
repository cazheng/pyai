import requests

url = "https://api.siliconflow.cn/v1/images/generations"

payload = {
    "batch_size": 1,
    "guidance_scale": 10,
    "image_size": "768x512",
    "model": "stabilityai/stable-diffusion-3-5-large",
    "num_inference_steps": 3,
    "prompt": "芯潮流(珠海)科技有限公司, 中国新年, poster",
    "seed": 4999999999
}
headers = {
    "Authorization": "Bearer sk-nfddkgvcxubmntusvbqsosujlzcnjkcjmphzgfctpgkeymnq",
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
        with open("image2.png", "wb") as file:
            file.write(image_response.content)
        print("图像已下载为 image2.png")
    else:
        print(f"图像下载失败，状态码：{image_response.status_code}")
else:
    print(f"API调用失败，状态码：{response.status_code}")
    
print(response.text)