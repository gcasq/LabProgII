import java.lang.Math;

class sapos extends Thread{
    String nome;
    int distpercurso,distpercorrida,numsaltos,saltomax;
    sapos(String nome,int distpercurso){
        this.nome = nome;
        this.distpercurso = distpercurso;
        this.distpercorrida = 0;
        this.numsaltos = 0;
        this.saltomax = 30;
    }
    void show(int aux){
        System.out.println("O "+nome+" pulou "+aux+" casas    Percorreu "+distpercorrida);
    }
    void jump(){
        int aux = (int) Math.random()*saltomax;
        distpercorrida+=aux;
        show(aux);
    }
    

}

class CorridaDeSapos {


    public static void main(String[] args) {
        final int numsapos = 5;
        final int distpercurso = 500;
        sapos[] s = new sapos[numsapos];
        for (int i=0;i<s.length;i++){
            s[i] = new sapos("Sapo "+i,distpercurso);
        }


    }


}