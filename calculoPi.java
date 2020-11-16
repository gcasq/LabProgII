//Este exercício calculará o valor de Pi utilizando o recurso de Threads. O principal intuito é a prática da utilização deste recurso.

public class calculoPi {
    public static void main(String[] args) {
        pi impar = new pi(1.0);
        pi par = new pi(2.0);
        impar.start();
        par.start();
    }
}
class pi extends Thread{
    double i;
    static int op=0;
    static double Value=1;
    pi(double num){
        this.i=num;
    }
    public void rest(){
        yield();
    }
    public void showvalue(){
        System.out.println("Pi is equal to "+2.0*Value);
    }
    public void run(){
        while(op<30000){
        double aux = i*2;
        Value = Value * (aux/(aux-1))*(aux/(aux+1));
        i+=2;
        op++;
        rest();
        }
        showvalue();

    }
}
