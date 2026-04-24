<%@ page import="java.sql.*" %>
<html>
<head>
    <title>Practical 3 - Insert using JSP</title>
</head>
<body>

<%
    String url = "jdbc:mysql://localhost:3306/javalab";
    String user = "javauser";
    String password = "password";

    String name = request.getParameter("name");
    String age = request.getParameter("age");

    if(name != null && age != null) {
        try {
            Connection con = DriverManager.getConnection(url, user, password);
            PreparedStatement ps = con.prepareStatement("INSERT INTO student(name, age) VALUES (?, ?)");

            ps.setString(1, name);
            ps.setInt(2, Integer.parseInt(age));

            int i = ps.executeUpdate();

            if(i > 0) {
                out.println("Data Inserted Successfully");
            }

            con.close();
        } catch(Exception e) {
            out.println(e);
        }
    }
%>

<h2>Insert Student Data</h2>
<form method="post">
    Name: <input type="text" name="name" /><br><br>
    Age: <input type="text" name="age" /><br><br>
    <input type="submit" value="Insert" />
</form>

</body>
</html>
