from cmath import log
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver import ActionChains
import time
import re
import json
import requests

TOKEN = 'bb335dc92'
URL = 'http://www.bhshare.cn/imgcode/'  # 接口地址
# 账号
user = "2006030308"
# 密码
password = 'Yy86736734'


wd = webdriver.Chrome("chromedriver")
wd.maximize_window()
# 等待五秒
wd.implicitly_wait(5)


def login():
    # 换成自己学校统一检索的url 我这边是武汉生物工程为例
    wd.get("https://findwhsw.libsp.cn/#/readRange")

    submit = wd.find_element_by_xpath(
        '//*[@id="app"]/div/div/div[1]/div/div/div/div[3]')  # 首先创建对象
    time.sleep(1)
    ActionChains(wd).click(submit).perform()  # 点击登陆

    time.sleep(1)
    # 输入账号
    wd.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/input').send_keys(user)
    # 输入密码
    wd.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[2]/input').send_keys(password)

    # 获取图片src
    img_str = wd.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div/img').get_attribute('src')
    time.sleep(3)
    return imgcode_online(img_str)


# 图片识别
def imgcode_online(imgurl):
    """
    在线图片识别
    :param imgurl: 在线图片网址 / 图片base64编码（包含头部信息）
    :return: 识别结果
    """
    data = {
        'token': TOKEN,
        'type': 'online',
        'uri': imgurl
    }
    response = requests.post(URL, data=data)
    print(response.text)
    result = json.loads(response.text)
    if result['code'] == 200 and len(result['data']) == 4:
        print(result['data'])
        # 输入验证码
        yanzheng = wd.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[3]/input').send_keys(result['data'])
        ActionChains(wd).click(yanzheng).perform()  # 点击同意
        return 'success'
    else:
        submit = wd.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div/div')
        ActionChains(wd).click(submit).perform()  # 点击刷新
        print(result['msg'])
        return 'error'


yanzhen = login()
while (yanzhen != 'success'):
    i = 0
    i = i + 1
    if i > 5:
        break
    yanzhen = login()


# 勾选同意
submit1 = wd.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[6]/label/span/input')
ActionChains(wd).click(submit1).perform()  # 点击同意
# print("等待10秒登陆")
# for i in range(10):
#     time.sleep(1)
#     print('还剩下：' + str(10 - i))
time.sleep(0.5)

submit2 = wd.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div[4]/div')
ActionChains(wd).click(submit2).perform()  # 点击同意
# 判断验证码是否正确
# -----------


# 清空收藏


def quxiaoshoucang():
    try:
        wd.get('https://findwhsw.libsp.cn/#/personalCenter')
        wd.implicitly_wait(5)

        time.sleep(1)
        shudan = wd.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/span')

        ActionChains(wd).click(shudan).perform()  # 点击书单
        time.sleep(2)

        # 点击默认书单
        chuangjian = wd.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/a[2]')
        ActionChains(wd).click(chuangjian).perform()  # 点击创建
        time.sleep(1)
        moren = wd.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]')
        ActionChains(wd).click(moren).perform()  # 点击默认书单
        time.sleep(1)

        shoucang = wd.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[1]')
        # for i in shoucang:
        #     print(i.text)
        print(shoucang.text)
        # 把前100个的收藏拿出来用来循环取消收藏
        str = shoucang.text
        a = re.findall("\d+", str)
        a = int(a[0])

        # 收藏的书>0 则跳过
        if a > 0:
            for i in range(a):
                # 点击取消收藏
                quxiao = wd.find_element_by_xpath(
                    '//*[@id="app"]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/span/img')
                ActionChains(wd).click(quxiao).perform()  # 取消
                time.sleep(1)

                # 确定
                quxiaoqueren = wd.find_element_by_xpath(
                    '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]/span')
                ActionChains(wd).click(quxiaoqueren).perform()  # 取消确认
                time.sleep(1)
                wd.refresh()
                time.sleep(2)
                print("成功取消收藏"+str(i)+'本')
    except:
        pass


def yitiaolong():

    time.sleep(3)
    # 开始收藏
    try:
        shoucang = wd.find_element_by_xpath(
            '//*[@id="container"]/div[1]/div[1]/div[3]/div[3]/div/div[2]/span/img')
        ActionChains(wd).click(shoucang).perform()  # 点击收藏
        time.sleep(2)

        # 收藏确认
        shoucangqueren = wd.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div/div[1]/div[3]/div/button[2]/span')
        ActionChains(wd).click(shoucangqueren).perform()  # 确认收藏

        time.sleep(1)
        # 打分
        pingfen = wd.find_element_by_xpath(
            '//*[@id="container"]/div[1]/div[1]/div[3]/div[2]/div/div/div/div[2]/span[2]/ul/li[5]/div[1]/i')
        ActionChains(wd).click(pingfen).perform()  # 打分
    except BaseException:
        pass


quxiaoshoucang()
print("已清空收藏")
for i in range(20):
    id = random.randint(2, 60000)
    time.sleep(1)
    wd.get("https://findwhsw.libsp.cn/#/searchList/bookDetails/"+str(id))
    time.sleep(1)
    wd.get("https://findwhsw.libsp.cn/#/searchList/bookDetails/"+str(id))
    yitiaolong()
print("完成全部任务拉")
