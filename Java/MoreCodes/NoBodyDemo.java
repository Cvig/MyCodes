//The target of a loop can be empty

class NoBodyDemo
{
	public static void main(String args[])
	{
		int i,j;
		i = 100;
		j = 300;
		//mid-point
		while(++i<--j); //no body in this loop 
		System.out.println("Mid-point is"+i);
		
		
	}
	
	
	
	
}