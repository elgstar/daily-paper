# Daily Paper 📚🔍

## 🌟 项目简介

这是一个 **Python 项目**，旨在每天自动搜索指定期刊（包括 **Nature**、**Nature Communications**、**PRL**、**PRE**、**GRL** 空间物理领域的期刊）中前一天发布的文章，并根据关键词进行筛选。筛选出的文章将通过电子邮件发送给指定的收件人。项目利用了这些期刊的 **RSS 订阅**，并搭配了一个 **7B的DeepSeek 模型** 对文章摘要进行总结。🚀

## 🛠️ 安装指南

### 1. **克隆仓库**
```sh
git clone https://github.com/elgstar/daily-paper.git
cd daily-paper
```

### 2. **安装依赖**
```sh
pip install -r requirements.txt
```

## 📖 使用说明

### 1. **配置环境变量**

🔑 项目将电子邮件地址、密码等信息以密文的形式存储，并从名为 `DAILY_PAPER_KEY` 的环境变量中读取一个字符串作为密钥对加密信息进行解密。

因此，在实际使用时，需要设置 `DAILY_PAPER_KEY` 环境变量，并替换相应的密文（位于 `src/user.py` 文件中）。

`src/user.py` 脚本提供了加密解密程序。执行以下命令：
```sh
python src/user.py
```
会要求输入信息，并给出输入信息的 **SHA256** 和加密后的密文。可以将得到的密文进行替换。

### 2. **运行脚本**
如果需要手动运行脚本，可以执行以下命令：
```sh
python src/main.py
```

## 📂 项目结构

```text
daily-paper/
├── .github/
│   └── workflows/
│       └── run-main-py.yml
├── src/
│   ├── main.py 🎯
│   ├── user.py 🧑‍💻
│   └── collector.py 📋
├── requirements.txt
├── README.md
├── README-CN.md
└── LICENSE
```

## 🤝 贡献指南

欢迎贡献！如果你发现任何问题或有改进建议，请随时提交 **issue** 或 **pull request**。🙏

## 📜 许可证

本项目采用 **MIT 许可证**，详情请参阅 [LICENSE](./LICENSE) 文件。📜

## ❤️ 致谢

感谢所有为本项目提供帮助和支持的人。❤️
