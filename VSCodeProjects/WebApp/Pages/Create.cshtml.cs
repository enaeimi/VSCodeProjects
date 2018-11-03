using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace WebApp.Pages
{
    public class CreateModel : PageModel
    {
        private readonly AppDbContext _db;
        public CreateModel(AppDbContext db)
        {
            _db = db;
        }
        [BindProperty]
        public Customer Customer{get; set;}
        public async Task<IActionResult> OnPostaAsynch()
        {
              if (!ModelState.IsValid) {
                  return Page();
                }
              
                _db.Customers.Add(Customer);
                await _db.SaveChangesAsync();
              

                return RedirectToPage("/");
        }
        public void onGet()
        {

        }
    }
}