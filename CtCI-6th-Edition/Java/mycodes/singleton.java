import java.lang.*;

class Singleton {
    private static volatile Singleton _instance = null;

    public static Singleton getInstance() {
        if (_instance == null) {
            synchronized (Singleton.class) {
                if (_instance == null)
                    _instance = new Singleton();
            }
        }
        return _instance;
    }

    public static void main(String[] args) {
        Thread t1 = new Thread() {
            @Override
            public void run() {
                super.run();
                Singleton.getInstance();
            }
        };
        Thread t2 = new Thread() {
            @Override
            public void run() {
                super.run();
                Singleton.getInstance();
            }
        };
        t1.start();
        t2.start();
    }
}

