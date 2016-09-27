package pkg1000.fib.num;

import java.math.BigInteger;

/**
 *
 * @author arvganesh
 */
public class FibNum {

    public static String fibonnaciNum(long n) { // Gets nth Fibonnaci Number.
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        BigInteger temp = a.add(b);
        
        for (int i = 0; i < n; i++) {
            temp = a.add(b);
            b = a;
            a = temp;
            
            
        }
        String x = temp.toString();
        return x;
        // Sequence Starts like 1,1,2,3,5,8 etc.
    }
    public static void main(String[] args) {
        long count = 1000; // I checked before, its ~ 200 digit Fibonacci Number.
        while (true) {
            if (fibonnaciNum(count).length() == 1000) { // Checking the amount of digits in the fibonnaci number.
                System.out.println(count);
                break;
            }
            else count++;
        }
        
    }
    
}
