import requests
from bs4 import BeautifulSoup

"""爬取博客网站上的"""
class climb():
    url=""
    _headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    def __init__(self,url):
        self.url=url
    def run(self):
        response= requests.get(self.url,headers=self._headers)
        response.encoding='utf-8'#确保正确解析
        if response.status_code == 200:
            # 解析HTML内容
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取文章标题  
            title_tag = soup.find('h1', class_='post-title')
            title = title_tag.text.strip() if title_tag else "标题未找到"
            
            # 提取发布时间 
            time_tag = soup.find('time', class_='post-meta-item')
            publish_time = time_tag.text.strip() if time_tag else "时间未找到"
            
            # 打印结果
            print(f"文章标题: {title}")
            print(f"发布时间: {publish_time}")
        else:
            print("请求失败，状态码:", response.status_code)


    



if __name__ == '__main__':
    # 实例化
    blog_url = 'https://cuiqingcai.com/5548.html'
    gl=climb(blog_url)
    gl.run()