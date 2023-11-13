import java.util.Scanner;

public class KonversiSuhu {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("## Program Java Konversi Suhu ##");
        System.out.println("================================");

        double celcius, fahrenheit, kelvin, reamur;

        System.out.println("Masukkan suhu Celsius = ");
        celcius = input.nextDouble();
        System.out.println("==================================");

        fahrenheit = (9.0/5.0 * celcius) + 32;
        kelvin = celcius + 273.15;
        reamur = celcius * (4.0/5.0);

        System.out.println(celcius+"derajat Celcius = "+fahrenheit+" derajat Fahrenheit");
    }
}
