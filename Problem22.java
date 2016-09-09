/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package problem22;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.TreeSet;

/**
 *
 * @author arvganesh
 */
public class Problem22 {

    public static int getIntPos(String s) {
        char[] ch = s.toCharArray();
        int temp = 0;
        int temp_integer = 0;
        int integerVal = 0;
        for (char c : ch) {
            temp = (int) c;
            temp_integer = 64; //for upper case

            if (temp <= 90 & temp >= 65) {
                integerVal = integerVal + (temp - temp_integer);
            }
        }
        return integerVal;
    }
    /*
    public static class myComp implements Comparator<String> {
        @Override
        public int compare(String str1, String str2) {
            return str1.compareTo(str2);
        }
    }
    */
    public static ArrayList nameToInt(TreeSet ts) {
        ArrayList<Integer> list = new ArrayList<>();
        Iterator iterator;
        iterator = ts.iterator();
        while (iterator.hasNext()) {
            list.add(getIntPos(iterator.next().toString()));
        }
        return list;
    }
    public static int sumOfIndexM(ArrayList list) {
        int sum = 0;
        for (int i = 0; i < list.size(); i++) {
            int letterNum = (int) list.get(i);
            sum = sum + (letterNum*(i+1));
            
        }
        return sum;
    }
    public static void main(String[] args) {
        String fileName = "/home/aganesh/Documents/Java/File Reading/names.txt";

		try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {

			String line;
                        TreeSet<String> ts = new TreeSet<String>();
			while ((line = br.readLine()) != null) {
			     String[] strAdd = line.split("\",\"");
                             for (int i = 0; i < strAdd.length; i++) {
                                 ts.add(strAdd[i]);
                             }
                             
                                     
			}
                        ArrayList<Integer> intList = new ArrayList<>(nameToInt(ts));
                        System.out.println(sumOfIndexM(intList));
                        
		} catch (IOException e) {
			e.printStackTrace();
		}

	}
    }


