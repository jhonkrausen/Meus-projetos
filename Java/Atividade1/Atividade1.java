package Atividade1;
import java.util.Scanner;

public class Atividade1 {
    public static void main(String[] args) {
        
        Scanner entraDados = new Scanner(System.in);
        System.out.println("Quantos metros você quer converter?: ");
        float metros = entraDados.nextFloat();
        float centimetros = metros*100;
        System.out.println(metros + " metros em centímetros é: " + centimetros);
        entraDados.close();
        

    }
}
