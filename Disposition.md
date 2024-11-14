# 配置API Key到环境变量
建议您把API Key配置到环境变量，从而避免在代码里显式地配置API Key，降低泄漏风险

- windows系统 PowerShell
### 添加临时性环境变量
```powershell
# 用您的 DashScope API Key 代替 YOUR_DASHSCOPE_API_KEY
$env:DASHSCOPE_API_KEY = "YOUR_DASHSCOPE_API_KEY"
```
您可以在当前会话运行以下命令检查环境变量是否生效。
```powershell
echo $env:DASHSCOPE_API_KEY
```

### 添加永久性环境变量
```powershell
# 用您的 DashScope API Key 代替 YOUR_DASHSCOPE_API_KEY
[Environment]::SetEnvironmentVariable("DASHSCOPE_API_KEY", "YOUR_DASHSCOPE_API_KEY", [EnvironmentVariableTarget]::User)
```
打开一个新的PowerShell窗口。
在新的PowerShell窗口运行以下命令，检查环境变量是否生效。
```powershell
echo $env:DASHSCOPE_API_KEY
```


# 选择开发语言 配置虚拟环境
如果您的Python已安装完成，可以创建一个虚拟环境来安装OpenAI Python SDK或DashScope Python SDK，这可以帮助您避免与其它项目发生依赖冲突。
您可以运行以下命令，创建一个命名为.venv的虚拟环境：
```powershell
# 如果运行失败，您可以将python替换成python3再运行
python -m venv .venv
```

激活虚拟环境创建虚拟环境

您可以运行以下命令，创建一个命名为.venv的虚拟环境：

# 如果运行失败，您可以将python替换成python3再运行
python -m venv .venv
- 如果您使用windows系统，请运行以下命令来激活虚拟环境：
 ```powershell
 .venv\Scripts\activate
```

如果您使用macOS或者Linux系统，请运行以下命令来激活虚拟环境：
 ```powershell
 source .venv/bin/activate
```

## 调用大模型api
openAI Python SDK 参考以下代码发送API请求
```python
import os
from openai import OpenAI

try:
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '你是谁？'}
            ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(f"错误信息：{e}")
    print("请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
