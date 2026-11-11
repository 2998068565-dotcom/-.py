import streamlit as st
import json, random
from importlib import import_module

from 雌小鬼单词程序面向对象版本 import WordManager

# 网页标题与初始化
st.set_page_config(page_title="雌小鬼单词本", page_icon="😼")
st.title("雌小鬼单词本 Web 版")

# session_state 存数据
if 'manager' not in st.session_state:
    # 实例化管理器
    st.session_state.manager = WordManager('D:/code/programming-language/Python/雌小鬼单词/雌小鬼单词.json')
    # 生成一个空题目
    st.session_state.current_question = None

manager = st.session_state.manager

# 侧边栏显示状态
with st.sidebar:
    st.header("状态面板")
    st.write(f"❤️ 血量: {manager.hp}")
    st.write(f"💖 好感度: {manager.affection}")

# 网页主界面
st.subheader("开始抽背")

# 如果目前没有题目，或者点了“换一题”
if st.button("随机抽一题") or st.session_state.current_question is None:
    if not manager.words_dict:
        st.warning("词库空空如也喵！请先录入喵！")
    else:
        # 这里调用你写的方法
        key, test_words = manager._get_test_word()
        options = manager._generate_options(test_words['meaning'])
        if options:
            st.session_state.current_question = {
                "word": key,
                "correct": test_words['meaning'],
                "options": options
            }

# 渲染题目
q = st.session_state.current_question
if q:
    st.markdown(f"### 单词：**{q['word']}**")
    st.write("请选择正确的释义：")
    
    # 在网页上把四个选项渲染成按钮
    for i, opt in enumerate(q['options']):
        if st.button(f"{chr(65+i)}. {opt}", key=f"btn_{i}"):
            # 点击按钮后的逻辑
            if opt == q['correct']:
                st.success("回答正确喵！")
                manager._update_status(is_correct=True)
            else:
                st.error(f"回答错误！正确答案是 {q['correct']}")
                manager._update_status(is_correct=False)
            # 答完题把题目清空，等待下一次点击
            st.session_state.current_question = None
            st.rerun() # 强制刷新网页