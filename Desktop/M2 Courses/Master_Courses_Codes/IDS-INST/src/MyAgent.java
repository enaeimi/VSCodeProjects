import java.lang.instrument.*;

public class MyAgent {

	public static void premain(String args, Instrumentation inst) {

		Person obj = new Person("AAA", "BBB", "CCCC", 1);
		long size = inst.getObjectSize(obj);
		System.out.println("Premain Method: Bytes used by object: " + size);
	}
}