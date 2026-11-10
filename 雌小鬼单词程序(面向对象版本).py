import random, os, json

class WordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words_dict = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.words_dict = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("文件格式坏了,已重置为空字典喵")

    def save_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.words_dict, f, ensure_ascii=False)

    def add_word(self):
        new_word = input("请输入英文单词喵: ")
        new_meaning = input("请输入中文释义喵: ")
        self.words_dict[new_word] = {'meaning': new_meaning, 'wrong_count': 0}
        self.save_data()
        print("添加成功喵~")

    def show_all(self):
        print(self.words_dict)

    def test_word(self):
        if not self.words_dict:
            print("字典是空的喵！")
            return
            
        keys = list(self.words_dict)
        weights = [self.words_dict[k]['wrong_count'] + 1 for k in keys]
        key = random.choices(keys, weights=weights, k=1)[0]
        test_words = self.words_dict[key]

        print('单词:%s,请输入中文释义喵:' % key)
        while(True):
            ch = input("请输入(或输入'显示正确答案'查看答案喵~~~~): ").strip()
            if (ch == '显示正确答案'):
                print('正确答案是 %s ,臭杂鱼这都不会真弱喵~~~' % test_words['meaning'])
                break
            elif (ch == test_words['meaning']):
                if (test_words['wrong_count'] > 0):
                    test_words['wrong_count'] -= 1
                print('回答正确！\n但是没有奖励,因为这是你本该做到的哦杂鱼喵~\n')
                break
            else:
                test_words['wrong_count'] += 1
                print('回答错误！！！连这都不会你个杂鱼喵~~~,你已经错了%s遍了！！！\n请重新回答喵:' % test_words['wrong_count'])
        
        self.save_data()

    def run(self):
        while True:
            print('\n请选择你的操作杂鱼喵~:')
            print('1. 打印文件序列')
            print('2. 写入文件序列')
            print('3. 随机抽取一个单词')
            print('4. 退出操作')
            
            user_input = input()
            try:
                flag = int(user_input)
            except ValueError:
                print("输入无效喵！")
                continue

            if flag == 1:
                self.show_all()
            elif flag == 2:
                self.add_word()
            elif flag == 3:
                self.test_word()
            elif flag == 4:
                print("退出喵！")
                break

if __name__ == '__main__':
    manager = WordManager('D:/code/programming-language/Python/雌小鬼单词/雌小鬼单词.json')
    manager.run()