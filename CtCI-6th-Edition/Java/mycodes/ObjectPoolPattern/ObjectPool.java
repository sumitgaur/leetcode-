package ObjectPoolPattern;

import java.util.Hashtable;

public abstract class ObjectPool<T> {
    private Long expiration;
    Hashtable<T, Long> locked, unlocked;

    abstract T create();

    public ObjectPool() {
        this.locked = new Hashtable<T, Long>();
        this.unlocked = new Hashtable<T, Long>();
        this.expiration = 3000L;
    }

    public Long getExpiration() {
        return expiration;
    }

    public void setExpiration(Long expiration) {
        this.expiration = expiration;
    }
}

