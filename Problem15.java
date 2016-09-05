/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lattice.paths;

import java.math.BigInteger;

/**
 *
 * @author arvganesh
 */
public class LatticePaths {

   
     public static BigInteger factorial(long n) {
       BigInteger fact = new BigInteger("1");
       for (int i = 1; i <= n; i++) {
           fact = fact.multiply(new BigInteger(i + ""));
       }
       return fact;
   }
    private static BigInteger findPath(long m, long n) {
        long number = m+n;
        long number2 = (m+n)-n;
        BigInteger p = factorial(n).multiply(factorial(number2));
        BigInteger num = factorial(number).divide(p);
        BigInteger two = BigInteger.valueOf(2);
        return num;
    }

    public static void main(String[] args) {
        System.out.println(findPath(20,20));
    }

}
