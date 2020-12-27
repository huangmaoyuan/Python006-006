学习笔记       
1，创建虚拟环境，python -m venv <dir>。激活和离开虚拟环境可以用<dir>/bin/activate 和 deactivate。       
2，pip3 freeze > requirement.txt。将当前虚拟环境中的依赖包重定向到requirement.txt。          
3，pip3 install -r ./requirement.txt。把requirement.txt里的依赖包安装到新环境。    
4，python中的高级数据类型有coleections，nametuple，deque，Counter，orderedDict。   
5，if __name__='__main__':   只有当直接执行这个.py文件的时候执行，别的程序导入它则不执行。      
6，常用模块：time，logging，random，json，path，os。     
7，daemon进程特点：开机自启，脱离终端，后台执行。     
8，os.fork()创建子进程。os.chdir("/")修改目录为更。os.umask(0)拥有任何文件的写权限。os.setsid()进程与原来的登陆会话和进程组脱离。     
9，如果多次使用某个正则表达式，可使用re.compile()和保存正则表达式对象以便复用，可以让程序更高效。     
10，正则表达式5个常用方法：re.match, re.search, re.findall, re.sub, re.splite。     
11，/dev/null 是空设备，如不想让输出内容到终端，可把输出重定向到/dev/null。     
