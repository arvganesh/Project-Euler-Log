package problem26;

import java.math.BigInteger;

/**
 *
 * @author arvganesh
 */
public class Problem26 {

    private static int gcd(int a, int b) {
        BigInteger b1 = BigInteger.valueOf(a);
        BigInteger b2 = BigInteger.valueOf(b);
        BigInteger gcd = b1.gcd(b2);
        return gcd.intValue();
    }

    public static int multiplicativeOrder(int n, int a) {
        int k = 1;
        if (gcd(n, a) != 1) {
            return 0;
        } else {

            while (Math.pow(a, k) % n != 1) {
                k += 1;
            }
            return k;
        }
        
    }

    public static void main(String[] args) {
        int greatestLen = 0;
        int greatestNum = 0;
        for (int d = 1000; d > 1; d--) {
            int currentLen = multiplicativeOrder(d, 10);
            if (currentLen > greatestLen) {
                greatestLen = currentLen;
                greatestNum = d;
            }
            if (greatestLen > d - 1) {
                break;
            }
        }
        System.out.println(greatestNum);
    }

}
