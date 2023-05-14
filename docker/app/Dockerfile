# 指定基础环境
FROM python:3.7
# 指定个人信息 可有可无
MAINTAINER  username<email>

# 安装项目依赖
# 拷贝当前目录下的req文件到容器的当前目录下
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -i https://pypi.douban.com/simple -r requirements.txt

# 拷贝项目代码到容器的当前路径下
COPY . .

# 运行项目
CMD gunicorn -c ./gunicorn.py manage:app
