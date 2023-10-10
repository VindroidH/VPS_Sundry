# crontab 定时任务

http://c.biancheng.net/view/1092.html

``` shell
apt install crontab
service crontab status
```

``` shell
crontab -e
# 00:30 run vnstat, output log to daily.log
30 0 * * * vnstat -i eth0 -d >> /var/log/vnstat/daily.log
# 20mins echo
*/20 * * * * echo $(date) >> /var/log/test/test.log

# echo $(date) "text" >> file.log
```


crontab 时间表示

| 项目  | 含义  | 范围  |
|:-----:|:----:|:----|
| \#.1  | "\*"  | 一小时当中的第几分钟(minute) 0~59 |
| \#.2  | "\*"  | 一天当中的第几小时(hour) 0~23 |
| \#.3  | "\*"  | 一个月当中的第几天(day) 1~31  |
| \#.4  | "\*"  | 一年当中的第几个月(month) 1~12  |
| \#.5  | "\*"  | 一周当中的星期几(week) 0~7（0和7都代表星期日）|

