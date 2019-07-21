# class MM(object):
#     def __init__(self):
#         #设置词典中最长字串为3
#         self.window_size = 3
#
#     def cut(self,text):
#         '''
#         对文本进行切片并匹配
#         :param text:要进行匹配的文本
#         :return: 匹配到的结果
#         '''
#         result = []
#         index = 0
#         text_length = len(text)
#         #定义词典
#         dic = ['研究','研究生','生命','命','的','起源']
#         while text_length > index:
#             piece = ''
#             #range(start,stop,step) => range(4,0,-1) => size in (4,3,2,1)
#             for size in range(self.window_size + index,index,-1):    #4,0,-1
#                 #对text进行切片，切size大小
#                 piece = text[index:size]
#                 if piece in dic:
#                     #在词典中匹配到之后，后移继续切片
#                     index = size - 1
#                     break
#             #没有匹配到，则往后移动
#             index = index + 1
#             result.append(piece+'----')
#         print(result)
#         return result

# if __name__ == '__main__':
#     text = '研究生命的起源'
#     # text = '我你他而研究生命的起源'
#     # text = '研究你生命的起源'
#     tokenizer = MM()
#     tokenizer.cut(text)


# class RMM(object):
#     def __init__(self):
#         self.window_size = 3
#
#     def cut(self,text):
#         result = []
#         index = len(text)
#         dic = ['研究','研究生','生命','命','的','起源']
#         while index > 0:
#             piece = ''
#             for size in range(index - self.window_size,index):
#                 piece = text[size:index]
#                 if piece in dic:
#                     index = size + 1
#                     break
#             index = index - 1
#             result.append(piece + '----')
#         #倒置result里面元素的位置
#         result.reverse()
#         print(result)
#         return result
#
# if __name__ == '__main__':
#     text = '研究生命的起源'
#     tokenizer1 = MM()
#     tokenizer2 = RMM()
#     MMresult = tokenizer1.cut(text)
#     RMMresult = tokenizer2.cut(text)
#
#     if len(MMresult) == len(RMMresult):
#         print("分词结果词数相同")
#         #判定是否结果相同，否则返回单字较少的
#         if MMresult == RMMresult:
#             print("分词结果相同")
#         else:
#             #判断单字数量
#             print("返回单字数量少的")
#     elif len(MMresult) < len(RMMresult):
#         print("MMresult:")
#         print(MMresult)
#     elif len(MMresult) > len(RMMresult):
#         print("RMMresult:")
#         print(RMMresult)


# class HMM(object):
#     def __init__(self):
#         pass
#
#     def try_load_model(self,trained):
#         pass
#
#     def train(self,path):
#         pass
#
#     def viterbi(self,text,states,strat_p,trans_p,emit_p):
#         pass
#
#     def cut(self,text):
#         pass
#
# class HMM(object):
#     def __init__(self):
#         import os
#
#         #存取算法中间结果，不用每次都训练模型
#         self.model_file = './data/hmm_model.pkl'
#
#         #状态值集合
#         self.state_list = ['B','M','E','S']
#         #参数加载，用于判断是否需要重新加载model_file
#         self.load_para = False
#
#     #加载已计算的中间结果，当需要重新训练时，需要初始化清空结果
#     def try_load_model(self,trained):
#         if trained:
#             import pickle
#             with open(self.model_file,'rb') as f:
#                 self.A_dic = pickle.load(f)
#                 self.B_dic = pickle.load(f)
#                 self.Pi_dic = pickle.load(f)
#                 self.load_para = True
#
#         else:
#             #状态转移概率 (状态->状态的条件概率)
#             self.A_dic = {}
#             #发射概率 (状态->词语的条件概率)
#             self.B_dic = {}
#             #状态的初始概率 (一句话第一个字被标记成S B E M的概率)
#             self.Pi_dic = {}
#             self.load_para = False
#
#     #计算转移概率、发射概率、初始概率
#     def train(self,path):
#         #重置几个概率矩阵
#         self.try_load_model(False)
#         #统计状态出现次数，求P(o)
#         Count_dic = {}
#         #初始化参数
#         def init_parameters():
#             for state in self.state_list:
#                 self.A_dic[state] = {s:0.0 for s in self.state_list}
#                 self.Pi_dic[state] = 0.0
#                 self.B_dic[state] = {}
#
#                 Count_dic[state] = 0
#
#         def makeLabel(text):
#             out_text = []
#             if len(text) == 1:
#                 #单独成词
#                 out_text.append('S')
#             else:
#                 #词首、词中、词尾
#                 out_text += ['B']+['M']*(len(text)-2)+['E']
#
#             return out_text
#
#         init_parameters()
#         line_num = -1
#
#         #观察者集合，主要是字以及标点等
#         words = set()
#         with open(path,encoding='utf8') as f:
#             for line in f:
#                 line_num += 1
#                 #去除首位空格
#                 line = line.strip()
#                 if not line:
#                     continue
#
#                 word_list = [i for i in line if i != ' ']
#                 words |= set(word_list) #更新字的集合  | 位或运算符，按照二进制做或操作
#
#                 linelist = line.split()
#
#                 line_state = []
#                 for w in linelist:
#                     line_state.extend(makeLabel(w))
#
#                 #assert断言，声明布尔值必须为真的判定，如果发生异常表明表达式为假
#                 assert len(word_list) == len(line_state)
#
#                 for k,v in enumerate(line_state):
#                     Count_dic[v] += 1
#                     if k==0:
#                         self.Pi_dic[v] += 1    #每个句子的第一个字的状态，用于计算初始状态概率
#                     else:
#                         self.A_dic[line_state[k-1]][v] += 1 #计算转移概率
#                         self.B_dic[line_state[k]][word_list[k]] = \
#                             self.B_dic[line_state[k]].get(word_list[k],0) + 1.0     #计算发射概率
#
#         self.Pi_dic = {k:v *1.0/line_num for k,v in self.Pi_dic.items()}
#         self.A_dic = {k:{k1:v1 / Count_dic[k] for k1,v1 in v.items()} for k,v in self.A_dic.items()}
#
#         #加1平滑
#         self.B_dic = {k:{k1:(v1+1)/Count_dic[k] for k1,v1 in v.items()} for k,v in self.B_dic.items()}
#
#         #序列化
#         import pickle
#         with open(self.model_file,'wb') as f :
#             #使用pickle.dump序列化对象，并将结果数据流写到文件对象中
#             pickle.dump(self.A_dic,f)
#             pickle.dump(self.B_dic,f)
#             pickle.dump(self.Pi_dic,f)
#
#         return self
#
#     def viterbi(self,text,states,start_p,trans_p,emit_p):
#         '''
#         Veterbi算法的实现，求最大概率的路径
#         :param text:
#         :param states:
#         :param start_p: 初始概率
#         :param trans_p: 转移概率
#         :param emit_p: 发射概率
#         :return:
#         '''
#         V = [{}]
#         path = {}
#         for y in states:
#             V[0][y] = start_p[y] * emit_p[y].get(text[0],0)
#             path[y] = [y]
#         for t in range(1,len(text)):
#             V.append({})
#             newpath = {}
#
#             #检验训练的发射概率矩阵中是否有该字
#             #python在一行后加 \ 作为换行标志符
#             neverSeen = text[t] not in emit_p['S'].keys() and \
#                 text[t] not in emit_p['M'].keys() and \
#                 text[t] not in emit_p['E'].keys() and \
#                 text[t] not in emit_p['B'].keys()
#             for y in states:
#                 emitP = emit_p[y].get(text[t],0) if not neverSeen else 1.0 #设置未知字单独成词
#                 (prob, state) = max(
#                     [(V[t - 1][y0] * trans_p[y0].get(y, 0) *
#                       emitP, y0)
#                      for y0 in states if V[t - 1][y0] > 0])
#
#                 V[t][y] = prob
#                 newpath[y] = path[state] + [y]
#             path = newpath
#
#         if emit_p['M'].get(text[-1],0)>emit_p['S'].get(text[-1],0):
#             (prob,state) = max([(V[len(text) - 1][y],y) for y in ('E','M')])
#         else:
#             (prob,state) = max([(V[len(text) - 1][y],y) for y in states])
#
#         return (prob,path[state])
#
#     def cut(self,text):
#         import os
#         if not self.load_para:
#             self.try_load_model(os.path.exists(self.model_file))
#         prob,pos_list = self.viterbi(text,self.state_list,self.Pi_dic,self.A_dic,self.B_dic)
#         begin,next = 0,0
#         for i,char in enumerate(text):
#             pos = pos_list[i]
#             if pos == 'B':
#                 begin = i
#             elif pos == 'E':
#                 #python yield 生成器
#                 yield text[begin:i+1]
#                 next = i+1
#             elif pos == 'S':
#                 yield char
#                 next = i+1
#         if next<len(text):
#             yield text[next:]
#
# hmm = HMM()
# hmm.train('./data/trainCorpus.txt_utf8')
#
# text='这是一个非常棒的方案!'
# # text='中文博大精深!'
# res = hmm.cut(text)
# print(text)
# print(str(list(res)))

# import jieba
# sent = '中文分词是文本处理不可或缺的一步！'
# seg_list1 = jieba.cut(sent,cut_all=True)
# str.join(sequence)方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# print('全模式：','/'.join(seg_list1))
# seg_list2 = jieba.cut(sent,cut_all=False)
# print('精确模式：','/'.join(seg_list2))
# seg_list3 = jieba.cut(sent)
# print('默认精确模式：','/'.join(seg_list3))
# seg_list4 = jieba.cut_for_search(sent)
# print('搜索引擎模式：','/ '.join(seg_list4))

def get_content(path):
    '''
    加载指定路径下的数据
    :param path:
    :return:
    '''
    # with open(path,'r',encoding='gbk',errors='ignore') as f:
    with open(path,'r',encoding='gbk',errors='ignore') as f:
        content = ''
        for l in f :
            l = l.strip()
            content += l
        return content

def get_TF (words,topK=10):
    '''
    高频词统计
    :param words:
    :param topK: 前N个高频词
    :return: 高频词数组
    '''
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w,0) + 1
    #lambda 快速构建一个匿名函数
    #python sorted函数进行排序，返回一个新的list
    #key参数传入一个自定义lambda函数，x:x[1]即根据列表中每个元组的第二个元素进行排序
    #reverse设置为True进行倒序排列，从大到小
    return sorted(tf_dic.items(),key=lambda x:x[1],reverse=True)[:topK]

def main():
    import glob
    import random
    import jieba

    #Jieba加载用户自定义词典
    jieba.load_userdict('./data/user_dict.utf8')

    #glob 通配符模块，对目录内容进行匹配
    files = glob.glob('./data/news/C000013/*.txt')
    corpus = [get_content(x) for x in files]

    #randint生成一个范围内的指定随机整数
    sample_inx = random.randint(0,len(corpus))
    # split_words = list(jieba.cut(corpus[sample_inx]))
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('./data/stop_words.utf8')]

    print('样本之一：'+corpus[sample_inx])
    print('样本分词效果：'+'/'.join(split_words))
    print('样本的TopK(10)词：'+str(get_TF(split_words)))


def stop_words(path):
    with open(path,encoding='utf8') as f :
        return [l.strip() for l in f]

main()

