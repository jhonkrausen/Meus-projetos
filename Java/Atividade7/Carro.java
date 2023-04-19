package Atividade7;

    public class Carro {

        private String cor;
        private String modelo;
        private String nome;
        private String marca;

        public Carro(String c, String m, String n, String ma) {

            this.setCor(c);
            this.setModelo(m);
            this.setNome(n);
            this.setMarca(ma);
            
        }

        public void setCor(String c){
            this.cor = c;
        }

        public String getCor() {
            return this.cor;
        }
        
        public void setModelo(String m){
            this.modelo = m;
        }
        
        public String getModelo(){
            return this.modelo;
        }

        public void setNome(String n){
            this.nome = n;
        }

        public String getNome() {
            return this.nome;
        }

        public void setMarca(String ma){
            this.marca = ma;
        }

        public String getMarca() {
            return this.marca;
        }

        public void info(){

            System.out.println("Cor = " + this.getCor());
            System.out.println("Nome = " + this.getNome());
            System.out.println("Marca = " + this.getMarca());
            System.out.println("Modelo = " + this.getModelo());

        }

        
}