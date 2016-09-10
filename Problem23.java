package problem23;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

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

    public static Set<Integer> getAbunNums() {
        HashSet<Integer> hs = new HashSet<>();
        for (int i = 1; i <= 28123; i++) {
            if (isAbundantNum(i)) {
                hs.add(i);
            }
        }
        return hs;
    }

    public static long getTotalSum() {
        int sum = (28123 * 28124) / 2;
        return sum;
    }

    public static void main(String[] args) {
        long sum = 0;
        HashSet<Long> hs = new HashSet<Long>();
        HashSet<Integer> abunSet = new HashSet<Integer>(getAbunNums());
        int listSize = getAbunNums().size();
        for (int i = 1; i < 28123; i++) {
            for (int j = 1; j < 28123; j++) {
                long ij = i + j;
                if (i + j > 28123) {
                    break;
                }
                if (abunSet.contains(i) && abunSet.contains(j)) {
                    hs.add(ij);
                }

            }
        }
        //System.out.println(hs);

        // Here on is good :D
        Iterator it;
        it = hs.iterator();
        while (it.hasNext()) {
            sum = sum + (long) it.next();
        }

        // What you want
        long ans = getTotalSum() - sum;
        System.out.println(ans);

    }

}
