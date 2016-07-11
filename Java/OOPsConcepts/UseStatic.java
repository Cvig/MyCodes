//Demostrate static variables, methods, and blocks
/*
What is a static?
Does not have separate memory reference
It can be directly exceuted
Main method is always static even if there is no 
object on which main method is called
static is like a global variable...only one occurence.
New memory is not allocated to static variable.
Types: static variable, static method, static block
*/
class UseStatic
{
	static int a =3;
	static int b;
	int k;
	static void meth(int x)
	{
		System.out.println("x = "+x);
		System.out.println("a = "+a);
		System.out.println("b = "+b);
		
		
	}
	static 
	{
		System.out.println("Static block initialized."+a);
		b = a*4;
		
		
	}
	public static void main(String args[])
	{
	    System.out.println("main started");
		meth(42);		
			
			
	}
}