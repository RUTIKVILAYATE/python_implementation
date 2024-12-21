# Exponential Backoff

# Implement an exponential backoff strategy that doubles the wait time between retries, starting from one second, but stop after 5 retries

import time


wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts+1, "-wait time ", wait_time)
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts = attempts + 1




# Conclusion 
# pahle wait_time 1 hoga
# max_retries matlab kitni baar try kr skte ho woh hogh
# phir attempts kitne huye woh hoga, basically try kitne baar kiya woh hoga

# while mein --> jab tak attempts 5 baar se kam hoge tab tak pahle attempt mein 1 milao, wait time 1 rakho
# 1 second ke liye time rok do , matlab wait time 1 second hoga
# abb wait time double krdo 
# aur attempt ko 1 se bada diya
# abb attempt 2ra hoga, wait_time 4 hoga aur, 4 second ke liye wait krwao

# waise hi attempt == 5 prr loop ruk jayega means total loop 0 se 4 yani 5 time run hoga, yani 5 attempts 

