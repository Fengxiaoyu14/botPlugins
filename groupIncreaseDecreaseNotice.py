# -*- coding = utf-8 -*-
# @Time : 2021/9/2 0:34
# @File : groupIncreaseDecreaseNotice.py
# @software : PyCharm

from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent


notice = on_notice()

#进群事件
@notice.handle()
async def greeting(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    if event.group_id == 780021611 or 733385409 or 279626548:
        userId = event.get_user_id()
        at_ = "[CQ:at,qq={}]".format(userId)
        msg = at_ + '欢迎新进群的小伙伴~\n****请按照【年级 学院 名字 乐器】的格式来修改群备注哦****\n\n社团QQ:3368419258' \
                    '\n编配组群:781482377\nB站:山青DS器乐社\nhttps://space.bilibili.com/1036307210\n\n' \
                    '友情链接:山大DreamSeeker器乐团(济南)\nhttps://space.bilibili.com/1434239202' \
                    '\n回复 "社团简介" 获得更多信息'
        await notice.send(Message(msg))
