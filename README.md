通过通义千问api，使用python语言，调用大模型（openAI）完成控制台的输出
更改示例代码，支持多轮对话和智能识别用户离开意图
拓展：支持流式输出

【参考文档】
环境确认：https://help.aliyun.com/zh/model-studio/getting-started/first-api-call-to-qwen
API参考：https://help.aliyun.com/zh/model-studio/developer-reference/dashscopellm

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

### 激活虚拟环境创建虚拟环境

您可以运行以下命令，创建一个命名为.venv的虚拟环境：
```powershell
# 如果运行失败，您可以将python替换成python3再运行
python -m venv .venv
```

- 如果您使用windows系统，请运行以下命令来激活虚拟环境：
 ```powershell
 .venv\Scripts\activate
```

可能出现以下报错：
 ```powershell
venv\Scripts\activate :无法加载文件C:\Users\Administrator\.venv\Scripts\Activate.psl,因为在此系统上禁止运行脚本。有关详细信息;请参阅https:/go.microsoft.com/fwlink/?Link/?LinkID=135170中的_about_Execution_Policies
所在位置行:1字符:1
. venv\Scripts\activate
+ CategoryInfo SecurityError : (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
```
在管理员PowerShell窗口中，输入以下命令，并按Enter：
 ```powershell
 Set-ExecutionPolicy RemoteSigned
```
按Y

如果您使用macOS或者Linux系统，请运行以下命令来激活虚拟环境：
 ```powershell
 source .venv/bin/activate
```
### 安装模型调用SDK
您可以通过OpenAI的Python SDK或DashScope的Python SDK来调用百炼平台上的模型。

安装OpenAI Python SDK安装DashScope Python SDK
通过运行以下命令安装DashScope Python SDK：
 ```powershell
pip3 install -U dashscope
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
