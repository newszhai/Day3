print("--------------------10086查询服务------------------")
money=100;
liuliang=23.5;
shijian=100;
shuru=eval(input('输入1，显示当前余额\n输入2，显示当前的剩余流量，单位为G\n输入3，显示当前的剩余通话，单位为分钟\n输入0，退出自助查询系统'))
while True:
  if shuru==1:
    print("当前余额",money,"元")
    break
  elif shuru==2:
    print("当前剩余流量",liuliang,"G")
    break
  elif shuru==3:
   print("当前剩余通话时间",shijian,"分钟")
   break
  elif shuru==0:
      break
  else:
      print("输入错误")
      break