import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC10 {
	static len = 60000
	static boolean[][] starGrid=new boolean[len][len];
	static int[][] movX=new int[len][len];
	static int[][] movY=new int[len][len];
	static boolean[][] evoStarGrid=new boolean[len][len];
	static int[][] emovX=new int[len][len];
	static int[][] emovY=new int[len][len];
	
	public static void main(String[] args) {
		for (int i=0;i<len;i++) {
			for (int j=0;j<len;j++) {
				
			}
		}
		try{
		BufferedReader reader = new BufferedReader(new FileReader("inputAOC10.txt"));
		String input= reader.readLine();
		
		
		
			}catch (FileNotFoundException e) {
				System.out.println("Error 404:  das File wurde nicht gefunden");
			}catch (IOException e) {
				System.out.println("Error:  Daten sind inkorrekt");
			}catch (NumberFormatException e) {
				System.out.println("Error");
			}
	}
}