//Este exercício calculará o valor de Pi utilizando o recurso de Threads. O principal intuito é a prática da utilização deste recurso.

public class calculoPi {
    public static void main(String[] args) {
        pi impar = new pi(1);
        pi par = new pi(2);
    }
}

class pi extends Thread{
    int i;
    static int op=0;
    static double Value=0;
    pi(int num){
        this.i=num;
    }
    public void rest(){
        yield();
    }
    public void run(){
        int aux = i*2;
        Value+=(aux/aux-1)*(aux/aux+1);
        i++;
        rest();
    }
}
