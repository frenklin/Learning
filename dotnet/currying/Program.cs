using System;

namespace currying
{
    class Program
    {
        static void Main(string[] args)
        {
            var rnd = new Random();
            
            var sum55=sum(55);
            var sum33=sum(33);
            Console.WriteLine($"Sum 55+13 = {(sum55(13))}");
            Console.WriteLine($"Sum 33+13 = {(sum33(13))}");
            Console.WriteLine($"Sum 1+2 = {(sum(1)(2))}");
            
            var s2=sum2(()=>55);
            Console.WriteLine($"Sum 55+13 = {(s2(13))}");            

            var sRand=sum2(()=>rnd.Next());
            Console.WriteLine($"Sum rnd+13 = {(sRand(13))}");
        }

        static Func<int,int> sum(int x){
            return y=>y+x;
        }

        static Func<int,int> sum2(Func<int> x){
            return y=>y+x();
        }
    }


    
}
