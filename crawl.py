import os
import requests
from bs4 import BeautifulSoup


def crawl(url):
    headers = {
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Referer': url,
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    }


    response = requests.get(url=url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有图片标签
    img_tags = soup.find_all('img')

    # 创建一个文件夹用于存储下载的图片
    if not os.path.exists('images'):
        os.makedirs('images')

    # 下载并保存每张图片
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        #print(img_url)

        if not img_url.startswith('https://haowallpaper.com'):
            continue  # 跳过不以 https 开头的链接

        # 完整的图片URL
        if img_url.startswith('http'):
            full_url = img_url
        else:
            full_url = url + img_url

        # 获取图片名称
        img_name = os.path.basename(full_url)

        # 下载图片并保存到文件夹
        img_response = requests.get(full_url)
        img_response.raise_for_status()

        img_path = os.path.join('images', img_name)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)
        print(f"Downloaded {img_name}")

    print("All images have been downloaded.")

def filename():
    # 原始文件夹路
    folder_path = 'C:\\Users\\19167\\Desktop\\python\\images'

    for filename in os.listdir(folder_path):
    # 原始文件路径
        old_path = os.path.join(folder_path, filename)
    
    # 新的文件名（加上.jpg后缀）
        new_filename = f'{filename}.jpg'
        new_path = os.path.join(folder_path, new_filename)
    
        # 重命名文件
        os.rename(old_path, new_path)
        print(f'Renamed {old_path} to {new_path}')


if __name__ == "__main__":
    filename()
    # 设置目标URL
    base_url = "https://haowallpaper.com/?page={}"
    for page in range(1, 351):
        url = base_url.format(page)
        crawl(url)    
    

