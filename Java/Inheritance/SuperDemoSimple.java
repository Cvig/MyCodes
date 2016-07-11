//Create a superclass
class A
{
	int i;
	A()
	{
		i= 10;
		System.out.println("Inside A Constructor "+i);
		
		
	}
		
	

}

class B extends A
{
	int j;
	B()
	{
		super(); // itwill execute cosntructor of super class first
		j = 20;
		System.out.println("Inside B Constructor "+j);
		
		
	}
	
	
	
}

class SuperDemoSimple
{
	
	public static void main(String args[])
	{
		B ob = new B();
		
		
	}
	
	
}