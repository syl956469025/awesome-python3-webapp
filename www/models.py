# -*- coding: utf-8 -*-

import time,uuid,logging,asyncio
logging.basicConfig(level=logging.DEBUG)

from www.db import StringField,BooleanField,TextField,FloatField,Model,create_pool


def next_id():
    return '%s' % uuid.uuid4().hex

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True,default=next_id)
    email = StringField()
    passwd = StringField()
    admin = BooleanField()
    name = StringField()
    image = StringField()
    created_at = FloatField(default=time.time)





class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

async def test(loop):
    logging.info("test")
    await create_pool(loop,user='root', password='xiaoaojianghu', db='awesome', host="192.168.52.160", port=3306)
    user = User( name='Michael', email="test2@mtime.com", passwd="pass-word",image="http://tva4.sinaimg.cn/crop.128.0.1066.1066.50/9cd00a81jw8ey0g85svrij21hc0u0wqy.jpg")
    await user.save()

async def find(loop):
    await create_pool(loop,user='root', password='xiaoaojianghu', db='awesome', host="192.168.52.160", port=3306)
    rs = await User.findAll()
    print('查找测试： %s' % rs)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([find(loop)]))
loop.run_forever()
