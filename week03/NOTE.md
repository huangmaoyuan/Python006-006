学习笔记    
1，mysql里utf8和utf-8不同。    
2，select语句的书写顺序：SELECT_FROM_WHERE_GROUPBY_HAVING_ORDERBY_LIMIT。    
3，select语句的执行顺序：FROM_WHERE_GROUPBY_HAVING_SELECT_ORDERBY_LIMIT。    
4，COUNT(*)会统计值为NULL的行，而COUNT(列名)不会统计此列为NULL的行。   
5，WHERE作用与行。HAVING和GROUPBY在一起，作用于分组。   
6，根据小表驱动大表原则选择使用EXIST还是IN。   
7，mysql不支持FULL OUTER JOIN，需要用UNION。   
8，事务的特性：原子性；一致性；隔离性；持久性。   
9，事务的隔离级别：可重复读（mysql）；读未提交；读已提交；可串行化（并发性能低）。    
10，python对比shell的优势：基础数据类型更丰富；网络功能；支持多线程；标准库丰富。      
11，调优原则：升级硬件往往比调优效果更好；调优效果会随次数增加递减；有体系的调整。    
