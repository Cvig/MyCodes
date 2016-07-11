class StaticDemo
{
	static int a = 42;
	static int b = 99;
	static int c = 19;
	static void callme()
	{
		System.out.println("a = "+a);
		
	} 	
	
	
}

class StaticByName
{
	public static void main(String args[])
	{
		// To call static methods or variables, we 
		// don't need to create an object
		StaticDemo.callme();
		System.out.println("b = " + StaticDemo.b);
		
		
	}
	
	
}