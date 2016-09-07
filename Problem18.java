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
            int arrIndexLength = arrList.size() - 1;
            int ans = 0;

            while (arrList.size() != 1) {

                int sumOfNumbers = 0;
                ArrayList<Integer> tempStorage = new ArrayList<Integer>();
                for (int i = arrIndexLength; i > 0; i--) {
                    for (int x = 0; x < (arrList.get(i).size()); x++) {
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

                    }
                    if (i == 1) {
                        arrList.remove(i);
                        arrList.remove(i - 1);
                        arrList.add(tempStorage);
                    }
                    

                }

            }

        }

        System.out.println(arrList);
    }

}
