package Atividade4;

import java.util.Scanner;

public class Atividade4 {
    public static void main(String[] args) {
        
        Scanner entraDados = new Scanner(System.in);
        System.out.println("Digite os graus em Fahrenheit: ");
        float grausF = entraDados.nextInt();

        float grausC = ((grausF-32)*5/9);

        System.out.println(grausF + " em graus celcius é " + grausC);
        entraDados.close();

    }
}
