class Emp
{
    int eId; //employee ID
    String eName; //employee name
   //return type name of method(arguments)
     void displayDetails()
     {
       System.out.println("Emp Details are: Emp id is : "+eId+"Emp name is "+eName);
     }

}
class EmpMain
{
   public static void main(String args[])
   {
       //classname objectname = new classname()
       //object of class Employee
       Emp obj = new Emp();
       int a;
       // objectname.varname is the syntax to use variable of object of type class
       Emp obj1 = new Emp();
       obj1.eId = 2;
       obj1.eName = "xyz";
       a = 10;
       obj.eId = 1;
       obj.eName = "Chetna";
       obj.displayDetails();
       obj1.displayDetails();
       System.out.println("Values are "+a+" "+obj.eId+" "+obj.eName);
      System.out.println("Values are "+a+" "+obj1.eId+" "+obj1.eName);
   
   
   }


}
