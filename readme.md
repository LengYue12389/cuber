运行项目

```bash
> https://gitee.com/panshidi/registration-system.git
> cd flaskr
> python -m venv venv  #创建python虚拟环境
> .\venv\Scripts\activate.bat #激活虚拟环境
> 
> pip install -r requirements.txt # 安装项目依赖，可能不全，根据提示自行安装即可
cd static
mkdir media
cd media 
mkdir ptoto
mkdir img
mkdir banner
```
在config.py里还设置一下自己的数据库密码
以及SECRET_KEY 随便设置一个字符串就行

创建数据库 
```sql
CREATE DATABASE registration_system;
```
安装依赖以后创建数据库表
```bash
# 初始化会生成migrate文件夹
python manager.py db init
# 生成迁移文件
python manager.py db migrate
# 创建数据库表
python manager.py db upgrade 
# 运行项目
python manager.py
```

