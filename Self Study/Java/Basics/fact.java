import java.util.Scanner;
public class fact{
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the value of number:");
        int n = sc.nextInt();
        int fact = 1 ;
        for(int i=1;i<=n;i++){
            fact *=i;
        }
        System.out.println("Factorial:"+fact);
        sc.close();
    }
}