import time, sys

try:
    if len(sys.argv) == 2:
        seconds = int(sys.argv[1])
    else:
        seconds = abs(int(input('Enter countdown timer in seconds: ')))
    print('\nStarting.')
    count = True
    while count:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        left = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
        print(left, '\r', end='')
        if h == 0 and m == 0 and s == 0:
            print('\nFinished.')
            count = False
        time.sleep(1)
        seconds -= 1
except KeyboardInterrupt:
    print('\nExiting script.')
    sys.exit()
except:
    print('Enter a number in seconds.')
