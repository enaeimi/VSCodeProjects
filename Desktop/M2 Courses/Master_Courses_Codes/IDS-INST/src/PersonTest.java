public class PersonTest {
	
	
	public String FirstName;
	public String LastName;
	public int Age;
	
	public PersonTest(String fname,String lname,int age) {
		FirstName = fname;
		LastName = lname;
		Age= age;
	}
	public void Register(String s) {
	
}

	public void Update(String s) {

}

	public void Delete(String s) {

}

	public void Print() {	
		System.out.format("Firstname is : %s \n" , FirstName);
		System.out.format("Lastname is : %s \n" , LastName);
		System.out.format("Age is : %d \n", Age);
	
	} 
	

public static void main(String [] args){
	
	PersonTest p = new PersonTest("AAA","BBB",20);
	
	p.Print();
	
	//System.out.format("class Name is : %s", p.getClass());
	Class refPerson= p.getClass();
	for (int i = 0; i < args.length; i++) {
		System.out.format(String.valueOf((refPerson.getFields()[i])));
	}
	
	
	

}
}