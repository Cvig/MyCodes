//Demostrate method overloading.
class OverloadDemo
{
	void test()
	{
		
		System.out.println("No parameters");
		
		
	}
	//Overload test for two integer parameters.
	void test(int a, int b)
	{
		System.out.println("a and b:" +a + " " +b);
		
		
	}
	//overload test for a double parameters
	double test(double a)
	{
		System.out.println("double a: "+a);
		return a*a;
		
	}

	
}
class Overload
{
	public static void main(String args[])
	{
		
		OverloadDemo ob = new OverloadDemo();
		double result;
		
		//call all versions of test()
		ob.test();
		double j = ob.test(10);
		ob.test(10,20);
		result = ob.test(1.1);
		System.out.println(j + "..Result of ob.test(1.1): "+ result);
		
	}
	
	
}