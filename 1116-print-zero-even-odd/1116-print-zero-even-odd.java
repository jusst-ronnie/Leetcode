import java.util.concurrent.Semaphore;
import java.util.function.IntConsumer;

class ZeroEvenOdd {
    private int n;
    private Semaphore semZero = new Semaphore(1);
    private Semaphore semOdd = new Semaphore(0);
    private Semaphore semEven = new Semaphore(0);

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // Thread A
    public void zero(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i++) {
            semZero.acquire();
            printNumber.accept(0);
            // Decide which thread to release next
            if (i % 2 != 0) {
                semOdd.release();
            } else {
                semEven.release();
            }
        }
    }

    // Thread B (Even numbers)
    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i = 2; i <= n; i += 2) {
            semEven.acquire();
            printNumber.accept(i);
            semZero.release();
        }
    }

    // Thread C (Odd numbers)
    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i = 1; i <= n; i += 2) {
            semOdd.acquire();
            printNumber.accept(i);
            semZero.release();
        }
    }
}