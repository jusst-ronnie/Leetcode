from threading import Semaphore, Lock

class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(1)
        self.lock = Lock()
        self.h_count = 0

    def hydrogen(self, releaseHydrogen):
        self.h.acquire()
        
        releaseHydrogen()
        
        with self.lock:
            self.h_count += 1
            if self.h_count == 2:
                self.o.release()

    def oxygen(self, releaseOxygen):
        self.o.acquire()
        
        releaseOxygen()
        
        with self.lock:
            self.h_count = 0
            self.h.release()
            self.h.release()