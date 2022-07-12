import java.util.Arrays;
public class Prueba{
    

public static double sum(double[] numbers) {
        // double sum =0;
        // for(double x: numbers){
        //   sum+=x;
        // }
        //   return sum;
        return Arrays.stream(numbers).sum();
        
      }
    

      public static int summation(int n){
        return n == 1 ? 1 : n + summation(n-1);
        // return n*(n+1)/2;
      }


  public static void main(String[] args) {
      double [] valores = {2,5.3,-9,5.7,8.4,-2.3};
      System.out.println(sum(valores));
      System.out.println(summation(13));
      
  }
}
