import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC8 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		StringBuilder bob = new StringBuilder();
		try{
		BufferedReader reader = new BufferedReader(new FileReader("inputAOC8.txt"));
		bob.append(reader.readLine());
		reader.close();
		}catch (FileNotFoundException e) {
				System.out.println("Error 404:  das File wurde nicht gefunden");
			}catch (IOException e) {
				System.out.println("Error:  Daten sind inkorrekt");
			}catch (NumberFormatException e) {
				System.out.println("Error");
			}
		//System.out.println(bob.toString());
		
		String[] filter = new String[52];
		
		for (int i=0;i<52;i++) {
			filter[i]= input.next();
		}
		
		
			boolean c=true;
			int nf=0;
			int len = bob.length()+1;
		while(bob.length()<len){
			len =bob.length();
			nf=0;
			c=false;
			for(int j=0;j<52;j++){
				for (int i=0;i<bob.length();i++) {
					if(bob.indexOf(filter[j])>=0){
					//System.out.println(bob.substring(bob.indexOf(filter[j]), bob.indexOf(filter[j])+2));
					bob.delete(bob.indexOf(filter[j]), bob.indexOf(filter[j])+2);
					System.out.println(filter[j]+ " entfernt");
					c=true;}else{ nf++;}
				}	
			}			
		}
		System.out.println(bob.length());
		//System.out.println("übrig bleibt " + bob.toString());
	}
}
