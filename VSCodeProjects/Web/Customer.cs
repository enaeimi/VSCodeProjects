using System.ComponentModel.DataAnnotations;

namespace Web
{
    public class Customer
    {
        public int Id { get; set; }
        [Required, StringLength(10)]
        public string Name { get; set; }
        public string Email { get; set; }


        
        



    }
}