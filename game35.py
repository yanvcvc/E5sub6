#^_^coding=gbk ^_^
import linecache
#数据分割
f = [ x.replace('\n','') for x in linecache.getlines('a.txt')]
items = [filter(lambda k:k.startswith(str(x)),f) for x in range(1,6)]
items1 = filter(lambda k:k.startswith('A:'),f)
items2 = filter(lambda k:k.startswith('B:'),f)
items3 = filter(lambda k:k.startswith('C:'),f)
items4 = filter(lambda k:k.startswith('D:'),f)
answers = [ x.replace('\n','') for x in f if len(x) == 1 ]
#把正确答案组成一个字典，方便后面字典查询
answers_dict = { x:answers[x] for x in xrange(5)}
def test1():
    '判断用户输入的答案和正确答案是否一样，正确加2分，错误-4'
    score_list = 8
    for x in range(len(items1)):
        items_input = raw_input('{0}\n{1}\n{2}\n{3}\n{4} \n'.\
        format(str(items[x][0]),items1[x],items2[x],items3[x],items4[x]))
        if items_input.upper()  ==  answers_dict[x]:
           score_list += 2
           print '恭喜您，回答正确！ 您现在的分数是 %d' % score_list
        else:
          score_list = score_list - 4
          print '回答错误 扣除4分！ 您现在的分数是 %d' % score_list
               
         
welcome_info = raw_input('嘿嘿，欢迎来到<幸福小子>的python的小游戏世界.(y:进入,q:退出) :' )
while True:
    if welcome_info == 'y':
       raw_input('总共%d题，四个答案(A,B,C,D),选择其中一个答案，\n基础分数8分，\
    答对一题加2分，错误减4分\n按回车继续' % len(items1))
       test1()
       break
    else:
        print '成功退出！！！！！'
        break
答题小游戏解法2
#coding=gbk
import sys
import linecache
list  = raw_input('嘿嘿，欢迎来到****的python的小游戏世界.(y:进入，q：退出。)')
if  list.lower() != 'y':
    print '您已经成功退出！！！'
    sys.exit(0)
listdata = linecache.getlines('a.txt')
raw_input("规则:你现在有8个积分，以下5道问题，请输入A,B,C,D确定答案,答对得2分，答错扣4分,请按回车开始答题! ")
print "开始进入游戏咯"
mark = 8
for x in range(5):
    x *= 7
    answers = raw_input(''.join(listdata[x:x+5]))
    if answers == 'q':
        break
    if answers.upper() == listdata[x+5][0]:
        mark += 2
    else:
        mark -= 4
    if mark <= 0:
       print '您的分数已经小于0！！,请在来一次！！'
       break
    print '您现在的分数是 %d' %mark
