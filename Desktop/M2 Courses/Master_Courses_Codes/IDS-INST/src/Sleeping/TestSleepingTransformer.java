package Sleeping;

public class TestSleepingTransformer {
	public static void main(String[] args) {
		System.out.println("Program started...");
		Sleeping ist = new Sleeping();
		//SleepingClassTransformer sct = new SleepingClassTransformer();
		try {
			ist.randomSleep();
			System.out.println("Calling sum...");
			System.out.println(ist.sum(3, 3));
		} 
		catch (Exception e) {
			e.printStackTrace();
		}
	}
}
