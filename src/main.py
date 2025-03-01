#
# @brief: the entry of the program
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
import user, collecter, pytz, time
from datetime import datetime, timedelta

# ========================================================================= #
#
# @brief: obtain the data
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def target_date():
    current = datetime.now(pytz.utc)
    current = current.astimezone(pytz.timezone('Asia/Shanghai'))
    return (current - timedelta(days=1)).strftime("%Y-%m-%d")


# ========================================================================= #
#
# @brief: the main function
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def main():
    date = target_date()
    col = collecter.Collecter()
    usr = user.User().recv
    ai = user.ChatAI()
    for u in usr:
        id = col.filter(date, u.keywords, ai)
        sdr = user.Sender()
        sdr.send(u, date, [col.articles[index] for index in id])
        time.sleep(3)
        sdr.quit()
        time.sleep(10)


# ========================================================================= #
if __name__ == "__main__":
    main()
