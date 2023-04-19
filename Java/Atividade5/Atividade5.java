package Atividade5;

import java.util.Scanner;

public class Atividade5 {
    public static void main(String[] args) {
        
        Scanner entraDados = new Scanner(System.in);
        System.out.println("Digite os graus em celcius: ");
        int grausC = entraDados.nextInt();

        int grausF = (grausC*(9/5)) + 32;

        System.out.println(grausC + " em graus fahrenheit é " + grausF);
        entraDados.close();
    }
}
