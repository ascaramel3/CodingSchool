import time

timer_amount=0

print("~Timer~")

timer_query=input("Please set an amount of time for the timer.")

timer_amount=timer_query

timer=float(timer_amount)

print("timer start")

time.sleep(timer)

print("time up")

