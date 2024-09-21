import java.util.*;
class kilometertomiles{
public static void main(String[] args){
int kilometer;
Scanner sc = new Scanner(System.in);
System.out.println("Enter the value for kilometer: ");
kilometer=sc.nextInt();
float mile = kilometer*0.6214f;
System.out.println(kilometer+" kilometer is equal to "+mile+" miles");
//System.out.println(kilometer+" kilometer is equal to "+0.6214*kilometer+" miles");
}
} 