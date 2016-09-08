
package sumofdigitsofprime;

import java.math.BigInteger;

/**
 *
 * @author arvganesh
 */
public class SumOfDigitsOfPrime {
    public static BigInteger factorial(long n) {
       BigInteger fact = new BigInteger("1");
       for (int i = 1; i <= n; i++) {
           fact = fact.multiply(new BigInteger(i + ""));
       }
       return fact;
   }
    public static int sumOfDigits(BigInteger b) {
        int digitSum = 0;
        int number = 0;
        for (int i = 0; i < b.toString().length(); i++) {
            String s = b.toString();
            char c = s.charAt(i);
            number = Character.getNumericValue(c);
            digitSum = number + digitSum;
        }
        return digitSum;
    }
    public static void main(String[] args) {
        System.out.println("Ans: " + sumOfDigits(factorial(100)));
    }
    
}
