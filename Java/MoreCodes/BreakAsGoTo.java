//Using break as a civilized form of goto.
class BreakAsGoTo
{
	public static void main(String args[])
	{
		boolean t = true;
	first:
	{
		second:
		{
			third:
			{
				System.out.println("Before the break");
				if(t)
					break third;
				System.out.println("This won't execute");
				
			}
			System.out.println("This is after third block");
		}
		System.out.println("This is after second block");
			
		}
		
		
		
		
	}	
}
		
		
		
	
	
	
	
	
	
