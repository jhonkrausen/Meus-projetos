package Atividade2;
import java.util.Scanner;


public class Atividade2 {
    public static void main(String[] args) {
        Scanner entraDados = new Scanner(System.in);
        System.out.println("Digite o raio do circulo: ");
        float raio = entraDados.nextFloat();

        double area = Math.PI*(raio*raio);
        System.out.println("A area do circulo é: " + area);
        entraDados.close();
    }
}
