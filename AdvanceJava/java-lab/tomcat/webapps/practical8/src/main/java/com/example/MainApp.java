package com.example;

import com.example.model.Student;
import com.example.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {

    public static void main(String[] args) {

        // CREATE
        Student s1 = new Student("Alpha", 90);

        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();

        session.persist(s1);

        tx.commit();
        session.close();

        System.out.println("Student inserted successfully!");
    }
}
