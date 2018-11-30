package Sleeping;

import java.lang.instrument.Instrumentation;

public class MyAgent {

	private static volatile Instrumentation globalInstr;

	public static void premain(String args, Instrumentation inst) {
		globalInstr = inst;
		
		
		System.out.println("MyAgent: Instrumentation Applied !");
		inst.addTransformer(new SleepingClassTransformer());
	
	
	}

	public static long getObjectSize(Object obj) {
		if (globalInstr == null)
			throw new IllegalStateException("Agent not initted");
		return globalInstr.getObjectSize(obj);
	}
}
