# 1.打印文件序列
# 2.写入文件序列
# 3.随机获取一个文本
# 4.退出操作

import json, random

words_dict = {}
flag = 0

while(True):
    print('请选择你的操作杂鱼~:\n1.打印文件序列\n2.写入文件序列\n3.随机抽取一个单词\n4.退出操作')
    user_input = input()
    try:
        flag = int(user_input)
    except ValueError:
        print("输入无效，请输入数字 1-4 !!!连这个都不会你个小杂鱼\n")
        continue
    if (flag == 1):
        try:
            with open('D:/code/programming-language/Python/雌小鬼单词.json','r',encoding='utf-8') as f:
                words_dict = json.load(f)
                print(words_dict)
        except FileNotFoundError:
            print("还没有保存任何单词哦，请先添加！")
        except json.JSONDecodeError:
            print("杂鱼！文件是空的或者格式坏了哦！选2重新录入吧！")
    
    elif (flag == 2):
            try:
                with open('D:/code/programming-language/Python/雌小鬼单词.json','r',encoding='utf-8') as f:
                    words_dict = json.load(f)
            except FileNotFoundError:
                pass

            new_word = input("请输入英文单词: ")
            new_meaning = input("请输入中文释义: ")
            words_dict[new_word] = {'meaning':new_meaning,'wrong_count':0}

            with open('D:/code/programming-language/Python/雌小鬼单词.json','w',encoding='utf-8') as f:
                 json.dump(words_dict, f, ensure_ascii=False)
            print("杂鱼杂鱼添加成功~")

    elif (flag == 3):
        try:
            with open('D:/code/programming-language/Python/雌小鬼单词.json','r',encoding='utf-8') as f:
                words_dict = json.load(f)
                if not words_dict:
                    print('还没有添加单词哦~,快去添加吧~~~')
                    continue

            keys = list(words_dict)
            weights = [words_dict[k]['wrong_count'] + 1 for k in keys]
            key = random.choices(words_dict, weights=weights, k=1)[0]
            test_words = words_dict[key]

            print('单词:%s,请输入中文释义:' % key)
            while(True):
                ch = input("请输入(或输入'显示正确答案'查看答案~~~~): ").strip()
                if (ch == '显示正确答案'):
                    print('正确答案是 %s ,臭杂鱼这都不会真弱~~~' %test_words['meaning'])
                    break
                elif (ch == test_words['meaning']):
                    if (test_words['wrong_count'] > 0):
                        test_words['wrong_count'] -= 1
                    print('回答正确！\n但是没有奖励,因为这是你本该做到的哦杂鱼~\n')
                    break
                else:
                    test_words['wrong_count'] += 1
                    print('回答错误！！！连这都不会你个杂鱼~~~,你已经错了%s遍了！！！\n请重新回答:' %test_words['wrong_count'])
            with open('D:/code/programming-language/Python/雌小鬼单词.json','w',encoding='utf-8') as f:
                json.dump(words_dict, f, ensure_ascii=False)
        except FileNotFoundError:
            print("还没有保存任何单词哦，请先添加！")
    
    elif (flag == 4):
        print('退出任务\n')
        break
    
    else:
        print('ValueFalse,please try agian.\n')
