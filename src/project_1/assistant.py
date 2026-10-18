"""用 Pydantic AI 试一个最小 Agent。

默认模型是 `test`，不需要 API 密钥。它会调用已注册的工具，但参数是占位值。换成真实模型时传入模型名，并设置对应的密钥，例如：

    assistant.run_sync("1+2 等于几？", model="openai:gpt-4o")
"""

from pydantic_ai import Agent

assistant = Agent(
    "test",
    instructions="你是项目里的助手。需要把两个整数相加时，调用 add。",
    output_type=str,
)


@assistant.tool_plain
def add(a: int, b: int) -> int:
    """把两个整数相加。"""
    return a + b


def run(prompt: str) -> str:
    """跑一次 Agent，返回最终文本。"""
    return assistant.run_sync(prompt).output


if __name__ == "__main__":
    print(run("请把 1 和 2 相加"))
