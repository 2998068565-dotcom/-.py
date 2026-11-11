import random, os, json

class WordManager:
    def __init__(self, file_path):
        # 初始化
        self.file_path = file_path
        self.words_dict = {}
        self.load_data()
        self.hp = 100
        self.affection = 50

    def load_data(self):
        # 加载数据
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.words_dict = json.load(f)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("文件格式坏了,已重置为空字典喵")

    def save_data(self):
        # 保存数据
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.words_dict, f, ensure_ascii=False)

    def add_word(self):
        # 添加单词
        new_word = input("请输入英文单词喵: ")
        new_meaning = input("请输入中文释义喵: ")
        self.words_dict[new_word] = {'meaning': new_meaning, 'wrong_count': 0}
        self.save_data()
        print("添加成功喵~")

    def show_all(self):
        # 打印序列
        print(self.words_dict)

    def _get_test_word(self):
        # 按权重随机抽取单词
        keys = list(self.words_dict)
        weights = [self.words_dict[k]['wrong_count'] + 1 for k in keys]
        key = random.choices(keys, weights=weights, k=1)[0]
        test_words = self.words_dict[key]
        return key, test_words

    def _generate_options(self, correct_meaning):
        # 获取四个选项
        all_meanings = list(set(v['meaning'] for v in self.words_dict.values()))
        if len(all_meanings) < 4:
            return None
        all_meanings.remove(correct_meaning)
        wrong_opstions = random.sample(all_meanings, 3)
        options = [correct_meaning] + wrong_opstions
        random.shuffle(options)
        return options

    def _update_status(self, is_correct):
        # 状态参数(好感度，血量)
        if is_correct:
            self.hp = min(100, self.hp + 5)
            self.affection += 10
            if self.affection > 200:
                print("主人好厉害喵，好喜欢主人喵，想帮主人炸金喵~~~")
        else:
            self.hp -= 10
            self.affection -= 5
            if self.hp <= 0:
                print("嘤嘤嘤，杂鱼已经没救了，程序强制关闭喵！")
                exit()

    def test_word(self):
        if not self.words_dict:
            print("字典是空的喵！")
            return
        # 随机获取单词
        key, test_words = self._get_test_word()

        # 随机获取四个选项
        options = self._generate_options(self.test_word['meaning'])
        if not options:
            print("字典单词不够喵，先去补充字典喵~")
            return

        print(f'\n【血量: {self.hp} | 好感度: {self.affection}】')
        print(f'单词: {key}，请选择正确的释义喵:')
        for i, opts in enumerate(options):
            print(f"{chr(65+i)}.{opts}")
        # 问答板块
        while(True):
            ch = input("请输入选项(A/B/C/D)，或输入'显示正确答案': ").strip().upper()
            
            if ch == '显示正确答案':
                print(f'正确答案是 {test_words["meaning"]}，臭杂鱼这都不会真弱喵~~~')
                self._update_status(is_correct=False)
                break
                
            # 判断用户输入的是不是 A, B, C, D
            elif ch in ['A', 'B', 'C', 'D']:
                # 利用 ASCII 码把字母转成索引：A->0, B->1, C->2, D->3
                choice_index = ord(ch) - ord('A')
                user_choice = options[choice_index] 
                
                if user_choice == test_words['meaning']:
                    print('回答正确！但是没有奖励喵~\n')
                    if test_words['wrong_count'] > 0:
                        test_words['wrong_count'] -= 1
                    self._update_status(is_correct=True)
                else:
                    print(f'回答错误！！！你选了 {user_choice}，连这都不会你个杂鱼喵~~~\n')
                    test_words['wrong_count'] += 1
                    self._update_status(is_correct=False)
                break
                
            else:
                print("杂鱼！只能输入 A、B、C、D 喵！请重新输入：")
                
        # 保存
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