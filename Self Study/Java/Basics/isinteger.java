import java.util.*;
public class isinteger {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        if(sc.hasNextInt()){
            int num = sc.nextInt();
            System.out.println("\nNumber is integer: "+num);
        }
        else{
            System.out.println("Number is not integer");
        }
        sc.close();
    }
}
