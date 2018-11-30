import java.lang.reflect.*;
import static java.lang.System.out;

public class TestCatalogue {

	public static void main(String[] args) {

		Catalogue personsCatalogue = new Catalogue();

		personsCatalogue.register(new Person("Ebrahim", "ebi", "Naeimi", 1));
		personsCatalogue.register(new Person("Ali", "AL", "Naeimi", 2));

		System.out.println(personsCatalogue.getPersonCatalogue().get(0)
				.toString());
		System.out.println(personsCatalogue.getPersonCatalogue().get(1)
				.toString());

		// Start of Question 1
		Class c = personsCatalogue.getClass(); // Get the class of the Object
		System.out.println("Class name is:" + c.toString());

		Member[] members = c.getDeclaredMethods(); // Gets the Declared methods
													// in the class
		printMembers(members, "Methods"); // Prints all the declared methods in
											// the class

		try {
			getMethod(members, "register").invoke(personsCatalogue,
					new Person("aaa", "bbbb", "ddddd", 3)); // invoke the method
															// with name
															// 'register'
			System.out.println(personsCatalogue.getPersonCatalogue().get(2)
					.toString()); // verification that the implementation worked

			// test
			Class<?> pClass = Class.forName("Person"); // Get the Person class
			Constructor<?> cPerson = pClass.getConstructor(new Class[] {
					String.class, String.class, String.class, int.class }); // Invoking
																			// the
																			// parameterized
																			// constructor
			Person p_refl = (Person) cPerson.newInstance("test", "test",
					"test", 3); // Creating an instance with parameterized
								// constructor
			System.out.println(p_refl.toString()); // Call to test
			// end of test

		} catch (Exception e) {
			e.printStackTrace();
		}
		// End of Question 1
	}

	// ---------------------------------------------------------------------------
	// getMethod:
	// Searches for a method with the name from the Members list and returns
	// the type casted Method if found. Otherwise, returns null.
	// ---------------------------------------------------------------------------
	private static Method getMethod(Member[] member, String name) {

		Method result = null;
		for (Member method : member) {
			if (method.getName().equals(name) == true) {
				result = (Method) method;
			}
		}

		return result;
	}

	// ---------------------------------------------------------------------------
	// printMembers:
	// Prints the names of all the Methods present in the Members array
	// ---------------------------------------------------------------------------
	private static void printMembers(Member[] mbrs, String s) {
		out.format("%s:%n", s);
		for (Member mbr : mbrs) {
			out.format("  %s%n", ((Method) mbr).toGenericString());
		}
		if (mbrs.length == 0)
			out.format("  -- No %s --%n", s);
		out.format("%n");
	}

}