class sapos extends Thread{
    String nome;
    int distpercurso,distpercorrida,numsaltos;
    sapos(String nome,int distpercurso){
        this.nome = nome;
        this.distpercurso = distpercurso;
        this.distpercorrida = 0;
        this.numsaltos = 0;
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