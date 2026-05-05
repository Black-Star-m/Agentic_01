# ======================
# 1、先定义两个工具函数（实际干活的）
# ======================
def calculator(a, b):
    """计算器工具"""
    return a * b

def search(keyword):
    """搜索工具"""
    return f"[搜索结果]关于 {keyword} 的相关资料"

# 工具映射：大写工具名 映射 真实函数
tool_map = {
    "CALCULATOR": calculator,
    "SEARCH": search
}

# ======================
# 2、模拟 LLM 逻辑
# 真实场景这里调用大模型，这里直接模拟输出规定格式文本
# 规则：只能输出 大写工具名(参数) 格式
# ======================
def llm_response(user_input):
    # 系统提示词里告诉LLM：计算用CALCULATOR，查资料用SEARCH
    if "乘" in user_input or "乘以" in user_input:
        # LLM 只输出固定格式文本，不是执行代码
        return "CALCULATOR(a=123, b=456)"
    elif "搜索" in user_input:
        return "SEARCH(keyword=人工智能发展历史)"
    else:
        return "不需要使用工具，直接回答问题"

# ======================
# 3、核心：解析 LLM 输出的工具调用文本
# 提取 工具名、参数
# ======================
def parse_tool_call(text):
    # 简单解析：匹配 大写工具名(xxx=xxx,xxx=xxx)
    if "CALCULATOR" in text:
        tool_name = "CALCULATOR"
        a = 123
        b = 456
        return tool_name, {"a":a, "b":b}
    elif "SEARCH" in text:
        tool_name = "SEARCH"
        return tool_name, {"keyword":"人工智能发展历史"}
    else:
        return None, None

# ======================
# 4、完整 Agent 主流程
# ======================
if __name__ == "__main__":
    # 用户提问
    user_question = "帮我算一下123乘以456"
    print("用户提问：", user_question)

    # 第一步：交给LLM，生成工具调用字符串
    llm_text = llm_response(user_question)
    print("LLM输出原始文本：", llm_text)

    # 第二步：程序解析 工具名+参数
    tool_name, params = parse_tool_call(llm_text)

    if tool_name:
        # 第三步：程序手动调用对应的工具函数
        func = tool_map[tool_name]
        res = func(**params)
        print("工具执行结果：", res)
        # 第四步：把结果再丢给LLM，让它整理成人话回答
    else:
        print("LLM直接回答：", llm_text)
