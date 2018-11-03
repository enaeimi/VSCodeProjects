using System.ComponentModel.DataAnnotations;

namespace WebApp
{
    public class Customer
    {
        public long Id { get; set; }
        [Required, StringLength(10)]
        public string Name { get; set; }
        


        
        
    }
}