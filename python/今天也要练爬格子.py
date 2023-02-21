#! /usr/bin/python3
'''
Author: linxuan
Description: 爬格子随机练习程序
FilePath: /scrips/python/今天也要练爬格子.py
'''

import os
import curses
import random
import time
import pickle
## 配置
DEFAULT_WEIGHT = '''
1 2 3 4 1
1 2 4 3 1
1 3 2 4 1
1 3 4 2 1
1 4 2 3 1
1 4 3 2 1
2 1 3 4 1
2 1 4 3 1
2 3 1 4 1
2 3 4 1 1
2 4 1 3 1
2 4 3 1 1
3 1 2 4 1
3 1 4 2 1
3 2 1 4 1
3 2 4 1 1
3 4 1 2 1
3 4 2 1 1
4 1 2 3 1
4 1 3 2 1
4 2 1 3 1
4 2 3 1 1
4 3 1 2 1
4 3 2 1 1
'''
CONFIG_PATH = './weight.pkl'
PRICTIME_TIME = 120 # 每次练习的时间(s)
CHANGE_WEIGHT_WAIT = 5 # 等待输入改变权重的时间(s)


stdscr = curses.initscr()
stdscr.nodelay(True)    # 不等待输入
stdscr.timeout(1000)    # 设置超时时间
tot = 0
types = []
def clear_stdscr():
    stdscr.timeout(0)
    while stdscr.getch() !=-1:
        continue
    stdscr.timeout(1000)
# 导入权重
if os.path.exists(CONFIG_PATH):
    try: 
        with open('weight.pkl', 'rb') as f:
            types = pickle.load(f)
    except:
        stdscr.addstr(0, 0, "load weight failed, use default weight")
        stdscr.refresh()
        time.sleep(5)
        stdscr.clear()
if types == []:
    types = [t.split(' ') for t in DEFAULT_WEIGHT.split('\n') if t != '']
    types = [[int(i) for i in t] for t in types]
while True:
    t = random.choices(types, weights=[t[4] for t in types], k=1)[0]
    stdscr.addstr(0, 0, "now: %d %d %d %d" % (t[0], t[1], t[2], t[3]))
    stdscr.refresh()
    left = PRICTIME_TIME

    def draw(left, total, first=False):
        stdscr.addstr(1, 0, " "*100)
        stdscr.addstr(1, 0, ("timeleft: %4d(s)" % left))
        stdscr.addstr(2, 0, " "*100)
        stdscr.addstr(2, 0, "total time: %4d(m)" % (total/60 if total != 0 else 0))
        stdscr.refresh()

    while left > 0:
        time.sleep(1)
        left -= 1
        tot += 1
        draw(left, tot)

    def change_weight():
        '''等待5s是否有按键输入，如果有则改变权重'''
        wait = CHANGE_WEIGHT_WAIT
        while wait > 0:
            stdscr.addstr(4, 0, " "*100)
            stdscr.addstr(4, 0, "press k to add weight, j to minus weight(timeout: %ds)" % wait)
            stdscr.refresh()
            input = stdscr.getch() # 获取键盘输入,timeout=1000ms
            if input == ord('k'):
                t[4] += 1
                stdscr.addstr(4, 0, " "*100)
                stdscr.addstr(4, 0, "add weight success")
                stdscr.refresh()
                time.sleep(1)
                break
            elif input == ord('j'):
                t[4] -= (1 if t[4] > 0 else 0)
                stdscr.addstr(4, 0, " "*100)
                stdscr.addstr(4, 0, "minus weight success")
                stdscr.refresh()
                time.sleep(1)
                break
            wait -= 1
        if wait != 0:
            # 保存权重，保存为pyton原生支持的pickle格式
            with open(CONFIG_PATH, 'wb') as f:
                pickle.dump(types, f)
        stdscr.addstr(4, 0, " "*100)
        stdscr.refresh()
        
    change_weight()

    stdscr.clear()
    stdscr.refresh()
    clear_stdscr()
