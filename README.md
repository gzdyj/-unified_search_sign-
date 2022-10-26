### 

### 

# Python Selenium自動化领取图书馆积分

### 2022-10-26

增加调用api识别验证码功能（有概率识别失败，需要重新运行脚本）

### 2022-10-08

#### 环境说明

Python 3.10.7
IDE VsCode laste  
chrome浏览器：106.0.5249.103
chromedriver：[下载地址](http://chromedriver.storage.googleapis.com/index.html)

#### 吐槽

以前靠抽奖图书馆柜子突然变成靠读者积分排名领取，任务还多的离谱，就突发起来抓个api自动刷，谁知道一开始就是无底洞，抓的api直接调用不了，似乎有反爬（流下没有技术的泪水），然后又想到直接浏览器模拟用自动化测试Selenuium工具，现学现用可算折腾一天可算整出来了，谁知道还会每次打卡定位的地方，js随机两种格式，但是懒狗不想继续折腾了，直接异常处理加上暴力循环。直接一天随机看20本书总有五本能对。

![图书馆积分增加规则](https://cos.zinzin.cc//images_1/chrome_In8V9uYUSs.png?imageMogr2/format/webp) 

#### 目的

登陆采用等待20秒人工识别验证码，然后判断收藏书籍是否为空，不为空全部取消收藏（防止重复收藏bug），然后随机1-50000书籍编号页面，进行收藏和打卡，暂时就这么多，后续可能更新评论，委托等~~~~

<font color="red">运行后，弹出的浏览器一定要最大窗口化！</font>

#### 最后效果

![最后效果](https://cos.zinzin.cc//images_1/Code_dLYqaj519J.gif?imageMogr2/format/webp)

#### 
