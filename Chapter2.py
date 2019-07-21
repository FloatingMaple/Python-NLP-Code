# import re
# text_string = '文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。'
# # regex = '爬虫'
# # regex = '爬.'
# # regex = '^文本'
# regex = '信息$'
# #以句号为分隔符通过split切分段落为句子
# p_string = text_string.split('。')
# for line in p_string:
#     if re.search(regex,line) is not None:
#         print(line)

# import re
# text_string = ['[重要的]今年第七号台风23日登录广州东部沿海地区','上海发布车库销售管理通知：违规者暂停网签资格','[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']
# #使用^表示起始
# #存在“重要”或“紧要”，使用[]匹配多个字符
# #以“..”代表之后的两个字符
# regex = '^\[[重紧]..\]'
# for line in text_string:
#     if re.search(regex,line) is not None:
#         print(line)
#     else:
#         print("not match")

# import  re
# # if re.search("\\\\","I have one nee\dle") is not None:
# if re.search(r"\\","I have one nee\dle") is not None:
#     print("match it")
# else:
#     print("not match")

# import re
# strings = ['War of 1812','There are 5280 feet to a mile','Happy New Year 2019!']
# year_strings=[]
# for string in strings:
#     if re.search('[1-2][0-9]{3}',string):
#         year_strings.append(string)
# print(year_strings)

# import re
# years_string = '2016 was a good year,but 2017 will be better!'
# years = re.findall('[2][0-9]{3}',years_string)
# print(years)

# import numpy as np
# #通过array可以将向量直接导入
# vector = np.array([1,2,3,4])
# #通过array也可以将矩阵导入
# matrix = np.array([[1,'Tim'],[2,'Joey'],[3,'Johnny'],[4,'Frank']])
# print(vector)
# print(matrix)

# import numpy as np
# array = np.arange(12)
# print(array)
# matrix = array.reshape(3,4)
# print(matrix)
# print(matrix.shape)

# import numpy as np
# #genfromtxt默认comments为#，即数据中由#标注的数据将被注释掉
# nfl = np.genfromtxt("D:/Code/Python-NLP-Code/source/price.csv",delimiter="\t",comments="##",dtype='U75')
# print(nfl)

# import numpy as np
# # genfromtxt默认comments为#，即数据中由#标注的数据将被注释掉
# # dtype设置为U75,即每个值都是75byte的Unicode。
# # skip_header设置为整数，意思是跳过文件开头的X行。
# nfl = np.genfromtxt("D:/Code/Python-NLP-Code/source/price.csv",delimiter="\t",comments="##",dtype='U75',skip_header=1)
# print(nfl)

# import numpy as np
# matrix = np.array([[1,2,3],[20,30,40]])
# print(matrix[0,1])

# import numpy as np
# matrix = np.array([
#     [5,10,15],
#     [20,25,30],
#     [35,40,45]
# ])
# #选择所有行且列的索引是1的数据
# print(matrix[:,1])
# print()
# #选择所有行且列的索引是0和1的数据
# print(matrix[:,0:2])
# print()
# #选择行的索引是1和2且所有列的数据
# print(matrix[1:3,:])
# print()
# #选择行的所以是1和2且列的索引是0和1的数据
# print(matrix[1:3,0:2])

# import numpy as np
# matrix = np.array([
#     [5,10,15],
#     [20,25,30],
#     [35,40,45]
# ])
# #判断matrix矩阵中的每个值是否等于25
# m = (matrix == 25)
# print(m)

# import numpy as np
# matrix = np.array([
#     [5,10,15],
#     [20,25,30],
#     [35,40,45]
# ])
# #matrix[:,1]选取所有行切索引为1的列的数据，然后判断是否等于25
# second_column_25 = (matrix[:,1] == 25)
# print(second_column_25)
# #展示返回true值的那一行数据
# print(matrix[second_column_25,:])
# #更清晰的展示上面的作用，即选择True行的数据展示
# print(matrix[[True,True,False],:])

# import numpy as np
# vector = np.array([5,10,15,20])
# #在数组中利用
# #判断等于5或10，得到一个布尔值数组
# equal_to_ten_or_five = (vector == 10) | (vector == 5)
# #利用布尔值数组将值替换为50
# vector[equal_to_ten_or_five] = 50
# print(vector)
# #在矩阵中利用
# matrix = np.array([
#     [5,10,15],
#     [20,25,30],
#     [35,40,45]
# ])
# #将第二列中为25的值替换为10
# second_column_25 = matrix[:,1] == 25
# matrix[second_column_25,1] = 10
# print(matrix)

# import numpy as np
# matrix = np.array([
#     ['','10','15'],
#     ['20','25','30'],
#     ['35','40','']
# ])
# second_column_25 = (matrix[:,2] == '')
# matrix[second_column_25,2] = '0'
# print(matrix)

# import numpy as np
# vector = np.array(["1","2","3"])
# #从string转为float类
# #如果含非数字类型，会报错
# vector = vector.astype(float)
# print(vector)

import numpy as np
#数组例子
vector = np.array([5,10,15,20])
print(vector.sum())
#矩阵例子
matrix = np.array([
    [5,10,15],
    [20,10,30],
    [35,40,45]
])
#axis=1计算行的和
print(matrix.sum(axis=1))
#axis=0计算列的和
print(matrix.sum(axis=0))