# -*- coding=utf-8 -*-
'''本程序功能：将json文件中指定的list或dict内容，依次存入excel'''
import json
import xlwt

def test():
    #新建excel
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet("sheet1",cell_overwrite_ok=True)

    #新建sheet页中表头
    list=[u'商品名称',u'商品ID']
    for i,item in enumerate(list): #enumerate(list)返回索引序列，同时返回下标及数据，如(0，商品名称)
        sheet.write(0,i, label=item)

    #读取json文件
    filename="/Users/lilicui/工作目录/1.json"
    with open(filename,'r') as fp:
        res=json.load(fp) #json.load将文件中json字符串转换成dict

    #取data中关键list或dict用于后续循环
    data=res["content"]["data"]
    for row,line in enumerate(data):
        sheet.write(row+1,0,line[0])
        sheet.write(row+1,1, line[1])
    book.save('/Users/lilicui/工作目录/GOODS.xls')
    fp.close()

if __name__=='__main__':
    test()

