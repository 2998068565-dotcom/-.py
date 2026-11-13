import customtkinter as ctk
from 雌小鬼单词程序面向对象版本 import WordManager

manager = WordManager('D:/code/programming-language/Python/雌小鬼单词程序/雌小鬼单词.json')

# 初始化
app = ctk.CTk()
app.iconbitmap('图标.ico')
app.title('杂鱼杂鱼~')
app.geometry("500x400")

# 深色
ctk.set_appearance_mode('dark')

# 状态标签
status_label = ctk.CTkLabel(app, text=f"❤️ 血量: {manager.hp} | 💖 好感度: {manager.affection}", font=("微软雅黑", 16))
status_label.pack(pady=10)

# 标题标签
word_label = ctk.CTkLabel(app, text="单词抽查", font=("微软雅黑", 24))
word_label.pack(pady=50)

# 选项按钮
options_button = []
for i in range(4):
    btn = ctk.CTkButton(app, text=f"{chr(65+i)}", font=("微软雅黑", 14))
    options_button.append(btn)

# 抽题按钮
button = ctk.CTkButton(app, text='抽题', font=("微软雅黑", 14))
button.pack()

# 存储选项信息的字典
check = {}

# 整合逻辑，生成题目和选项
def option_select():
    global check
    if not manager.words_dict:
        word_label.configure(text = '词库是空的喵！！！')
        return

    key, test_words = manager._get_test_word()
    options = manager._generate_options(test_words['meaning'])

    if not options:
        word_label.configure(text = '词库的单词不够喵！！！')
        return

    # 保存选项信息
    check = {
        "word": key,
        "correct": test_words['meaning'],
        "options": options
    }

    button.pack_forget()
    # 更新选项显示
    for i in range(4):
        options_button[i].configure(text=f'{chr(65+i)}.{options[i]}')
    for btn in options_button:
        btn.pack(pady=5)
    word_label.configure(text=f'{key}')

def check_answer(idx):
    global check
    if not check:
        return
    user_choice = check['options'][idx]
    if user_choice == check['correct']:
        word_label.configure(text = "狗修金答对了喵，狗修金好厉害喵！")
        manager._update_status(is_correct=True)
    else:
        word_label.configure(text = "杂鱼杂鱼答错了喵~~~")
        manager._update_status(is_correct=False)

    # 按钮恢复
    for btn in options_button:
        btn.pack_forget()
    button.pack(pady=20)
    check = {}

    # 状态更新
    status_label.configure(text=f"❤️ 血量: {manager.hp} | 💖 好感度: {manager.affection}")

# 绑定函数和按钮
button.configure(command=option_select)
for i in range(4):
    btn = options_button[i]
    btn.configure(command= lambda idx=i : check_answer(idx))

# 循环
app.mainloop()
