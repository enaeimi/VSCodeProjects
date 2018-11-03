using System;
using LibraryData.Models;
using Microsoft.EntityFrameworkCore;


namespace LibraryData
{
    public class LibraryContext : DbContext
    {
        public LibraryContext(DbContextOptions optiopns) : base(optiopns) { }

        public DbSet<Employee> Employees {get; set;} 
        public DbSet<Person> Persons {get; set;} 
        
    }
}
