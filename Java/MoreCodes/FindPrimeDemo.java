//Test for primes.
class FindPrimeDemo
{
	public static void main(String args[])
	
	{
		int num;
		boolean isPrime = true;
		num =13;
		for (int i=2; i<= num/2 ; i++) //check till half, half to start from 2 only
		{
			if((num%i)==0)  //16%3 =1, 16%2=0
			{
				isPrime = false;
				break;
				
			}
		}
			if(isPrime)
				System.out.println(num + " is Prime");
			else
				System.out.println(num + " is Not Prime");
			
			
		}
		
		
		
		
		
		
	}
	
	
	
	
