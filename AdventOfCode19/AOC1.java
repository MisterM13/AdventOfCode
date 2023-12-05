import java.util.*;

class AOC1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		StringBuilder bob = new StringBuilder();
		int resultat=0;
		bob.append("Output: \n");
		int index = 0;
		while (true){
		String nextLn = scanner.nextLine();
		if (nextLn.equals("")) {
			break;
		}
		int input = Integer.parseInt(nextLn);
		int res = input/3 -2;
		resultat = resultat + res;
		while ((res/3-2) > 0) {
			res = res/3-2;
			resultat = resultat+res;
		}
				}
		System.out.println(resultat);
	}
}