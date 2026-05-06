from typing_extensions import TypedDict, Annotated
import operator
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# ====================== 1. 定义State + 绑定Reducer ======================
class MyState(TypedDict):
    # 对话消息：使用add_messages 【追加合并，不覆盖】
    messages: Annotated[list, add_messages]
    # 数字计数器：使用operator.add 【累加合并】
    num: Annotated[int, operator.add]
    # 普通字段：无Reducer 【默认直接覆盖】
    info: str

# ====================== 2. 定义图节点 ======================
def node_1(state: MyState) -> MyState:
    """第一个节点：往state里写第一批数据"""
    return {
        "messages": [HumanMessage(content="第一次发送消息")],
        "num": 1,
        "info": "初始信息"
    }

def node_2(state: MyState) -> MyState:
    """第二个节点：更新数据，测试Reducer效果"""
    return {
        "messages": [HumanMessage(content="第二次追加消息")],
        "num": 2,
        "info": "信息被覆盖了"
    }

# ====================== 3. 构建流程图 ======================
builder = StateGraph(MyState)

# 添加节点
builder.add_node("node1", node_1)
builder.add_node("node2", node_2)

# 连线：开始 → node1 → node2 → 结束
builder.add_edge(START, "node1")
builder.add_edge("node1", "node2")
builder.add_edge("node2", END)

# 编译图
graph = builder.compile()

# ====================== 4. 执行运行 ======================
if __name__ == "__main__":
    result = graph.invoke({})
    print("=== 最终State结果 ===")
    print("messages 列表长度:", len(result["messages"]))
    print("messages 内容:", [m.content for m in result["messages"]])
    print("num 累加结果:", result["num"])
    print("info 最终值:", result["info"])