//Create a superclass.
class A
{
	int i; //public by default
	private int j; // private to ARG_IN
	int getJ()
	{
		return j;
	}
	void setJ(int a)
	{
		j =a;
		
	}
	void setij(int x, int y)
	{
		i = x;
		j = y;
		
	}
	
	
	
} 
//A's j is not accessible from here.
class B extends A
{
	int total;
	int j = getJ();
	void sum()
	{
		total = i+j; //ERROR, j is not accessible here
		
		
	}
	
	
	
}

class AccessInher
{
	public static void main(String args[])
	{
		B subOb = new B();
		subOb.setij(10,12);
		subOb.setJ(12);
		subOb.sum();
		System.out.println("Total is "+ subOb.total);
		
		
	}
	
	
}