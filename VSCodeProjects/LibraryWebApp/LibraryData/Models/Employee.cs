using System;
using System.Text;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;


namespace LibraryData.Models
{
    public class Employee
    {
        public int EmployeeId  {get; set;}
        public string Name  {get; set;}
        public string Family  {get; set;}
        public string Tel  {get; set;}
        //public string Address  {get; set;}
        public int ManagerId  {get; set;}

        // public DateTime DateOfBirth  {get; set;}
        //public virtual LibraryCard LibraryCard {get; set; }

    }


}