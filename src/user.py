#
# @brief: user information
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
import os, hashlib, smtplib, time, base64
from cryptography.fernet import Fernet
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI

# ========================================================================= #
#
# @brief: user information
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class user_information:
    def __init__(self, keywords: str = None, email: bytes = None):
        self.keywords = keywords
        self.email = email

# ========================================================================= #
#
# @brief: compute the sha256 hash value of the input data
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def sha256(text: str, hex: bool = True) -> str:
    if hex:
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).digest()


# ========================================================================= #
#
# @brief: encrypt/decrypt the data using the AES algorithm
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Encryptor:
    def __init__(self):
        # obtain the environment variable
        key = os.environ.get("DAILY_PAPER_KEY")
        self.__check_key(key)
        self.cipher = Fernet(base64.urlsafe_b64encode(sha256(key, hex=False)))

    def __check_key(self, key: str) -> None:
        if not key:
            raise ValueError("No key found in environment variable!")
        if sha256(sha256(key)) != "9d87f119e3312568ac0b4576d37b80b8da7877342f8ae41edfa7cf8e68300708":
            raise ValueError("Invalid key found in environment variable!")
        
    def encrypt(self, plain_text: str) -> str:
        #
        # @brief: encrypt the input data using the AES algorithm with the key
        # @info: written by Liangjin Song on 2025-02-28 at Nanchang University
        #
        if not isinstance(plain_text, bytes):
            plain_text = plain_text.encode()
        return self.cipher.encrypt(plain_text).decode('utf-8')

    def decrypt(self, cipher_text: str) -> str:
        return self.cipher.decrypt(cipher_text.encode('utf-8')).decode('utf-8')

# ========================================================================= #
#
# @brief: the user class, add the user information
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class User:
    def __init__(self):
        self.recv = []
        self.__load_user()
        self.__decrypt()
    
    def __decrypt(self):
        en = Encryptor()
        for i in self.recv:
            i.email = en.decrypt(i.email)
    
    def __load_user(self):
        self.recv.append(user_information('reconnection', 'gAAAAABnxU5T7_BMttRvgKeSY_Z5QhBF8YaKpb3XSjaAgmCnl4y-63r3g0LdMSbzTeKy22y95oHUq0JIROePqdcS3abbmsiKC4DTwrAAERTWjOXlOvrHlGw='))
        self.recv.append(user_information('turbulence', 'gAAAAABnxU5T7_BMttRvgKeSY_Z5QhBF8YaKpb3XSjaAgmCnl4y-63r3g0LdMSbzTeKy22y95oHUq0JIROePqdcS3abbmsiKC4DTwrAAERTWjOXlOvrHlGw='))
        self.recv.append(user_information('shock', 'gAAAAABnxU5T7_BMttRvgKeSY_Z5QhBF8YaKpb3XSjaAgmCnl4y-63r3g0LdMSbzTeKy22y95oHUq0JIROePqdcS3abbmsiKC4DTwrAAERTWjOXlOvrHlGw='))

# ========================================================================= #
#
# @brief: chat with AI
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class ChatAI:
    def __init__(self):
        en = Encryptor()
        self.url = en.decrypt('gAAAAABnwr51W9XlIwM9JsGdysqrNt_yYkAGf4Zl0vdkeOYe1kFfln_MmWIx-32YxLI4pPFYu-GNx3UdAxiUmnRSap1kn9L70vMX2ql61ZZ6C4_kpqFBUKI=')
        self.api = en.decrypt('gAAAAABnwrxV7ntnJQHYOhQ7FrbBgPz9Us2cnfX0eQqODMqn_rluCLmCMfSg03GygHb8tnP92QwSluCBRqoSjdCTsZo_ov3Xt65-UI7U2xYCX0GS1jw2JYzVOOyHcpps4ueTqD42i96bSL_Lbru-4HeXCLKA2J2xEQ==')
        self.model = en.decrypt('gAAAAABnwryM_66nQSNZd5295KankJutIOhqd_SUUOSxrgDAf1nxMH1Dif8xb5felBDzG3g0A91pzrHeaPj116tVqXRb8-D1mSQE78i7s-3HojpO9KEhG8MaPxdS40H9Rw8LXSkxnWZJ')
        self.client = OpenAI(api_key = self.api, base_url = self.url)

    def chat(self, text: str) -> str:
        time.sleep(5)
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {"role": "system", "content": "你是一名精通中文和英文的空间物理领域的专家，能够提取给定文本的关键信息。\
                 你需要根据给定的论文摘要，从“研究方法、研究内容、研究结论”三个方面，使用简体中文进行总结。\
                 根据给定的三个方面分三段输出，使用纯文本，不要使用markdown、html等语法。"},
                {"role": "user", "content": text}
            ],
            max_tokens = 2000,
            temperature = 0.6
        )
        return response.choices[0].message.content.strip()

# ========================================================================= #
#
# @brief: generate the email content with html format
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Message:
    def __init__(self, usr: user_information, date: str, fromer: str, articles: list):
        self.date = date
        self.keywords = usr.keywords
        self.msg = MIMEMultipart()
        self.msg['From'] = fromer
        self.msg['To'] = usr.email
        self.msg['Subject'] = f'{date}空间物理文献'
        self.msg['X-Priority'] = '3'  # 3 = Normal
        self.msg['X-MSMail-Priority'] = 'Normal'
        self.msg['Importance'] = 'Normal'
        self.msg.attach(MIMEText(self.__generate_content(articles), 'html', 'utf-8'))

    def __html_frame(self, body: str) -> str:
        html = """
        <html>
        <head>
            <style>
            body { font-family: Arial, sans-serif; }
            .paper { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; }
            </style>
        </head>
        <body>
            %s
            <p></p>
            <br>
            <p>搜索时间以北京时间为标准，搜索的期刊包含Geophysical Research Letters、\
                Journal of Geophysical Research: Space Physics、\
                Space Weather、AGU Advance、Physical Review Letters、Physical Review E、\
                    Nature、Nature Commucations、Nature Physics、
                    Science、Science Advances、Astrophysical Journal Letters、Astrophysical Journal、\
                        Science Bulletin等。\
                    点击文章标题可以打开文章链接，文章总结由AI生成，仅供参考。</p>
            <p>本邮件由机器自动生成并发送，请不要回复！</p>
            <br>
            <p>祝好！</p>
            <p>文献小书童</p>
        </body>
        </html>
        """ % body
        return html
    
    def __article(self, articles: list) -> str:
        html = ''
        for i, art in enumerate(articles):
            tmp=f"""
            <br>
            <h2>论文{i+1}：<a href="{art.link}">{art.title}</a></h2>
            <p><strong>作者：</strong>{art.author}</p>
            <p><strong>期刊：</strong>{art.journal}</p>
            <p><strong>摘要：</strong>{art.abstract}</p>
            <p><strong>小书童AI：</strong>{art.aisum}</p>
            """
            html = html + tmp.strip() + '\n'
        return html

    def __body(self, articles: list) -> str:
        body = ''
        if not articles:
            title = f'您好，根据关键词{self.keywords}，没有检索到{self.date}的文章！'
            body = title
        else:
            title = f'您好，根据关键词{self.keywords}，检索到{self.date}的文章如下：'
            body = f"""
            {title}
            <br>
            <div class="paper">
            {self.__article(articles)}
            </div>
            """
        return body

    def __generate_content(self, articles: list) -> str:
        return self.__html_frame(self.__body(articles))

# ========================================================================= #
#
# @brief: send the email to the user
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
class Sender:
    def __init__(self):
        en = Encryptor()
        self.sender = en.decrypt('gAAAAABnwr0JdfzNk2T5k2JWtI3fMIyg1F5a8tl4htA6gIN1qKopDDUlx4hll0G-b55F3-KzdE7SXXU89crGmTbwF2M6MBArcg==')
        self.passwd = en.decrypt('gAAAAABnwrzo4kvtpLqdyIiYH2_4Nw3S9W_WaQCpFhqN8e-vNynCRhq5Sp-NutA_6rYUgZRgRrW3J3-rZbuNw4yZTgzH_S5x341H6PeODJggX5cwp7IBIJ0=')
        self.host = en.decrypt('gAAAAABnwr1bzKx2XUeVDbx9BIPc7wb5p6JljaJY0nfz2vCWCLoqssP-sVazKF9e9odKGvV2QYpbky1Xuokyyp5WwIu82LFGhw==')
        self.stmp = smtplib.SMTP_SSL(self.host, 465)
        self.stmp.login(self.sender, self.passwd)

    def quit(self):
        self.stmp.quit()
    
    def send(self, user: user_information, date: str, articles: list):
        fromer = formataddr(('Space Research: ' + user.keywords, self.sender))
        msg = Message(user, date, fromer, articles).msg
        try:
            self.stmp.sendmail(self.sender, user.email, msg.as_string())
        except smtplib.SMTPException as e:
                print("Failed to send email:", e)


# ========================================================================= #
#
# @brief: encrypt the input data
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
if __name__ == "__main__":
    data = input("please enter the data to encrypt:\n")
    print('\nsha256 is')
    print(sha256(data))
    en = Encryptor()
    print("\nThe encrypted data is")
    print(en.encrypt(data))

