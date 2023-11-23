import os
import time
import playsound

from clock import print_big_clock

"""
- [x] clock에서 불러다 쓸 수 있도록 하자. print_bit_clock, get_now
- [x] countdown 기능은 어떻게 표현할까?
    - [x] 전체 시간을 초로 환산하고 1초식 줄여 나간다.
    - [x] 출력은 계산을 통해 분과 초로 출력한다.
- [x] 알람기능 넣기
- [ ] 시간을 입력받을 수 있게 하자. (argparse)
- [ ] TODO 스누즈 기능 넣기
"""


def get_left_time(t):
    """Convert time to hours, minutes and seconds"""
    s = t % 60
    m = (t // 60) % 60
    h = (t - m * 60 - s) // 3600
    
    return h, m, s


def main(t):
    total_seconds = t
    h, m, s = get_left_time(total_seconds)
    while True:
        if total_seconds:
            os.system('clear')
            print_big_clock((h, m, s))
            time.sleep(0.001)
            total_seconds = total_seconds - 1
            h, m, s = get_left_time(total_seconds)
        else:
            print("Job Done!!!")
            playsound.playsound('sound/alarm.wav')
            break


if __name__ == "__main__":
    main(25 * 60)
