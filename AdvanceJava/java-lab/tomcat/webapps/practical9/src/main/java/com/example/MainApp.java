package com.example;

import com.example.model.Feedback;
import com.example.util.HibernateUtil;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class MainApp {

    public static void main(String[] args) {

        Session session = HibernateUtil.getSessionFactory().openSession();
        Transaction tx = session.beginTransaction();

        Feedback fb = new Feedback(
                "Alpha User",
                "alpha@example.com",
                "Great website, very helpful!"
        );

        session.save(fb);

        tx.commit();
        session.close();

        System.out.println("Feedback saved successfully!");
    }
}
