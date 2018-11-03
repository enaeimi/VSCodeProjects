using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using Microsoft.EntityFrameworkCore;


namespace Web
{
    public class Startup
    {
    
        public IConfiguration Configuration{get; set;}
        public Startup(IConfiguration config)
        {
            Configuration=config;
            
        } 

        // This method gets called by the runtime. Use this method to add services to the container.
        // For more information on how to configure your application, visit https://go.microsoft.com/fwlink/?LinkID=398940
        //It prepares the environment by adding required services
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<AppDbContext> (options => 
                options.UseInMemoryDatabase("name"));
                

            services.AddMvc();

            
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        //It configures the serivces added in ConfigureServices.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
        {
            
            loggerFactory.AddConsole();

            //if (env.IsDevelopment()) //Commented to show development errors
            {
                app.UseDeveloperExceptionPage();
            }

            

            app.UseMvc();//To use MVC pattern and pages(.cshtml)

            app.Run(async (context) => //Default route 
            {
                await context.Response.WriteAsync("<b>Hello World!!!!!</b>");
            });
        }
    }
}
