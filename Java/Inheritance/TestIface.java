//complete skeleton and everything is abstract
interface Callback
{
	void callback(int param);
	void test();
	
	
}
//Interfaces are not extended, ther are implemented
class Client implements Callback
{
	public void callback(int p)
	{
		System.out.println("callback called with "+p);
		
		
	}
	//compile time error of I don't implement all the methods of interface class
	//you can either make this class abstracted or atleast write method name
	public void test()
	{
		
	}
	void nonIfaceMeth()
	{
		System.out.println("Classes that implement interfaces " + "may also define other members, too.");
	} 
}

class TestIface
{
	public static void main(String args[])
	{
		Client ob = new Client();
		ob.callback(42);
		
		
	}
	
	
}