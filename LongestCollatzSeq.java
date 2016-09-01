/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package longestcollatzseq;

import java.util.ArrayList;

/**
 *
 * @author arvganesh
 */
public class LongestCollatzSeq {

    public static int collatzNum(long n) {
        int count = 0;
        while (true) {
            if (n % 2 == 0) {
                n = n / 2;
                count++;
                //System.out.println("n: " + n);
            } else {
                n = (3 * n) + 1;
                count++;
                //System.out.println("n: " + n);
            }
            if (n == 1) {
                count++;
                break;
            }

        }
        return count;

    }

    public static void main(String[] args) {
        int largeLength = 0;
        int largeI = 0;
        int tempLen = 0;
        int i = 0;
        for (i = 999168; i >= 1; i --) {

            tempLen = collatzNum(i);
            //System.out.println("TL: " + tempLen + " I: " + i);
            if (tempLen > largeLength) {
                largeLength = tempLen;
                largeI = i;
                
            }
            
            
           

        }
        System.out.println("The Length for " + largeI +" is " + largeLength);

    }

}
