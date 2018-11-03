using System;

namespace TestConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            var result = AddInt(3,4);

            Console.WriteLine("Result: " + result);
            Console.Read();
        }
        public static int AddInt(int a , int b)
        {
            return a+b;
        }
    }
}
