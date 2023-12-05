import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC5 {
	static int len = 1000;
	static int[][] mesh = new int[len][len];
	static int inch;
	public static void main(String[] args) {
		for (int i=0;i<len;i++) {
			for(int j=0;j<len;j++){
			mesh[j][i]=0;
			}
		}
		
		try{
				BufferedReader reader = new BufferedReader(new FileReader("inputAOC5.txt"));
				while(true){
					
					String input = reader.readLine();
					if (input.equals("end")) {
						break;}
					
					
					int a = input.indexOf(",");
					int b = input.indexOf(":");
					int c = input.indexOf(" ",a)+1;
					int d = input.indexOf("x");
					int e = input.indexOf("@")+1;
					int linkRand = Integer.parseInt(input.substring(e+1,a));
					int oben = Integer.parseInt(input.substring(a+1,b));
					int brX = Integer.parseInt(input.substring(c,d));
					int brY = Integer.parseInt(input.substring(d+1));
				
					Fabric f = new Fabric(linkRand, oben, brX, brY);
				
					for (int i=0;i<len;i++) {
						for(int j=0;j<len;j++){
						mesh[j][i]=mesh[j][i]+ f.fabric[j][i];
						}
					}
				}
				for (int i=0;i<len;i++) {
					for(int j=0;j<len;j++){
					if(mesh[j][i]>=2){inch++;}
					}
					}
				System.out.println(inch);
				
				}catch (FileNotFoundException e) {
						System.out.println("Error 404:  das File wurde nicht gefunden");
					}catch (IOException e) {
						System.out.println("Error:  Daten sind inkorrekt");
					}catch (NumberFormatException e) {
						System.out.println("Error");
					}
	}
}