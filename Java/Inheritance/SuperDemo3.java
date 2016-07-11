//Using super to overcome name hiding
class A
{
	int a;
}
class B extends A
{
	
	int b; 
	B(int a, int b)
	{
		
		super.a = a; 
		this.b = b;
		
	}
	
	
}

class C extends B
{
	int c;
	C(int a, int b, int c)
	{
		//can't write just super() here bcoz there is no
		//constructor with zero arguments here.
		super(a,b);
		this.c =c;
		
	}
	
	
}

class SuperDemo3{
	
	
	
	public static void main(String args[])
	{
		//input
		C ob = new C(1,2,3);
		System.out.println(ob.a + " " + ob.b + " " +ob.c);
		
		
	}
}