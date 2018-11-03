using System;
using System.Data.SqlClient;


namespace sqlConsoleProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var client = new SqlConnection(""))
            {
                client.Open();
                SqlCommand command = new SqlCommand("Select count(*) from Employee",client);
                var count = command.ExecuteNonQuery();
                Console.WriteLine("Tne number of records is:" + count);
                
            }

            Console.WriteLine("Hello World!");
            
        }
    }
}
