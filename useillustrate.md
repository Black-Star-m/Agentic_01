## 初始化 & 查看
初始化仓库: git init
查看当前状态（修改了哪些文件）：git status
查看提交历史：git log
查看提交：git checkout 对应提交的哈希码
***
## 添加 & 提交
添加单个文件到暂存区：git add 文件名

添加所有修改：git add .

提交到本地仓库：git commit -m "这里写提交说明"

追加提交（不新增commit，修改上一次提交）:git commit --amend
***
## 拉取 & 推送
关联远程仓库：git remote add origin 仓库地址

拉取远程代码：git pull
推送到远程：git push
***
## 分支操作（高频）
查看所有分支：git branch

创建新分支：git branch 分支名

切换分支：git checkout 分支名
或新版：git switch 分支名

创建并直接切换：git checkout -b 分支名

合并某分支到当前分支：git merge 要合并的分支名

删除分支：git branch -d 分支名
***
## 撤销 & 回滚
放弃工作区修改（恢复到最近一次commit）：git checkout -- 文件名

取消暂存（add 后想撤回）：git reset HEAD 文件名

回退到上一个版本：git reset --hard HEAD^
***
## 其他常用
克隆远程仓库：git clone 仓库地址

暂存当前修改（临时切分支用）：git stash

恢复暂存：git stash pop

查看远程地址：git remote -v

创建文件：touch 文件名.后缀

删除文件：rm 文件名.后缀

清除当前指令页面：clear

***
github的分支名现在改成main了，，不过国内汉化版的gitee还是marster

更新文件后
1. 把所有修改的文件加入暂存区：git add .

2. 提交修改（引号里写你改了啥，随便写）：git commit -m "更新了xxx功能/修改了xxx文件"

3. 推送到 GitHub（第一次用过 -u 之后，直接 push 就行）：git push

4. 将github上的更改，比如新分支，拉到本地：git pull origin master