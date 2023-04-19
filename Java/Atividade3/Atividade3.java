package Atividade3;
import java.util.Scanner;
public class Atividade3 {
    public static void main(String[] args) {
        Scanner entraDados = new Scanner(System.in);
        System.out.println("Digite a medida do lado do seu quadrado em cm: ");
        int lado = entraDados.nextInt();
        int area = lado*lado;
        System.out.println("A area do seu quadrado é: " + area);
        entraDados.close();
    }
}
