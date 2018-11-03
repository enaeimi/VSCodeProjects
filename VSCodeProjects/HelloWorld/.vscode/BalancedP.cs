using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWorld
{
    public class BalancedP
    {

        public bool Matchbr(string brString)
        {

            if (brString.Length > 2)
            {
                return Matchbr(brString.Substring(1, brString.Length - 1));
            }
            else
            {
                if (brString[0] == brString[brString.Length - 1])
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }

        }

    }
}