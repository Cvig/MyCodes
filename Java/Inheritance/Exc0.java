class Exc0
{
	public static void main(String args[])
	{
		try
		{
			int d = 0;
			int a = 42/d;
			System.out.println("done 1");		
			
			
		}
		catch(Exception e)
		{
			System.out.println("Exception occurred "+e);
			int d = 1;
			int a = 42/d;
			
			
			
		}
		System.out.println("done");
		
		
	}
	
	
	
	
}