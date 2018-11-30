public class Person {

	private String firstName;
	private String lastName;
	private String middleName;
	private int personId;
	private int Age;
	private int Tel;

	public Person() {

		this.firstName = null;
		this.lastName = null;
		this.middleName = null;
		this.personId = 0;

	}

	public Person(String firstName, String lastName, String middleName,
			int personId) {

		this.firstName = firstName;
		this.lastName = lastName;
		this.middleName = middleName;
		this.personId = personId;
	}

	public Person(String firstName, String lastName, String middleName,
			int personId, int age, int tel) {

		this.firstName = firstName;
		this.lastName = lastName;
		this.middleName = middleName;
		this.personId = personId;
		this.Age = age;
		this.Tel = tel;
	}

	public String getFirstName() {

		return this.firstName;
	}

	public void setFirstName(String firstName) {

		this.firstName = firstName;
	}

	public String getLastName() {

		return this.lastName;
	}

	public void setLastName(String lastName) {

		this.lastName = lastName;
	}

	public String getMiddleName() {

		return this.middleName;
	}

	public void setMiddleName(String middleName) {

		this.middleName = middleName;
	}

	public int getPersonId() {

		return this.personId;
	}

	public void setPersonId(int personId) {

		this.personId = personId;
	}

	public int getAge() {

		return this.Age;
	}

	public void setAge(int age) {

		this.Age = age;
	}

	public int getTel() {

		return this.Tel;
	}

	public void setTel(int tel) {

		this.Tel = tel;
	}

	public String toString() {

		return this.firstName + " " + this.middleName + " " + this.lastName;
	}
}