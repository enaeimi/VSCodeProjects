using System;
using System.Linq;
using Microsoft.EntityFrameworkCore;

namespace TodoApi.Models
{

    public class MySqlContext : DbContext
    {

        public DbSet<TodoItem> TodoItems { get; set; } //DbSet represents database table

        // public MySqlContext(DbContextOptions<MySqlContext> options) : base(options)
        // {
        // }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
            => optionsBuilder.UseMySQL(connectionString: "@Server=localhost;database=AspNetCore,uid=root");




    }

}