# The latest <threading> module provides object oriented approach towards multi-threading in python
# <threading> module combines all the methods of <_thread> module and exposes
# a few additional ones
import threading
import time

queue = []
# Lock from the threading module can be used to ensure access to queue shared resource in a synchronized manner.
# here, the consumer will wait the acquire the thread_lock, until producer is holding it,
# while appending an element to the queue.
# and the producer will wait to acquire the lock, while consumer holds the lock to peek an element from the queue.
thread_lock = threading.Lock()


class Producer(threading.Thread):

    def __init__(self,name,limit):
        threading.Thread.__init__(self)
        self.limit = limit
        self.name = name

    def run(self):
        while self.limit > 0:
            #print("producer waiting to acquire lock!")
            thread_lock.acquire()
            time.sleep(1) # Simulated production delay
            queue.append(self.limit)
            print(queue)
            self.limit -= 1
            thread_lock.release()
            #print("producer releasing the lock")


class Consumer(threading.Thread):

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            try:
                #print("Consumer waiting to acquire lock!")
                thread_lock.acquire()
                time.sleep(1) # Simulated consumption delay
                print(queue.pop())
                thread_lock.release()
                #print("consumer releasing the lock")
            except IndexError as e: # reached the end of the queue
                print("consumer has no more elements to read from the queue")
                break


if __name__ == '__main__':
    consumer = Consumer("Consumer 1")
    producer = Producer("Producer 1",5)

    print("Running producer: ")
    producer.start()
    print("Running consumer: ")
    consumer.start() # In absence of lock, consumer thread begins, while producer sleeps for
    # 1 second attempts consuming from an empty queue and exits

    producer.join()
    consumer.join()

    print("\n\nExiting the program!")