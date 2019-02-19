# import time,sched

# #被调度触发的函数
# def event_func(msg):
#     print("Current Time:",time.time(),'msg:',msg)
    
# if __name__=="__main__":
#     #初始化sched模块和scheduler类
#     s=sched.scheduler(time.time,time.sleep)   #scheduler的两个参数用法复杂,可以不做任何更改
#     #设置两个调度
#     s.enter(1,2,event_func,("Small event",))
#     s.enter(1,1,event_func,("Big event",))  ##四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给他
#                                             #的参数（注意：一定要以tuple给如，如果只有一个参数就(xx,)）
#     s.run()        #运行。注意sched模块不是循环的，一次调度被执行后就Over了，如果想再执行，请再次enter

# import schedule
# import time
# def job():
#     print("job is working...")
# def job_1():
#     print('job_1 is working...')
# schedule.every(1).minutes.do(job)
# schedule.every(2).seconds.do(job_1)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# 编程：牛牛有N个字符串，他想将这些字符串分类，
# 他认为两个字符串A和B属于同一类需
# 要满足以下条件：A中交换任意位置的两个字符，
# 最终可以得到B，交换的次数不限。比如：
# abc与bca就是同一类字符串。现在牛牛想知道这
# N个字符串可以分成几类。
n = int(input())
i = 0
arr = []
while i < n:
    s = input() 
    str = ''.join(sorted(s))
    print(str)
    arr.append(str)
    i += 1
print(len(set(arr)))

# import time
# print(time.asctime(time.localtime()))