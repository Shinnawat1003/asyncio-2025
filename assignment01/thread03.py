# extending the Thread class
from threading import Thread
from time import sleep, ctime

# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a momentAdd commentMore actions
        sleep(1)
        # display a message
        print(f'{ctime()} This is coming from another thread')

# create the thread
thread = CustomThread()
# start the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread to finish')
thread.join()
