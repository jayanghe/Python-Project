## SSH连接GitHub
### 生成SSH key
```bash
$ ssh-keygen -t rsa -C "your_email@example.com"
```
按回车
cat 生成的id_rsa.pub 

### 添加SSH到Github
copy 到GitHub setting SSH添加

### 测试这个key
```bash
$ ssh -T git@github.com
```
将会有一段警告代码,输入yes,出现successfully authenticated, but GitHub does not provide shell access.表示成功

## 本地文件push到Git远程仓库
```bash
git init
git add * 
git commit -m "commit"
git remote add origin git@github.com:Username/Repositories.git   //SSH
git remote add origin https://github.com/Username/Repositories.git //Https 
git push origin master 
git push -u origin master //加上-u参数可以将本地分支和远程分支关联起来，以后推送或拉取就可以简化命令
出现fatal: refusing to merge unrelated histories
强制合并 git pull origin master --allow-unrelated-histories
--allow-unrelated-histories , 把两段不相干的 分支进行强行合并


```

