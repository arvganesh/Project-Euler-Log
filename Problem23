package problem23;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
/**
 *
 * @author arvganesh
 */
public class Problem23 {

    private static int sumOfFactors(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                sum += i;
            }
        }
        return sum;

    }

    private static boolean isAbundantNum(int n) {
        if (sumOfFactors(n) > n) {
            return true;
        }
        return false;
    }
    public static ArrayList getAbunNums() {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i < 28123; i++) {
            if (isAbundantNum(i)) list.add(i);
        }
        return list;
    }
    public static long getAllNums() {
        int sum = 0;
        for (int i = 1; i < 28123; i++) {
            sum = sum + i;
        }
        return sum;
    }
    public static void main(String[] args) {
        long sum = 0;
        HashSet<Long> hs = new HashSet<Long>();
        int listSize = getAbunNums().size();
        for (int i = 1; i < listSize; i++) {
            for (int j = 1; j < listSize; j++) {
                long ij = i+j;
                if (i + j > 28123) {
                    break;
                }
                if (isAbundantNum(i) && isAbundantNum(j)) hs.add(ij);
                
            }
        }
        System.out.println(hs);
        Iterator it;
        it = hs.iterator();
        while (it.hasNext()) {
            sum = sum + (long) it.next();
        }
        System.out.println(sum);

    }

}
