using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWorld
{
public class DecimalToBinaryConverter
{
    public string ConvertToBinary (long decimalNumber) {

        long quotient, remainder;
        string binaryNumberResult = "";
        while (decimalNumber > 0 ) {
            quotient = decimalNumber /2 ; 
            remainder = decimalNumber % 2 ;
            decimalNumber= quotient;
            binaryNumberResult += decimalNumber.ToString();

        }
        return string.Join("", binaryNumberResult.ToCharArray().reve);
    }

}
}