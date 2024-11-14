import os
from openai import OpenAI

# 初始化对话记录
conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant. Please help detect if the user wants to end the conversation based on their input.'}
]

try:
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    # 循环进行多轮对话
    while True:
        user_input = input("用户：")  # 获取用户输入

        # 将用户输入追加到对话历史中
        conversation.append({'role': 'user', 'content': user_input})

        # 发送用户输入给模型，要求模型判断用户是否有结束意图
        intention_check = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {'role': 'system', 'content': 'You are an AI that determines if the user wants to end the conversation based on their input. Respond with "yes" or "no".'},
                {'role': 'user', 'content': user_input}],
                #stream=True,
        # 通过以下设置，在流式输出的最后一行展示token使用信息
        #stream_options={"include_usage": True}
        )

        # 获取模型的意图判断（直接由模型判断用户是否想结束对话）
        intention_response = intention_check.choices[0].message.content.strip().lower()

        # 如果模型认为用户有结束对话的意图
        if intention_response == "yes":
            print("助手：感谢您的咨询，再见！")
            break
        else:
            # 获取助手回复并继续对话
            completion = client.chat.completions.create(
                model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
                messages=conversation
            )
            
            # 获取助手回复
            assistant_reply = completion.choices[0].message.content
            print("助手：", assistant_reply)

            # 将助手回复追加到对话历史中
            conversation.append({'role': 'assistant', 'content': assistant_reply})

except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
