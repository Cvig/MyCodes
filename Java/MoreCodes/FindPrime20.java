//This program prints whether 0-20 numbers are prime or not line by line
import java.lang.Math;

class FindPrime20
{
		public static void main(String args[])
		{
			boolean isPrime;
			for(int i=0; i<=20;i++)
			{
				isPrime = true;
				for(int j=2;j<=Math.sqrt(i);j++)  // can only check upto sqrt of that number to check if it's prime or not
				{
					if(i%j==0) 
					{
						isPrime = false;
						break;
					}
					
				}
				if(isPrime && i>1) System.out.println(i+" is Prime"); // any number less than 2 is not prime
				else System.out.println(i+ " is not Prime");
			}
			

			
		}
	
} 