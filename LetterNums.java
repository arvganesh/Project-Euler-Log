/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package letternums;

import java.util.ArrayList;

/**
 *
 * @author arvganesh
 */
public class LetterNums {

    private static String str(int n) {
        //array and variable declaration
        String[] array = new String[100];
        array[1] = "one";
        array[2] = "two";
        array[3] = "three";
        array[4] = "four";
        array[5] = "five";
        array[6] = "six";
        array[7] = "seven";
        array[8] = "eight";
        array[9] = "nine";
        array[10] = "ten";
        array[11] = "eleven";
        array[12] = "twelve";
        array[13] = "thirteen";
        array[14] = "fourteen";
        array[15] = "fifteen";
        array[16] = "sixteen";
        array[17] = "seventeen";
        array[18] = "eighteen";
        array[19] = "nineteen";
        array[20] = "twenty";
        array[30] = "thirty";
        array[40] = "forty";
        array[50] = "fifty";
        array[60] = "sixty";
        array[70] = "seventy";
        array[80] = "eighty";
        array[90] = "ninety";

        String str = String.valueOf(n);
        // declaring all of a
        char a;
        int numValA;
        int numValA2;
        String strA;
        // declaring all of b
        char b;
        int numValB;
        int numValB2;
        String strB;
        // declaring all of c
        char c;
        int numValC;
        String strC;
        

        if (str.length() == 1) {
            // returning the single digit numbers
            return array[n];
        }
        // for two digit numbers
        if (str.length() == 2) {
            a = str.charAt(0);
            numValA = Character.getNumericValue(a);
            strA = array[numValA];
            b = str.charAt(1);
            numValB = Character.getNumericValue(b);
            strB = array[numValB];
            numValB2 = numValB*10;
            numValA2 = numValA*10;
            int numValX = numValA2 + numValB;
            if (n % 10 == 0) {
                return array[numValA2];
            }
            else if (n < 20) {
                return array[n];
            }
            else {
                return array[numValA2] + strB;
            }
        }
        // for 3 digit numbers
        if (str.length() == 3) {
            a = str.charAt(0);
            numValA = Character.getNumericValue(a);
            strA = array[numValA];
            b = str.charAt(1);
            numValB = Character.getNumericValue(b);
            strB = array[numValB];
            numValB2 = numValB*10;
            c = str.charAt(2);
            numValC = Character.getNumericValue(c);
            strC = array[numValC];
            if (n % 100 == 0) {
                return strA + "hundred";
            }
            else if (n % 10 == 0) {
                return strA + "hundredand" + array[numValB2]; 
            }
            else if (b == '0') {
                return strA + "hundredand" + strC;
            }
            else if (b == '1') {
                return strA + "hundredand" + array[numValB2 + numValC];
            }
            else {
                return strA + "hundredand" + array[numValB2] +  strC;
            }
                
        }
        // return 1000
        if (str.length() == 4) {
            return "onethousand";
        }

        return "there was an issue: please debug!";
    }
    // get the sum of a string(str), add the amount of characters to add, after all has been added, return add.
    public static int wordSum(int n) {
        int add = 0;
        int len = 0;
        for (int i = 1; i < n + 1; i++) {
            len = str(i).length();
            add = add + len;
        }
        return add;
    }

    public static void main(String[] args) {
        // for (int i = 1; i < 1001; i++) - for checking if the numbers in the sequence were correct
            System.out.println("Ans: " + wordSum(1000));
        
    }

}
