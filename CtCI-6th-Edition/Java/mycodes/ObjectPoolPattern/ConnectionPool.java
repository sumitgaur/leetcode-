package ObjectPoolPattern;

import java.util.ArrayList;

class JDBCConnectionPool<Connection> extends ObjectPool {
    @Override
    Connection create() {
        return null;
    }
}
