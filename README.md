![GIF](https://edu-image.nosdn.127.net/8CEB4BB4FFC4CE976C084DBAC4DEC415.gif)

### Python自动化脚本

### 本项目原本为https://github.com/zkeq/religious-auto 的辅助脚本

### (完整题库也在此项目中)

#### 现原项目已经失效,故本脚本只能生成题库,并无实际用途.

- 为宗教自动化答题脚本的python爬虫
- python环境:3.9
- 所需的库:`lxml` 
  -  `pip install lxml`

### 使用方法

1. 保存网页为本地文件(越多越好)
2. 将网页文件保存为html格式并放在 `main.py` 同目录下 (命名为1.html,2.html......)
3. 调整 `main.py`中的网页文件名参数(修改数字)
4. 运行 `main.py`
5. 查看是否含有报错以及相关信息,有 则必须处理(否则数据库就乱掉了)!
6. 将得到的列表传入  [json格式化页面](https://www.bejson.com/explore/index_new/)https://www.bejson.com/explore/index_new/)`(因为他这个格式化是通过英文的逗号之类的东西换行,所以会误判,但关系不大,2分钟就可以处理完)`
8. 无用: 将其填入脚本的`data.js` 的列表中 (注意格式)
9. 无用: 自行填写题目的正确选项
10. 无用: 即可使用
