import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DNA {
    public static void main(String[] args) throws java.io.IOException {
        int a, c, g, t;
        a = c = g = t = 0;
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int ch;
        while ((ch = in.read()) != -1) {
            ch = (char)ch;
            if (ch == 'A') {
                a += 1;
            } else if (ch == 'C') {
                c += 1;
            }
            else if (ch == 'G') {
                g += 1;
            }
            else if (ch == 'T') {
                t += 1;
            }
        }
        System.out.printf("%d %d %d %d\n", a, c, g, t);
    }
}
