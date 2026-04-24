package com.example.dao;

import com.example.model.Student;
import com.example.util.DBConnection;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class StudentDAO {

    // CREATE
    public void insertStudent(Student s) {
        String sql = "INSERT INTO student(name, email) VALUES (?, ?)";

        try (Connection con = DBConnection.getConnection();
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setString(1, s.getName());
            ps.setString(2, s.getEmail());

            ps.executeUpdate();
            System.out.println("Inserted Successfully");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // READ
    public List<Student> getAllStudents() {
        List<Student> list = new ArrayList<>();
        String sql = "SELECT * FROM student";

        try (Connection con = DBConnection.getConnection();
             Statement st = con.createStatement();
             ResultSet rs = st.executeQuery(sql)) {

            while (rs.next()) {
                Student s = new Student(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getString("email")
                );
                list.add(s);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return list;
    }

    // UPDATE
    public void updateStudent(Student s) {
        String sql = "UPDATE student SET name=?, email=? WHERE id=?";

        try (Connection con = DBConnection.getConnection();
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setString(1, s.getName());
            ps.setString(2, s.getEmail());
            ps.setInt(3, s.getId());

            ps.executeUpdate();
            System.out.println("Updated Successfully");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // DELETE
    public void deleteStudent(int id) {
        String sql = "DELETE FROM student WHERE id=?";

        try (Connection con = DBConnection.getConnection();
             PreparedStatement ps = con.prepareStatement(sql)) {

            ps.setInt(1, id);

            ps.executeUpdate();
            System.out.println("Deleted Successfully");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
