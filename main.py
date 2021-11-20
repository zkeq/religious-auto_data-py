# coding:utf-8
# 引入正则库,字符串搜索
import re
# 引入提取网页的xpath库
from lxml import etree
# 先定义一个列表,作为第一层列表使用.(后面还有排序,去重什么的)
list_end = []
# 这里进入一个循环,即为html的文件名 *.html ,左等右不等
for i in range(1, 48):
    # 定义html的文件路径
    path = '%s.html' % i
    # 以utf-8的格式打开html文件
    f = open(path, 'r', encoding='utf-8')
    # 读取html文件
    st = f.read()
    # 将html文件加载到etree中并赋值,之后可使用xpath操作
    html = etree.HTML(st)
    # 定义一个临时列表
    all_list = []
    # 获取 题目id,非字符串,为一个element对象
    _id = html.xpath('/html/body/div[2]/div[2]/div/table/tbody/tr')
    # 获取 标题和答案(这里放在一起写了,因为分开写合并的时候逻辑很混乱,很麻烦)
    title = html.xpath('//*//font')
    # 定义两个变量为接下来的循环做铺垫
    a = 0
    c = 0
    # 以id的长度进行循环 id 和 title的值都为个数 *4...,因为id有空集(下文会去除)
    # print(len(_id))
    # print(len(title))
    for index in range(len(_id)):
        # 获取到id并将其转换为字典类型
        # (这里是因为后面要传id和其他属性进入这里,就是相当于一个母版,它创建之后其他元素都往它这里面传,之后再将元素一起传入上面定义的列表中)
        _dict = dict(_id[index].attrib).get('id')
        # # try:
        # 每次循环a的值+1(下面会有),即为遍历title,
        new_title = title[a]
        # # except Exception as e:
        # # continue
        # # print(type(id_num))
        # 判断title是标题还是选项(因为标题全部都含有顿号....本来想用数字判断..写的太长逻辑没接上....
        # 所以这就要求选项中不可含有顿号,否则会被识别成标题,这之后的所以选项都会乱掉的....
        # 嘻嘻后来我找到方法了.....折腾了很长时间)
        if '、' in new_title.text and bool(re.search(r'\d', new_title.text)):
            # 是标题的话就传入列表中,为什么这样写呢?
            # 是因为这是从第二个循环开始写的
            # 因为标题进入1次,选项要进入4次
            # 而我们只需要保存一次就行了
            # 所以我们就是第一次循环的时候,保存一个0的值,
            # 第二次循环到标题才会保存接下来赋予的标题和选项的值
            all_list.append(c)
            # # # # # # # # # # # # # # # # # # # # # # # # # # # 增加标题的报错信息
            # # # # # # # # # # # # # # # # # # # # # # # # # # # try:
            # # # # # # # # # # # # # # # # # # # # # # # # # # #     # 搜索是否标题中含有数字,没有的话就抛出一个异常
            # # # # # # # # # # # # # # # # # # # # # # # # # # #     if not bool(re.search(r'\d', new_title.text)):
            # # # # # # # # # # # # # # # # # # # # # # # # # # #         raise Exception
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # 捕捉这个异常并打破循环,(因为标题和选项如果对不上的话,会全部乱掉..)
            # # # # # # # # # # # # # # # # # # # # # # # # # # # except Exception as e:
            # # # # # # # # # # # # # # # # # # # # # # # # # # #     print('触发报错,应该识别为标题的地方出现了选项(即没有数字):\n',new_title.text)
            # # # # # # # # # # # # # # # # # # # # # # # # # # #     break
            # # # # # # # # # # # # # # # # # # # # # # # # # # # 这就是赋予标题的值
            # 这个text是因为 上面说过了,这个new_titile并不是一个字符串,而是一个对象类型
            c = new_title.text
        # 判断不是标题的时候执行逻辑
        else:
            # 增加抛错提示,这里是判断是否是标题中含有数字
            if bool(re.search(r'\d', new_title.text)) or '、' in new_title.text:
                print('请确认这不是标题 || ', new_title.text)
            # 这里就是单竖杠将标题和选项隔开,然后选项之间是双竖杠隔开
            c += '|' + new_title.text + '|'
            # 因为标题会由很多的空格和换行符,这里要全部去掉
            c = c.replace('\n', '').replace('\r', '').replace('\t', '')
        # # print(new_title)
        # 将a的值+1,也就是遍历的过程
        a += 1
    # # print(all_list)
    # 将上面赋予列表的第一个没有意义的0去掉
    all_list.remove(0)
    # 因为这时候标题只剩了99个了,也就是最后一个标题没有获取到
    # 然后这里就是再加一个没有用的东西,用于和选项合并的时候不会报错
    # 当然,这样写并不好,因为后期去重的时候可能因为这个值排在前面
    # 而把真实有效的值替换掉,但是我也没有想到其他方法.... (我想到了)
    # 只能后期再补充了(反正也没几个....我测试的时候只出现了2个)
    # 我来补充: 后面加了判断,就是后面如果发现这个东西,就进入下一次循环
    # 这条数据就废弃了,但是因为数据有很多条,就是样本足够多的话,肯定可以再找到相同的数据的
    all_list.append('##$%#%$#%$#$@$$%^#%$@#%$!#^$%$#^%')
    # print(all_list)
    # 以上为标题和选项

    # 以下为id的获取
    # 再次给a赋值为0,再次进行循环(a是老工具人了hh)
    a = 0
    # 再定义一个临时列表(好像这是第三个了....)
    list_temp = []
    # 再循环一遍id的长度....
    for index in range(len(_id)):
        # 获取到id
        # # 本行无用,删了也没事好像..._dict = dict(_id[index].attrib).get('id')
        # # print(_dict)
        # 因为range是从1开始的,但我们取列表需要从0开始,所以用a
        # 这个获取到的东西是 {'id': 'topicid_XXXXXXX'} 或者为 {}
        id_num = dict(_id[a].attrib)
        # 将获取到的东西传入临时列表,准备做去除空集处理
        list_temp.append(id_num)
        # 遍历
        a += 1

    # 以下为去除空集 用emd的原因是我认为快到end了但是感觉还没到...
    list_emd = []
    # 即为对上面的临时列表进行循环
    for x in list_temp:
        # 去除标题的所有空id集合,使其总数为100
        # print(x)
        if bool(x):
            # print(x)
            # 去除空元素
            list_emd.append(x)
    # print(len(list_emd))

    # 再循环,这时循环的是去掉空集之后的标题,即为100
    for index in range(len(list_emd)):
        # print(index)
        # 将题目与选项合并后的东西传入emd中...即为列表套字典(格式需要)
        list_emd[index]['question_txt'] = all_list[index]
        # 添加占位符, 方便手动输入答案
        list_emd[index]['answer'] = '正确答案填在此'
        # 没啥用,就是好看,做个提示而已(跟原来格式保持一致....)(但是没啥用)
        list_emd[index]['answer_txt'] = '使用说明：将正确答案填入answer的引号中就可，多选不用间隔，示例 *A* *ABCD*'
    # print(len(list_emd))
    # 将每次循环html文件得到的内容传入列表中,即为列表套列表套字典..
    list_end.append(list_emd)

# print(list_end)

# new_list = sorted(all_list, key=(lambda r: r['id']))
# 将列表套列表套字典转换为列表套字典
list_end = sum(list_end, [])


# 去重
def deletedup(li):
    # 定义一个集合
    seen = set()
    # 定义空集
    new_list_2 = []
    # 对于传入的参数进行循环处理
    for d in li:
        # 即为利用id来去重
        d1 = d['id']
        # 这里就是上文所说的去掉
        str1 = d['question_txt']
        # 其实也不是去掉,就是进入下一个循环,就是不传.
        if str1 == '##$%#%$#%$#$@$$%^#%$@#%$!#^$%$#^%':
            continue
        # print(d1)
        # print(seen)
        # 如果没有这个元素才传入,有就不传
        if d1 not in seen:
            # print(d1)
            # 传入元素
            new_list_2.append(d)
            # 传入集合中,是不是集合意义不大,因为不同页面的题号不同,所有肯定不一样
            seen.add(d1)
    # 返回去重之后的列表
    return new_list_2


# 入口函数
if __name__ == '__main__':
    # 对于得到的列表去重
    list_tools = deletedup(list_end)
    # 打印信息,完成任务,下一步去格式化就好啦!
    # print(new_list_2)
    new_list = sorted(list_tools, key=lambda r: r['id'])
    print(new_list)
    # 打印警告信息和统计信息
    print('总计:', len(new_list), '条数据', '\n注意:请划到顶部确认那些东西是不是标题!!!!')
