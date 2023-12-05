import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC6 {
	static int len = 1066;
	static Fabric[] mesh = new Fabric[len];
	static int[] over = new int[len];
	public static void main(String[] args) {
		for (int i =0;i<len;i++) {
			over[i]=0;
		}
		
		try{
				BufferedReader reader = new BufferedReader(new FileReader("inputAOC5.txt"));
				int count=0;
				while(true){
					
					String input = reader.readLine();
					if(count ==len){break;}
					if (input.equals("end")) {
						break;}
					
					
					int a = input.indexOf(",");
					int b = input.indexOf(":");
					int c = input.indexOf(" ",a)+1;
					int d = input.indexOf("x");
					int e = input.indexOf("@")+1;
					int g = input.indexOf("#")+1;
					int h = input.indexOf(" ");
					int linkRand = Integer.parseInt(input.substring(e+1,a));
					int oben = Integer.parseInt(input.substring(a+1,b));
					int brX = Integer.parseInt(input.substring(c,d));
					int brY = Integer.parseInt(input.substring(d+1));
					int id = Integer.parseInt(input.substring(g,h));
					
					
					mesh[count]= new Fabric(linkRand, oben, brX, brY,id);
					count++;
				}
				
			/*	boolean found=false;
				int n =0;
				for(int i=0;i<count;i++){
					if(n==count-i){found=true;}else{
					for(int j=i+1;j<count;j++){
						if(!mesh[i].overlaps(mesh[j])){n++;}
					}}
					if(found){System.out.println(mesh[i].returnID());}
				}
				*/
				for(int i=0;i<count;i++){
				for(int j=0;j<count;j++){
					if(i==j){}else{
					if(mesh[i].overlaps(mesh[j])){over[i]=over[i]+1;
					//System.out.println(mesh[i].returnID());
					}
					}
				}
				System.out.println(over[i]);
				}
				for (int i=0; i<len;i++) {
					if(over[i]==0){System.out.println("Das Resultat: "+mesh[i].returnID());}
				}
				}catch (FileNotFoundException e) {
						System.out.println("Error 404:  das File wurde nicht gefunden");
					}catch (IOException e) {
						System.out.println("Error:  Daten sind inkorrekt");
					}catch (NumberFormatException e) {
						System.out.println("Error");
					}
	}
}