import java.util.*;
class calculatingcgpa{
public static void main(String[] args){
int math,science,history;
Scanner sc = new Scanner(System.in);
System.out.println("Enter the marks for math: ");
math=sc.nextInt();
System.out.println("Enter the marks for science: ");
science=sc.nextInt();
System.out.println("Enter the marks for history: ");
history=sc.nextInt();
int total=math+science+history;
int cgpa = total/30;
System.out.println("Over all CGPA of given marks is: "+cgpa);
}
}

