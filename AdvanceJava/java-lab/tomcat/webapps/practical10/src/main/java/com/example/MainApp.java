package com.example;

import com.example.dao.StudentDAO;
import com.example.model.Student;

public class MainApp {

    public static void main(String[] args) {

        StudentDAO dao = new StudentDAO();

        // CREATE
        dao.insertStudent(new Student("Alpha", "alpha@gmail.com"));

        // READ
        System.out.println("---- All Students ----");
        dao.getAllStudents().forEach(s ->
                System.out.println(s.getId() + " " + s.getName() + " " + s.getEmail())
        );

        // UPDATE
        dao.updateStudent(new Student(1, "Updated Alpha", "updated@gmail.com"));

        // DELETE
        dao.deleteStudent(1);
    }
}
