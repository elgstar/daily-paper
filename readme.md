# Daily Paper 📚🔍

<div align="center" style="margin: 20px 0;">
  <a href="./README-CN.md" style="font-size: 16px; color: #0366d6; text-decoration: none; padding: 8px 16px; border-radius: 4px;">
    🌐 查看简体中文版
  </a>
</div>

## 🌟 Project Description

This is a **Python project** designed to automatically search for articles published the previous day in specified journals (including **Nature**, **Nature Communications**, **PRL**, **PRE**, and **GRL** in the field of space physics). The articles are filtered based on keywords, and the selected articles are sent to designated recipients via email. The project utilizes **RSS feeds** from these journals and incorporates a **7B DeepSeek model** to summarize the article abstracts. 🚀

## 🛠️ Installation Guide

### 1. **Clone the Repository**
```sh
git clone https://github.com/elgstar/daily-paper.git
cd daily-paper
```

### 2. **Install Dependencies**
```sh
pip install -r requirements.txt
```

## 📖 Usage Instructions

### 1. **Configure Environment Variables**

🔑 The project stores sensitive information such as email addresses and passwords in encrypted form. It reads a string from the environment variable `DAILY_PAPER_KEY` as the decryption key.

Therefore, in practice, you need to set the `DAILY_PAPER_KEY` environment variable and replace the corresponding ciphertext (located in the `src/user.py` file).

The `src/user.py` script provides an encryption and decryption utility. Run the following command:
```sh
python src/user.py
```
You will be prompted to enter information, and the script will output the **SHA256** hash and the encrypted ciphertext. You can replace the ciphertext with the generated one.

### 2. **Run the Script**
To manually run the script, execute the following command:
```sh
python src/main.py
```

## 📂 Project Structure

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

## 🤝 Contribution Guidelines

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to submit an **issue** or **pull request**. 🙏

## 📜 License

This project is licensed under the **MIT License**. For details, please refer to the [LICENSE](./LICENSE) file. 📜

## ❤️ Acknowledgments

Thank you to everyone who has contributed to and supported this project. ❤️
