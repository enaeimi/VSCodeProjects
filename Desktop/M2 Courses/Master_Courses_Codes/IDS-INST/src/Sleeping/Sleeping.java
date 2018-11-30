package Sleeping;

public class Sleeping {
	public void randomSleep() throws InterruptedException {
		// randomly sleeps between 500ms and 1200s
		long randomSleepDuration = (long) (500 + Math.random() * 700);
		System.out.printf("Sleeping for %d ms ..\n", randomSleepDuration);
		Thread.sleep(randomSleepDuration);
	}

	public int sum(int x, int y) {
		return x + y;
	}

}