<html>
<head>
    <title>Practical 2 - JSP</title>
</head>
<body>
    <h2>Hello, this is JSP Program</h2>

    <%
        String name = "Student";
        out.println("Welcome " + name + "<br>");
        out.println("Current Date and Time: " + new java.util.Date());
    %>

</body>
</html>
