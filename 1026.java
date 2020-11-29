import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
    	Scanner scan = new Scanner(System.in);
    	String num1, num2;
    	while (scan.hasNextLong()) {
    		num1 = Long.toBinaryString(scan.nextLong());
            num2 = Long.toBinaryString(scan.nextLong());
	        String total = "";
	        for (int i = 1; i <= num1.length() || i <= num2.length(); i++) {
	        	int tot = 0;
	        	if (i > num1.length()) tot = Character.getNumericValue(num2.charAt(num2.length()-i));
	        	else if (i > num2.length()) tot = Character.getNumericValue(num1.charAt(num1.length()-i));
	        	else if (Character.getNumericValue(num1.charAt(num1.length()-i)) != Character.getNumericValue(num2.charAt(num2.length()-i))) tot = 1;
	        	
	        	total = tot+total;
	        }
	        System.out.println(Long.parseLong(total,2));
    	}
    	scan.close();
    }

}
