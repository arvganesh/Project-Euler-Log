/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package problem.pkg16;

import java.math.BigInteger;

/**
 *
 * @author arvganesh
 */
public class Problem16 {

    public static String twoToThe(long n) {
        BigInteger square = new BigInteger("1");
        for  (int i = 1; i <= n; i++) {
            square = square.multiply(new BigInteger(2 + ""));
        }
        return square.toString();
    }
    public static long getDigitsSum(String s) {
        long sum = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int total = Character.getNumericValue(c);
            sum = sum + total;
        }
        return sum;
    }
    public static void main(String[] args) {
        System.out.println("Answer: " + getDigitsSum(twoToThe(1000)));
    }
    
}
