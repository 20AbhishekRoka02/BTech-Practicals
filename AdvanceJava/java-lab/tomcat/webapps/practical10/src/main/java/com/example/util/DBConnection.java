package com.example.util;

import java.sql.Connection;
import java.sql.DriverManager;

public class DBConnection {

    public static Connection getConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            return DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/cruddb",
                "crud_user",        // change if needed
                "password123"     // change if needed
            );

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
