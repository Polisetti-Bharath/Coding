import java.util.Scanner;
public class rev {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter your number: ");
        int num = sc.nextInt();
        int ld = 0;
        int r = 0;
        while(num!=0){
            ld = num%10;
            r=r*10+ld;
            num = num/10;
        }
        sc.close();
        System.out.println("Reverse: "+r);

    }
}
