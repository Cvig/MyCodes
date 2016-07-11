//Using continue with a label
class ContinueLabelDemo
{
	public static void main(String args[])
	{
		outer: for(int i=0; i<3; i++)
		{
			for(int j=0;j<10;j++)
			{
				System.out.println("I is :"+i+"j is :"+j);
				//System.out.print(""+(i*j));
				if(j>i)
				{
					System.out.println();
					continue outer;
					
					
				}
				
				
			}
			
		System.out.println();
		}
		
		
		
	}
	
	
	
	
	
}