using Microsoft.EntityFrameworkCore;

namespace Web
{
    internal class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions options) :base(options)
        {


        }

        public DbSet<Customer> Customers {get; set;}

    }
}