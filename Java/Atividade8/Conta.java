package Atividade8;

public class Conta {
    
    private String dono;
    private String tipo;
    private double saldo;
    private int numConta;
    private boolean status;

    public Conta(){
        this.saldo = 0;
        this.status = false;
    }

    public void abrirConta(String d, String t, int n){
        this.setDono(d);
        this.setTipo(t);
        this.setNumConta(n);
        this.setStatus(true);
    }

    public void fecharConta(){
        this.setDono(null);
        this.setSaldo(0);
        this.setNumConta(0);
        this.setTipo(null);
        this.setStatus(false);
    }

    public void depositar(double m){
        this.setSaldo(this.saldo + m);
    }

    public void sacar(double m){
        this.setSaldo(this.saldo - m);
    }

    public void setDono(String d){
        this.dono = d;
    }

    public String getDono(){
        return this.dono;
    }

    public void setTipo(String t){
        this.tipo = t;
    }

    public String getTipo(){
        return this.tipo;
    }

    public void setSaldo(double s){
        this.saldo = s;
    }

    public double getSaldo(){
        return this.saldo;
    }
    
    public void setNumConta(int n){
        this.numConta = n;
    }

    public int getNumConta(){
        return this.numConta;
    }

    public void setStatus(boolean st){
        this.status = st;
    }

    public boolean getStatus(){
        return this.status;
    }

    public void info(){
        System.out.println("--------------------------------");
        System.out.println("NOME: " + this.getDono());
        System.out.println("NUMERO: " + this.getNumConta());
        System.out.println("TIPO: " + this.getTipo());
        if(getSaldo() == 0){
            System.out.println("SALDO: R$" + Cores.Vermelho + this.getSaldo() + Cores.Cor);
        }else{
            System.out.println("SALDO: R$" + Cores.Verde + this.getSaldo() + Cores.Cor);
        }
        System.out.println("--------------------------------");
    }
}
