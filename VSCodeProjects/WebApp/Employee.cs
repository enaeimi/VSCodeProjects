using System.ComponentModel.DataAnnotations;

namespace WebApp
{
    public class Employee
    {
        public long Id { get; set; }
        [Required, StringLength(10)]
        public string Name { get; set; }
        public int Tel { get; set; }
        public string Family { get; set; }
        public long ManagerId { get; set; }
        


        
        
    }
}