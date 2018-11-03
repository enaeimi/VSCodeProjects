using System;
using System.Text;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;


namespace LibraryData.Models
{
    public class Person
    {
        public int Id  {get; set;}
        public string Name  {get; set;}
        public string Family  {get; set;}
        public string Tel  {get; set;}

        //public string Address  {get; set;}
        // public DateTime DateOfBirth  {get; set;}

        //public virtual LibraryCard LibraryCard {get; set; }

    }


}