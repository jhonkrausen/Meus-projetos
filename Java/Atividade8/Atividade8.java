package Atividade8;
import java.util.Scanner;


public class Atividade8 {


    public static void main(String[] args) {
        
        System.out.println("BEM VINDO!");
        boolean loop = true;
        while (loop == true){
            options();
        }
    }
    public static Contas conta = new Contas();
    public static Scanner entraDados = new Scanner(System.in);
    public static void options(){
        
        System.out.println("-------------------------");
        System.out.println("OPÇÕES: ");
        System.out.println("1 - ABRIR CONTA");
        System.out.println("2 - FECHAR CONTA");
        System.out.println("3 - DEPOSITAR");
        System.out.println("4 - SACAR");
        System.out.println("5 - VERIFICAR SALDO");
        System.out.println("6 - INFORMAÇÕES DA CONTA");
        System.out.println("-------------------------");

        String option = entraDados.nextLine();

        if(option == "1"){
            System.out.print("Digite o seu nome: ");
            String d = entraDados.next();
            System.out.print("Digite o tipo da conta(CC ou CP): ");
            String t = entraDados.next();
            System.out.print("Digite o número da sua conta: ");
            int n = entraDados.nextInt();
            conta.abrirConta(d,t,n);
            System.out.println("Conta criada com sucesso!");
        }
        else if(option == "2"){
            if(conta.getStatus() == true) {
                if (conta.getSaldo() > 0){
                    System.out.println("Saldo positivo! não pode fechar a conta.");
                }
                else if (conta.getSaldo() < 0){
                    System.out.println("Saldo negativo! não pode fechar a conta.");
                }
                else{
                    conta.fecharConta();
                    System.out.println("Conta fechada com sucesso!");
                }
            }
            else{
                System.out.println("Você ainda não tem uma conta!");
            }
        }
        else if(option == "3"){
            if(conta.getStatus() == true){
                System.out.print("Quanto você quer depositar?: ");
                double m = entraDados.nextInt();
                System.out.println("Você tem certeza?");
                System.out.println("1 - SIM");
                System.out.println("2 - NÃO");
                option = entraDados.nextLine();
                if (option == "1"){
                    conta.depositar(m);
                    System.out.println("Você depositou " + m + " com sucesso!");
                    option = null;
                }
                else if(option == "2"){
                    System.out.println("Obrigado!");
                    option = null;
                }
            }
            else{
                System.out.println("Você ainda não tem uma conta!");
            }
        }
        else if(option == "4"){
            if(conta.getStatus() == true){
                System.out.print("Quanto você quer sacar?: ");
                double m = entraDados.nextInt();
                System.out.println("Você tem certeza?");
                System.out.println("1 - SIM");
                System.out.println("2 - NÃO");
                option = entraDados.nextLine();
                if (option == "1"){
                    if(conta.getSaldo() >= m){
                        conta.sacar(m);
                        System.out.println("Você sacou " + m + " com sucesso!");
                        option = null;
                    }
                    else{
                        System.out.println("Saldo insuficiente!");
                    }
                }
                else if(option == "2"){
                    System.out.println("Obrigado!");
                    option = null;
                }
            }
            else{
                System.out.println("Você ainda não tem uma conta!");
            }
        }
        else if(option == "5"){
            if(conta.getStatus() == true){
                System.out.println("Seu saldo é: " + conta.getSaldo());
            }
            else{
                System.out.println("Você ainda não tem uma conta!");
            }
        }
        else if(option == "6"){
            if(conta.getStatus() == true){
                conta.info();
            }
            else{
                System.out.println("Você ainda não tem uma conta!");
            }
        }
        entraDados.close();
    }

}   

