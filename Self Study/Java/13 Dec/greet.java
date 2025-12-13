import java.util.*;
public class greet {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String n = sc.next();
        System.out.println("Hello there "+n);
        sc.close();


    }
}
