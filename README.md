# UESTC 电子科技大学网络认证 Docker
------------------------------
### 介绍
- 学校的宿舍电信、移动宽带自动登录
- 主楼校园网自动登录
------------------------------

### 使用
- 支持登录以下类型的网络
```angular2html
- 校园网有线接入+学号认证
- 移动、电信寝室宽带有线接入+学号认证
```
Docker 镜像已经上传到 Docker Hub，可以直接使用. network参数为网络类型，可选值为 uestc | dx | cmcc (校园网|电信|移动)
```angular2html
docker run -d --name uestc-network-auth --restart=always --network=host 
-e id=学号 -e passwd=密码 -e network=uestc ly1998117/uestc-login
```
------------------------------
### 感谢
- 基于 https://github.com/b71db892/AutoLoginUESTC 修改并打包