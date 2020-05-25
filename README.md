# covid-19_find_chinese_roommate
帮被困海外的中国人找中国人室友，共度时艰！

谢谢你对这个开源网站感兴趣，既然在这里见面，说明你已经读过这篇微信文章：

https://mp.weixin.qq.com/s?__biz=MzI3OTA5NDQ5MA==&tempkey=MTA2Ml9JNVNLT0ZlQlAyU1NBd201eGI5RlFxdzdhYktoMm14cVB4dGRDSHhUMzlTQUh3SlhNY0FYT3ZmdEc4cU1Zbng3NnZDUnFwTl9sM2hhSW5UM1JCYjFYU043UGpJTllUYWlVWTdWSWZpVktETkdRUF9ydEQyMEh1UWs5MUNaNjJ0dldkUE1MOEpYUUxzQ09WcEt0Nkdzbm1SVUZ3OHB6V3ppcG5mSktBfn4%3D&chksm=6b4db4b05c3a3da6fd6b154e4e2dce118292923021cb1d321423424cd74aa2c226be8068a98a&mpshare=1&scene=1&srcid=0525xJKR8tdTIMQIq5bxRYEi&sharer_sharetime=1590389619632&sharer_shareid=dab52f87e0ea957afa63cf0f7437bc02#wechat_redirect


# 使用的架构
为了能让更多志愿者参与开发这个网站，我们的：

后台框架选择Django 3.0.6；

前端选择Bootstrap 4.4.1（我太不擅长前端了，不如哪位大神先做出来就用ta的框架）；

数据库为了快速开发先用Firebase，之后可以迁移；

服务器先用Heroku，因为它部署简单而且免费，之后有需求的话再迁移。


# 功能分块 / Apps
租房板块：二房东可以发布招租、租客可以找租房信息。

情报发布板块：发布各地、各机场、航空公司、海关、航班变动信息，方便大家规划回国行程。

诉求板块：发布针对航空公司、部门的投诉，对于政府撤侨等工作的呼吁等等。

个人管理板块：个人主页。

志愿者实名认证板块：在这里注册志愿者，志愿者和用户约微信视频进行实名验证。


# 备注
网站服务应当覆盖各国。

每名用户可以通过一名随机志愿者验证完成实名认证。

每名用户可以通过三名已完成实名认证的用户验证完成实名认证。

情报发布板块应当允许留言和投票，比如筛选已过时的情报。

诉求板块应当允许留言和投票。


# 致谢
不瞒大家，笔者是一个刚刚商学院毕业的几乎不会开发的新人，思路和设计一定存在非常非常非常多的不足，希望大家不吝指正。

再次感谢你愿意参与，再一次，我们共度时艰！
