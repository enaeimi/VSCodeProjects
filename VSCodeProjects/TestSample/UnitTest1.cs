using NUnit.Framework;
using TestConsole;

namespace Tests
{
    [TestFixture]
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        // [Test]
        // public void Test1()
        // {
        //     Assert.Pass();
        // }


        [TestCase(2,4,6)]
        [TestCase(2,2,4)]
        [TestCase(10,-2,8)]
        public void Should_Return_Sum_Given_Ints(int x, int y, int z)
        {
            var result = Program.AddInt(x,y);
            Assert.AreEqual(z, result);
        }
    
        
    }
}