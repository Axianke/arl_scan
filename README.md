去年做渗透的时候往往面对多个目标一个一个看比较乏力，所以就缝了个小东西，现在转到别的岗位好久没用了，发出来让大家瞅瞅

整个目录结构，本来想从0缝合一个，后来觉得信息收集 灯塔做的还不错 ，所以研究了下灯塔的接口，利用灯塔扫描完的结果做下一步利用

![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps1.jpg)
整个工作流程如下

![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps2.jpg)

灯塔需要设置一个key，（之前用的账号密码登录后来发现会顶掉）具体设置方式在config-docker.yaml里面
![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps3.jpg)

config.ini

![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps4.jpg)

配置完毕后打开你的漏扫工具开启监听，并且打开你的灯塔添加任务，运行工具输入任务名称
![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps5.jpg)


默认没5分钟监听一次 如果灯塔扫描完了自动将url发送给漏扫进行探测，就像这样

![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps6.jpg)

当然你也可以先发送给awvs爬虫在转发给漏扫将 参数 vlun=no 下面的漏扫监听配置不变即可

复制awvs的api到配置文件中
![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps7.jpg)

运行工具

![img](https://666xianke.oss-cn-hangzhou.aliyuncs.com/img/wps8.jpg)

当然还有更多的awvs功能我没集成过来了（懒），目前打攻防前一晚上用来挂着或者平时安服大批量资产渗透还是能有点产出的，本来想把dddd、afrog、nuclei等主动式扫描也挪进来后面也搁置了

 
