import java.sql.*;
import java.util.LinkedList;
import java.util.Map;
import java.util.Properties;
import java.util.Queue;
import java.util.concurrent.Executor;

public class ConnectionPoolImpl implements ConnectionPool {
    private Driver driver;
    private String userName;
    private String passWord;
    private String jdbcUrl;
    private int maxPoolSize;
    private int size;
    private volatile Queue<Connection> connections; // volatile, so that it doesn't use thread local cache, always read from
    //main memory.

    public ConnectionPoolImpl(Driver driver, String userName, String passWord, String jdbcUrl, int maxPoolSize, int size) throws SQLException {
        this.driver = driver;
        this.userName = userName;
        this.passWord = passWord;
        this.jdbcUrl = jdbcUrl;
        this.maxPoolSize = maxPoolSize;
        this.size = size;
        this.connections = new LinkedList<>();
        for (int i = 0; i < maxPoolSize; i++) {
            this.connections.add(createNewConnection());
        }// eager loading
    }

    private Connection createNewConnection() throws SQLException {
        java.util.Properties info = new java.util.Properties();
        info.put("user", userName);
        info.put("password", passWord);
        return driver.connect(jdbcUrl, info);
    }

    @Override
    public Connection getConnection() throws SQLException, InterruptedException {
        return getConnection(0);
    }

    @Override
    public Connection getConnection(long timeout) throws SQLException, InterruptedException {
        long tillTime = System.currentTimeMillis() + timeout;
        if (!connections.isEmpty()) {
            synchronized (this) {
                while (System.currentTimeMillis() < tillTime) { // can create starvation problem, if some erronous large value sent as ts
                    if (!connections.isEmpty())
                        return connections.poll();
                }
            }
        }
        throw new SQLException("No connection available");
    }

    @Override
    public void releaseConnection(Connection connection) {
        synchronized (this) {
            connections.add(connection);
            this.notifyAll();
        }
    }

    public Driver getDriver() {
        return driver;
    }

    public void setDriver(Driver driver) {
        this.driver = driver;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassWord() {
        return passWord;
    }

    public void setPassWord(String passWord) {
        this.passWord = passWord;
    }

    public String getJdbcUrl() {
        return jdbcUrl;
    }

    public void setJdbcUrl(String jdbcUrl) {
        this.jdbcUrl = jdbcUrl;
    }

    public int getMaxPoolSize() {
        return maxPoolSize;
    }

    public void setMaxPoolSize(int maxPoolSize) {
        this.maxPoolSize = maxPoolSize;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public Queue<Connection> getConnections() {
        return connections;
    }

    public void setConnections(Queue<Connection> connections) {
        this.connections = connections;
    }

}
