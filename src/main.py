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
def target_date(days = 1):
    current = datetime.now(pytz.utc)
    current = current.astimezone(pytz.timezone('Asia/Shanghai'))
    return (current - timedelta(days=days)).strftime("%Y-%m-%d")


# ========================================================================= #
#
# @brief: the main function
# @info: written by Liangjin Song on 2025-02-28 at Nanchang University
#
def main():
    date = target_date()
    previous = target_date(2)
    col = collecter.Collecter()
    usr = user.User().recv
    #  ai = user.ChatAI()
    for u in usr:
        id1 = col.filter(date, u.keywords, ai)
        id2 = col.filter(previous, u.keywords, ai)
        id = list(set(id1 + id2))
        sdr = user.Sender()
        sdr.send(u, date, [col.articles[index] for index in id], previous)
        time.sleep(3)
        sdr.quit()
        time.sleep(10)


# ========================================================================= #
if __name__ == "__main__":
    main()
