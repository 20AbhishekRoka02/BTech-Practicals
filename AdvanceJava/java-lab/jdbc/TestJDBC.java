import java.sql.Connection;
import java.sql.DriverManager;

public class TestJDBC {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/javalab";
        String user = "javauser";
        String password = "password";

        try {
            Connection con = DriverManager.getConnection(url, user, password);
            System.out.println("Connected Successfully!");
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
