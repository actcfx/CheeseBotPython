import time

timeString = "2023-05-07 00:00:00"
struct_time = time.strptime(timeString, "%Y-%m-%d %H:%M:%S")
test_time = int(time.mktime(struct_time))
now = time.time()
time_delta = test_time - now
time_delta_str = time.strftime("%H小時%M分%S秒", time.localtime(time_delta))
time_delta_str =  f'{int(time_delta / 36400)}天' + time_delta_str
print(f'距離<@988804427756478574>考試還有{time_delta_str}，去讀書！')