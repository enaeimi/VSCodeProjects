using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebApp.Pages
{
    public class IndexModel : PageModel
    { 
        private readonly AppDbContext _db;
        public IndexModel(AppDbContext db)
        {
            _db = db;
        }


        public IList<Customer> Customers {get; private set;}
        public IList<Employee> Employees {get; private set;}
        public void OnGet()
        {

        }
    }
}
