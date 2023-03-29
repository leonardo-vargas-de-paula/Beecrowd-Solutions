import java.util.Scanner;

public class Main 
{
    public static void main(String[] args) 
    {
        Scanner myObj = new Scanner(System.in);

        int Op1 = myObj.nextInt();
        int Op2 = myObj.nextInt();

        int x = Op1 + Op2;

        System.out.println("X = " + x);

        myObj.close();

    }
}
