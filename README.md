![GIF](https://inews.gtimg.com/newsapp_ls/0/14194170153/0.gif)

#### Python自动化脚本

- 为宗教自动化答题脚本的python爬虫

##### 使用方法

1. 保存网页为本地文件(越多越好)
2. 删除选项中的所有 '`、`',(标题里面的不要删,这是判断标题和选项的依据....)
3. 将文件放在 `end_demo.py` 同目录下
4. 调整 `end_demo.py`中的文件名参数
5. 运行 `end_demo.py`
6. 将控制台的列表粘贴至`list_zj.py`的`all_list`中
7. 运行 `all_list.py`
8. 将得到的列表传入  [json格式化页面](https://www.bejson.com/explore/index_new/)https://www.bejson.com/explore/index_new/)
9. 格式化后填入VScode中消除所有因`,`导致的换行,修复所有飘红(如non_red.js)
10. 将填入脚本的`data.js` 的列表中 (注意格式)
11. 自行填写 题目的正确选项
11. 搜索数据中的选项: `请依据id自行替换此值`,找到这几个题目自行替换( BUG不知道怎么修.... )
12. 即可使用
