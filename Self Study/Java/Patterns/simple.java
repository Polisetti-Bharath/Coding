import java.util.Scanner;
public class simple{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of lines: ");
        int n = sc.nextInt();
        for(int i=1;i<n;i++){
            System.out.println("*");
        }
        sc.close();
        }
}