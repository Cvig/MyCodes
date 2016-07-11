//Using break to exit from nested loops
class BreakLoopWithNestedLoop
{
	public static void main(String args[])
	{
		one: // label can be any block of code and not just a loop.
		for(int i=0;i<3;i++)
		{
			System.out.println("i is: "+i);
			
		}
		System.out.println();
		outer:
		for(int i=0; i<3;i++)
		{
			System.out.print("Pass "+i+":");
			for(int j=0; j<100;j++)
			{
				if(j==10)
					break outer; //exit both loops. Can not break label one here
				System.out.print(j+" ");
				
				
			}
			
		System.out.println("This will not print");
		}
	System.out.println("Loop completes");
	}
	
	
	
}