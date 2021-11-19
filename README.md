![GIF](https://edu-image.nosdn.127.net/D97468EE8EBE2D04A09C4B76A3F55FE6.gif)

### Python自动化脚本

- 为宗教自动化答题脚本的python爬虫
- python环境:3.9
- 所需的库:`lxml` 
  -  `pip install lxml`

### 使用方法

1. 保存网页为本地文件(越多越好)
2. 删除选项中的所有 '`、`',(标题里面的不要删,这是判断标题和选项的依据....)(不删的话,执行的时候会抛出信息,也就是会检查你有没有删干净)
3. 将网页文件保存为html格式并放在 `main.py` 同目录下 (命名为1.html,2.html......)
4. 调整 `main.py`中的网页文件名参数(修改数字)
5. 运行 `main.py`
6. 查看是否含有报错以及相关信息,有 则必须处理(否则数据库就乱掉了)!
7. 将得到的列表传入  [json格式化页面](https://www.bejson.com/explore/index_new/)https://www.bejson.com/explore/index_new/)
8. 格式化后填入VScode中消除所有因`,`导致的换行,修复所有飘红(如format_Example.js文件)
`(因为他这个格式化是通过英文的逗号之类的东西换行,所以会误判,但关系不大,2分钟就可以处理完)`
9. 将其填入脚本的`data.js` 的列表中 (注意格式)
10. 自行填写题目的正确选项
11. 即可使用
