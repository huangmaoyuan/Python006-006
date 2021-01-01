学习笔记       
1，python的优点：语言简洁；胶水语言，可把多个业务串起来；自动化测试；库多。     
2，python的缺点：是动态语言，没有类型检查，多人协作容易挖坑；速度相对较慢，高并发不适合用python。        
3，python没有编译器，只有解释器。     
4，requests库对下层网络做了封装，相对用sokect库编程相对简单。    
5，http状态码：1xx 信息响应；2xx 成功响应；3xx 重定向；4xx 客户端响应；5xx 服务端响应。         
6，cookie包括登陆后验证过的信息。    
7，异常捕获：try：。。。except Exception as e。     
8，自定义异常需要继承Exception 类，后面可以用raise来抛出这个异常。    
9，finally无论有无异常都会执行。    
10，可以用with open来打开一个文件。   
11，类似__xxx___叫魔术方法。     
12，可以用P=Path（____file____）获取当前文件路径。    
13，把两个列表关联成字典：list3=dict(zip(list1,list2))。       
