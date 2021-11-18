# 模块1： AutoTest-python(web UI selenium )
# 去除webDriver特性：（反爬虫用）https://blog.csdn.net/MICHAELKING1/article/details/108322795
# 12306抢票 https://zhuanlan.zhihu.com/p/48077823
UI测试+接口测试(PYTHON 3.6)
pip freeze > requirements.txt
pip install -r requirements.txt

# 模块2:  小程序自动化技术：Airtest

# 模块3: 性能测试 locust
windows10 
python -m pip install locust  --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
locust 参数介绍：https://www.cnblogs.com/imyalost/p/9758189.html
##
git config --global http.sslVerify false


# git 操作
1.创建分支提交代码命令
git checkout -b xxx   1.创建分支  2. -b  分支切换到刚被创建的分支

2.提交
git add ./
git commit -m''
git push

3.切换到master分支
git checkout master

4.merge分支
git merge xxx

5.push
git push

拉取远程最新代码：
git reset --hard
git pull origin master

删除分支
git branch -d xxx

