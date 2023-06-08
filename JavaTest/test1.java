import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number 1/3: ");
        int num1 = scanner.nextInt();
        System.out.print("Enter number 2/3: ");
        int num2 = scanner.nextInt();
        System.out.print("Enter number 3/3: ");
        int num3 = scanner.nextInt();
        //sumOfThreeNums(num1, num2, num3);
        System.out.println(sumOfThreeNums(num1, num2, num3));
        }
	
	
	public static int sumOfThreeNums(int num1, int num2, int num3) {
	    int sum = 0;
	    
	    if (num1 >= num2 && num1 >= num3) {
	        sum = num1 + Math.max(num2, num3);
	    } else if (num2 >= num1 && num2 >= num3) {
	        sum = num2 + Math.max(num1, num3);
	    } else {
	        sum = num3 + Math.max(num1, num2);
	    }
	    
	    return sum;
	}


}
