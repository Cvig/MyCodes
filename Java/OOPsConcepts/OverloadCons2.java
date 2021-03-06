//Here Box allows one object to initialize another.

class Box
{
    double width;
	double height;
	double depth;
	
	//constructor clone of an object
	Box(Box ob)
	{
		//pass object to constructor
		width = ob.width;
		height = ob.height;
		depth = ob.depth;
		
		
	}
	
	//constructor used when all dimension specified
	Box(double w, double h, double d)
	{
		width = w;
		height = h;
		depth = d;
		
	}
	
	//constructor when no dimesnions specified
	Box()
	{
		width = -1; //use -1 to indicate an uninitialized box
		height = -1;
		depth = -1;
		
		
	}
	
	//constructor used when cube is created
	Box(double len)
	{
		
		width = height = depth = len;
		
	}

    //compute and return volume
	double volume()
	{
		
		return width*height*depth;
		
	}
}

class OverloadCons2
{
	public static void main(String args[])
	{
		//create boxes using the various constructors
		
		Box mybox1 = new Box(10,20,15);
		Box mybox2 = new Box();
		Box mycube = new Box(7);
		Box myclone = new Box(mybox1);
		
		double vol;
		//get volume of first box
		vol = mybox1.volume();
		System.out.println("Volume of mybox1 is "+vol);
		//get volume of second box
		vol = mybox2.volume();
		System.out.println("Volume of mybox2 is "+vol);
		//get volume of cube
		vol = mycube.volume();
		System.out.println("Volume of my cube is "+vol);
		vol = myclone.volume();
		System.out.println("Volume of myclone is "+vol);
	}
	
	
}