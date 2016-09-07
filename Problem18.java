package problem18.triangle;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 *
 * @author arvganesh
 */
public class problem18 {

    public static Integer getMax(int n, int m) {
        if (m > n) {
            return m;
        }
        return n;
    }

    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList> arrList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("/home/arvganesh/Desktop/triangle.txt"))) {

            String line;

            while ((line = br.readLine()) != null) {
                ArrayList<Integer> intList = new ArrayList<>();
                if (!line.equals("")) {
                    for (String value : line.split(" ")) {
                        intList.add(Integer.valueOf(value));
                    }

                }
                arrList.add(intList);
            }
            //System.out.println(arrList);
            int arrIndexLength = 0;
            int ans = 0;

            int sumOfNumbers = 0;

            for (int i = arrList.size() - 1; i >= 1; i--) {
                ArrayList<Integer> tempStorage = new ArrayList<Integer>();
                for (int x = 0; x < arrList.get(i).size() - 1; x++) {
                    int num1 = (int) arrList.get(i).get(x);
                    int num2 = (int) arrList.get(i).get(x + 1);
                    int num3 = (int) arrList.get(i - 1).get(x);

                    if (num1 > num2) {
                        sumOfNumbers = num1 + num3;
                        tempStorage.add(sumOfNumbers);
                    } else {
                        sumOfNumbers = num2 + num3;
                        tempStorage.add(sumOfNumbers);
                    }
                    if (arrList.size() == 1) {
                        arrList.get(0).set(0, (int) arrList.get(0).get(0) + getMax((int) arrList.get(1).get(0), (int) arrList.get(1).get(1)));
                        arrList.remove(1);
                    }

                }

                arrList.remove(i);
                arrList.remove(i - 1);
                arrList.add(tempStorage);
                
            }

        }

        System.out.println(arrList.get(0).get(0));
    }

}
