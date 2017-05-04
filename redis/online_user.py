import time
import redis
from datetime import datetime

ONLINE_LAST_MINUTES = 5
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(connection_pool = pool)


def mark_online(user_id):  # 将一个用户标记为online
    now = int(time.time())  # 当前的UNIX时间戳
    expires = now + (ONLINE_LAST_MINUTES * 60) + 10  # 过期的UNIX时间戳
    all_users_key = 'online-users/%d' % (now // 60)  # 集合名，包含分钟信息
    user_key = 'user-activity/%s' % user_id
    p = r.pipeline()
    p.sadd(all_users_key, user_id)  # 将用户id插入到包含分钟信息的集合中
    p.set(user_key, now)  # 记录用户的标记时间
    p.expireat(all_users_key, expires)  # 设定集合的过期时间为UNIX的时间戳
    p.expireat(user_key, expires)
    p.execute()


def get_user_last_activity(user_id):  # 获得用户的最后活跃时间
    last_active = r.get('user-activity/%s' % user_id)  # 如果获取不到，则返回None
    if last_active is None:
        return None
    return datetime.utcfromtimestamp(int(last_active))


def get_online_users():  # 获得当前online用户的列表
    current = int(time.time()) // 60
    minutes = xrange(ONLINE_LAST_MINUTES)
    return r.sunion(['online-users/%d' % (current - x)  # 取ONLINE_LAST_MINUTES分钟对应集合的交集
                         for x in minutes])
