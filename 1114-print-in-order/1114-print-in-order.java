import java.util.concurrent.Semaphore;

class Foo {
    private Semaphore sem2 = new Semaphore(0);
    private Semaphore sem3 = new Semaphore(0);

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        // Signal that the first method is done
        sem2.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        // Wait until sem2 is released by first()
        sem2.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        // Signal that the second method is done
        sem3.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        // Wait until sem3 is released by second()
        sem3.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
