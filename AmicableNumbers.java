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
    public static int sumOfFactors(int n) {
        int factor = 0;
        for (int i = 1; i <= Math.ceil(n/2); i++) {
            if (n % i == 0) {
                factor += i;
            }
        }
        return factor;
    }
    public static ArrayList isAmicablePair(int num) {
        ArrayList<Integer> list = new ArrayList<>();
        int factorSum = sumOfFactors(num);  
        int sumOfFactorSum = sumOfFactors(factorSum);        
        if (num == sumOfFactorSum && sumOfFactorSum != factorSum) {
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
                amiList.addAll(list);
                // list has two values. The amicable pair.
            }
            list.clear();
            
       
        }
        for (int i = 0; i < amiList.size(); i++) {
            int listget = amiList.get(i);
            sumOfAmiNum += listget;        
        }
        System.out.println(sumOfAmiNum);
    }
    
}
