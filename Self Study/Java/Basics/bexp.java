import java.util.Scanner;
public class bexp {
    public int binpow(int a,int b){
        if(b==0) return 1;
        int res = binpow(a,b/2);
        if(b%2==0) return res*res;
        else return res*res*a;
    }
    public void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number a: ");
        int a = sc.nextInt();
        System.out.print("\nEnter number b:");
        int b = sc.nextInt();
        System.out.println("Result:"+binpow(a,b));
        sc.close();
    }
}
