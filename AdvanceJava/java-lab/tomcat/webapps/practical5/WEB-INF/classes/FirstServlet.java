import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class FirstServlet extends HttpServlet {

    public void doGet(HttpServletRequest req, HttpServletResponse res)
            throws ServletException, IOException {

        res.setContentType("text/html");
        PrintWriter out = res.getWriter();

        out.println("<h2>This is First Servlet</h2>");

        RequestDispatcher rd = req.getRequestDispatcher("/second");
        rd.forward(req, res);
    }
}
