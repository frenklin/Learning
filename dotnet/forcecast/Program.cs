using System;
using System.Linq;
using System.Runtime.InteropServices;
using System.Collections;
using System.Net.Http.Headers;

namespace forcecast
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 10;
            var z = __makeref(i);
            var x = __reftype(z);
            var v = __refvalue(z, int);

            var b = Cast.ForceCast<A, B>(new A());
            var a = new ArrayInitializer(){1,2,3};
            var c = new IndexInitializer(){["a"] = 1, ["b"] = 2};
            Console.WriteLine("Hello World!");
        }

        static void ArgList(__arglist)
        {
            var args = new ArgIterator(__arglist);
            var @ref = args.GetNextArg();
        }
    }

    class A { public int a; }
    class B { public int b; }

    public class Cast
    {

        public static unsafe TOut ForceCast<TIn, TOut>(TIn input)
            where TIn: class
            where TOut: class
        {
            var p = new PinObj<TIn>() {TObj = input };
            var handle = __makeref(input);
            TOut obj = default(TOut);

            fixed (void* pin = &p.Pin)
            {
                TypedReference tr = __makeref(obj);
                *(IntPtr*)(&tr) = *(IntPtr*)(&handle);
                return __refvalue(tr, TOut);
            }
        }
    }

    public class ArrayInitializer : IEnumerable
    {
        public void Add(int a){ }
        public IEnumerator GetEnumerator(){ return null; }
    }

    public class IndexInitializer
    {
        public object this[string key]
        {
            get{ return null;}
            set{ }
        }
    }

}
