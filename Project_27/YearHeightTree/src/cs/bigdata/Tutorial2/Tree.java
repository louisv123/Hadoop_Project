package cs.bigdata.Tutorial2;

public class Tree {
	// Avoid instantiation.
	private Tree() {}
	static void showCharacteristics(String line) {
		try {
		String[] splitted_line = line.split(";");
		String age = splitted_line[15];
		String height = splitted_line[9];
		System.out.println("Age: " + age + 
				", Height: " + height);
		}
		catch (java.lang.NullPointerException n) {
			System.out.println("End Line");
		}
	}
}
