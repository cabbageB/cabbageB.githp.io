# 每周心得总结

## 关于git的学习

- git的安装与环境配置

  关于git的安装，我们可以去git的官方网站（据说下载比较慢），因此我们可以用[淘宝镜像](http://npm.taobao.org/mirrors/git-for-windows/)去下载，选择最新版本无脑安装即可（UP主是这样说的），安装完成后会自动配置环境变量，我们就可以直接使用。

- **git的基本使用**

  ```shell
  
  #查看系统config
  git config --system --list
  　　
  #查看当前用户（global）配置,这里也可以看到你设置的用户名与密码
  git config --global  --list
  
  #目前对我来说常用的命令
  #从远程仓库克隆项目到本地仓库
  git clone [url]
  
  #查看指定文件状态
  git status [filename]
  
  #将新建或者修改的文件全部添加到暂存区
  git add .
  
  #将暂存区的所有修改提交到本地仓库的历史记录
  git commit -m "提示消息"
  
  #将本地的改动推送到远程仓库对应的分支上
  git push origin [分支名]
  这里origin应该是对应一个远程仓库的网址
  
  关于分支
  # 列出所有本地分支
  git branch
  
  # 列出所有远程分支
  git branch -r
  
  # 新建一个分支，并切换到该分支
  git checkout -b [branch]
  
  # 删除分支
  $ git branch -d [branch-name]
  
  # 删除远程分支
  $ git push origin --delete [branch-name]
  $ git branch -dr [remote/branch]
  
  #将新建分支推送到远程仓库
  git push origin [分支名]
  ```

- **遇到的一些问题，希望大家帮忙解答**

  在我向远程仓库推送时，最初我没有在github设置本机绑定SSH公钥，实现免密码登录，就会跳出验证界面。然后我就输入

  global --list 里设置的用户名和密码，无法登入，然后去百度在凭据管理里面找，如下

  ![平局管理](D:\文本文件\git.png)

  打开后就能看到用户名和密码，但是依旧不行，最后我使用绑定SSH公钥，解决了问题。



## Markdown的学习

关于markdown，我感觉只要以后我们经常使用，应该就能上手，使用的软件是Typora，这个需要激活这里就分享一篇知乎上的文章，可以[免费激活]([Typora激活使用指南（2023年最新版） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/661170065)).



## 关于yolov5源码detect.py，train.py的注释

 在跟着B站UP主注释完代码后，感觉学到一些参数的作用，以及打印到终端的一些信息代表什么，也了解到一些关于神经网络方面的知识 ~~左耳进右耳出~~。对于yolo训练与识别的流程有个大概的了解。

然后是训练结果

第一个是自己在网上找的动漫图片，训练效果不是很好，感觉可能动漫人物的脸有点抽象。

第二个是在宿舍拍室友弹吉他的视频，然后每30帧提取一次图片，这个的训练轮数没有第一个多但是效果要好得多，标注的物体都能准确识别出。





