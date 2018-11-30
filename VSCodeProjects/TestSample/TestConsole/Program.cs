using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

namespace TestConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            // var result = AddInt(3,4);
            // Console.WriteLine("Result: " + result);



            string intext = Console.ReadLine();
            int i=0;
            intext[0] = char.ToUpper(intext[0]);
            i++;

            while (true) { 
                if(!Char.IsLetter(intext[i]))
                {
                    for (int j = intext.length; j > intext[i+1]; j--){
                        intext[j]= intext[j-1];
                    }
                    intext[i+1] = " ";
                }

                i++;

                    


            }

            Console.writleLine("Final String is: " + intext);



        }
        public static int AddInt(int a , int b)
        {
            return a+b;
        }
    }
}
