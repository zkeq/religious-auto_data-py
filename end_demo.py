# coding:utf-8

list_end = []

from lxml import etree
for i in range(1, 8):
    path = '%s.html' % i
    f = open(path, 'r', encoding='utf-8')
    st = f.read()
    html = etree.HTML(st)
    all_list = []
    _id = html.xpath('/html/body/div[2]/div[2]/div/table/tbody/tr')
    title = html.xpath('//*//font')
    a = 0
    c = 0
    for index in range(len(_id)):
        _dict = dict(_id[index].attrib).get('id')
        # try:
        new_title = title[a]
        # except Exception as e:
        # continue
        # print(type(id_num))
        if '、' in new_title.text:
            all_list.append(c)
            c = new_title.text
        if '、' not in new_title.text:
            c += '|' + new_title.text + '|'
            c = c.replace('\n', '').replace('\r', '').replace('\t', '')
        # print(new_title)
        a += 1
    # print(all_list)
    all_list.remove(0)
    all_list.append('100、 迷信本质上是一种世界观，宗教则是少数迷信职业者骗取钱财坑害百姓的手段|正确||错误|')
    # print(all_list)

    a = 0
    list_temp = []
    for index in range(len(_id)):
        _dict = dict(_id[index].attrib).get('id')
        id_num = dict(_id[a].attrib)
        list_temp.append(id_num)
        a += 1

    list_emd = []
    for x in list_temp:
      if bool(x):
        list_emd .append(x)
    # print(list_emd)


    combine_dict = {}
    for index in range(len(list_emd)):
        # print(index)
        list_emd[index]['question_txt'] = all_list[index]
        list_emd[index]['answer'] = '正确答案填在此'
        list_emd[index]['answer_txt'] = '使用说明:将正确答案填入answer的引号中就可,多选不用间隔,示例 *A* *ABCD*'
    list_end.append(list_emd)

# print(list_end)

# new_list = sorted(all_list, key=(lambda r: r['id']))

list_end = sum(list_end, [])

def deleteDup(li):
    seen = set()
    new_list_2 = []
    for d in li:
        d1 = d['id']
        # print(d1)
        # print(seen)
        if d1 not in seen:
            # print(d1)
            new_list_2.append(d)
            seen.add(d1)
    return new_list_2


if __name__ == '__main__':
    new_list_2 = deleteDup(list_end)
    print(new_list_2)
    print('总计:', len(new_list_2), '条数据')
