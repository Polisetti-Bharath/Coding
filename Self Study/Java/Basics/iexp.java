import java.util.Scanner;
public class iexp {
    public static int binpow(int a, int b) {
        int res = 1;
        while (b > 0) {
            if (b % 2 == 1) {
                res = res * a;
            }
            a = a * a;
            b = b / 2;
        }
        return res;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number a: ");
        int a = sc.nextInt();
        System.out.print("Enter number b: ");
        int b = sc.nextInt();
        System.out.println("Result: " + binpow(a, b));
        sc.close();
    }
}
