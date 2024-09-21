import java.util.*;
class calculater
{

public static void main(String[] args)
{
System.out.println("");
System.out.println("This is a calculater design by Yashwanth....");
System.out.println("");
Scanner sc = new Scanner(System.in);
while(true)
{
System.out.println("");
System.out.println(" For Addition press 1");
System.out.println(" For Substraction press 2");
System.out.println(" For Multiplication press 3");
System.out.println(" For Division press 4");
System.out.println(" For Quit press 5");

System.out.printf("Enter your operation number : ");
int operation = sc.nextInt();

if(operation == 5)
{
System.out.println("Thank You See You Again....");
break;
}

System.out.printf("Enter your first number :  ");
double a = sc.nextDouble();
System.out.printf("Enter your second number :  ");
double b = sc.nextDouble();

switch(operation)
{
case 1 :
System.out.printf("Addition of %.2f and %.2f is = %.2f \n",a,b,a+b); 
break;
case 2 :
System.out.printf("Substraction of %.2f and %.2f is = %.2f \n",a,b,a-b);
break;
case 3 :
System.out.printf("Multiplication of %.2f and %.2f is = %.2f \n",a,b,a*b);
break;
case 4 :
if(a!=0){
System.out.printf("Division of %.2f and %.2f is = %.2f \n",a,b,a/b);
}
else{
System.out.println("Can't Divide by Zero....\n");
}
break;
default : 
System.out.printf("Please enter valid number...\n");
break;
}
}
//System.out.printf("Your entered number is %d",a);
}
}