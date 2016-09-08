/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package numberofsundays;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.YearMonth;
import java.time.format.DateTimeFormatter;
import java.time.format.TextStyle;
import java.util.Locale;

/**
 *
 * @author arvin_000
 */
public class NumberofSundays {

    public static String getDate(Integer day, Integer month, Integer year) {

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d/M/yyyy");
        LocalDate date = LocalDate.parse(day + "/" + month + "/" + year, formatter); // LocalDate = 2010-02-23
        DayOfWeek dow = date.getDayOfWeek();  // Extracts a `DayOfWeek` enum object.
        String output = dow.getDisplayName(TextStyle.SHORT, Locale.US); // String = Tue
        return output;
    }

    public static int getSundays() {
        int count = 0;
        for (int y = 1901; y < 2001; y++) {
            for (int m = 1; m < 13; m++) {
                YearMonth yearMonthObject = YearMonth.of(y, m);
                int daysInMonth = yearMonthObject.lengthOfMonth();
                for (int d = 1; d <= daysInMonth; d++) {
                    if (getDate(d, m, y).equals("Sun")) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(getSundays());
    }

}
