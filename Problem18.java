package problem18.triangle;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 *
 * @author arvganesh
 */
public class Problem18Triangle {

    public static void main(String[] args) throws IOException {
        // reading the pyramid from a file
        ArrayList<String> list = new ArrayList<>();
        File file = new File("/home/arvganesh/Desktop/triangle.txt");
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line = null;
            int sum = 0;
            String[] array = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"};

            while ((line = br.readLine()) != null) {
                for (String value : line.split(" ")) {
                    if (!value.equals("")) {

                        list.add(value);

                    }

                }

            }
            System.out.println(list);
        }
    }

}
