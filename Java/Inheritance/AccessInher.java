// Create a superclass
class A
{
	int i; // public by default
	private int j; //private to A
	
	void setij(int x, int y)
	{
	 i = x;
	  j = y;
	}
		
}

//A's j is not accessible here.

class B extends A
{
	int total;
	void sum()
	{
		
		total = i + j ; //ERROR, j is not accessible here
		
	}
	
	
}


class AccessInher
{
	public static void main(String args[])
	{
		B subOb = new B();
		subOb.setij(10,11);
		subOb.sum();
		System.out.println("Sum is: "+ subOb.total);
		
		
	}
	
	
}