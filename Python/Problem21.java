/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package amicablenumbers;

import java.util.ArrayList;

/**
 *
 * @author arvganesh
 */
public class AmicableNumbers {
    public static int sumOfFactors(int n) { // Gets Sum of Proper Divisors of n.
        int factor = 0;
        for (int i = 1; i <= Math.ceil(n/2); i++) {
            if (n % i == 0) {
                factor += i;
            }
        }
        return factor;
    }
    public static ArrayList isAmicablePair(int num) { // Return an arraylist of amicable pairs ex: [x,y]
        ArrayList<Integer> list = new ArrayList<>();
        int factorSum = sumOfFactors(num);  
        int sumOfFactorSum = sumOfFactors(factorSum);
        if (num == sumOfFactorSum && sumOfFactorSum != factorSum) {
            // adding both pairs.
            list.add(factorSum);
            list.add(sumOfFactorSum);
        }
        
        return list;
    }
    public static void main(String[] args) {
        int sumOfAmiNum = 0;
        ArrayList<Integer> amiList = new ArrayList<>();
        for (int i = 1; i < 10000; i++) {
           ArrayList<Integer> list = isAmicablePair(i);
           if (!list.isEmpty() && !amiList.contains(i)) {
               // Adds the amicable pair to amiList.
                amiList.addAll(list);
                // list has two values. The amicable pair.
            }
            // removing all elements from the list so that it only adds pair by pair..
            list.clear();
            
       
        }
        // gets sum of all elements in the final list.
        for (int i = 0; i < amiList.size(); i++) {
            int listget = amiList.get(i);
            sumOfAmiNum += listget;        
        }
        System.out.println(sumOfAmiNum);
    }
    
}
