import requests
from bs4 import BeautifulSoup

def get_css():
    """
    功能: 获取css文件
    """
    
    url = "http://greenteapress.com/thinkstats2/html/thinkstats2.css"
    r = requests.get(url)
    with open("thinkstats2.css", 'w') as f:
        f.write(r.text)
        
def get_html_and_change_bgcolor():
    """
    功能: 获取网站源文件并修改背景颜色
    """
    
    web_name_list = ['index'] + [f"thinkstats20{f'{i}'.rjust(2, '0')}" for i in range(1, 17)] ## 储存网站名称的不同点
    
    for name in web_name_list:
        url = f"http://greenteapress.com/thinkstats2/html/{name}.html" ## 共性 + 不同 = 网站名称
        r = requests.get(url) ## 访问网址
        soup = BeautifulSoup(r.text)
        num = str(soup).find("body") ## 找到body标签所在的index(返回值为对应b的index，所以后面要加4)
        text = str(soup)[:num+4] + " style = \"background-color:beige\"" + str(soup)[num+4:] ## 加上style,修改背景颜色
        with open(f"{name}.html", 'w') as f:
            f.write(text) ## 写入html文件
            
def get_picture():
    """
    功能: 获取书中的图片
    """
    
    pic_name_list = [f"thinkstats20{f'{i}'.rjust(2, '0')}" for i in range(1, 56)] + ['next', 'up', 'back'] ## 储存图片名称
    
    for name in pic_name_list:
        url = f"http://greenteapress.com/thinkstats2/html/{name}.png"
        r = requests.get(url)
        with open(f"{name}.png", 'wb') as f: ## 将图片写入文件，wb表示用二进制写入
            f.write(r.content)
            
def main():
    """
    从Think Stats官网上下载Think Stats的html版本，并且修改背景颜色
    """
    get_css()
    get_html_and_change_bgcolor()
    get_picture()
    
if __name__ == "__main__":
    main()