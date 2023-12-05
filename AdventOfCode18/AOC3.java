import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC3 {
	static int twins =0;
	static int triple =0;
	
	public static void main(String[] args) {
	try{
		//Scanner reader = new Scanner(System.in);
		BufferedReader reader = new BufferedReader(new FileReader("inputAOC3.txt"));
		int checksum =0;
		String[]box = new String[1000];
		int blen=0;
		boolean eq =false;
		
		while(true){
			//String input = reader.next();
			String input = reader.readLine();
			char[] a = new char[input.length()];
			for (int i=0;i<input.length();i++) {
			a[i] = input.charAt(i);
			}
			box[blen]=BubbleSort.backString(BubbleSort.sort(a));
			
			if(blen>0){
				for (int i=0;i<blen;i++) {
			if(BubbleSort.backString(BubbleSort.sort(a)).equals(box[i])){
		    eq=true;System.out.println("doppelt");}
			}}
			blen++;
			
			if (input.equals("end")) {
				break;
			}else if(!eq){
				
				char[] sortArr = BubbleSort.sort(a);
				//System.out.println(BubbleSort.backString(BubbleSort.sort(a)));
				
				int c =0;
				int v =0;
				boolean sec=false;
				boolean dpair=false;
				boolean tpair=false;
				boolean row=false;
				/*for (int i=1;i<input.length();i++) {
					if(sortArr[i-1]==sortArr[i]){c++;v++;}
					row = v>2;
					if(c==2){
						if(!tpair){triple++;}
						c=0;sec=false;tpair=true;
					System.out.print(" triple");
					}
					else if(c==1&&sec){
						if(!dpair){twins++;System.out.print(" twins");}
						c=0;sec=false;dpair=true;
					}
					else if(c==1){sec=true;}
					else{sec=false;}
					}
					if(sec&&!dpair&&!row){twins++; sec=false;}
					*/
					
					for (int i=1;i<input.length();i++) {
						if(sortArr[i-1]==sortArr[i]){
							if(i+1<input.length()){
								if(sortArr[i-1]==sortArr[i+1]){
									if(!tpair){triple++;tpair=true;i++;System.out.print(" triple");}
									if(i+2<input.length()){if(sortArr[i+2]==sortArr[i])i++;}	
								}	
								else{
								if(!dpair){twins++;dpair=true;System.out.print(" twins");}
								}
							}
							else{
							if(sortArr[i]==sortArr[i-1]&&sortArr[i]==sortArr[i-2]){if(!tpair){triple++;tpair=true;i++;System.out.print(" triple2");}}
							else if(!dpair){twins++;dpair=true;System.out.print(" twins2");}
							}
						}	
					}		
					System.out.println("\n"+BubbleSort.backString(BubbleSort.sort(a)));
	}
	eq=false;
		}
	checksum = twins * triple;
	System.out.println(twins+ "twins");	System.out.println(triple+ "triple");

	System.out.println(checksum);
	
	}catch (FileNotFoundException e) {
		System.out.println("Error 404:  das File wurde nicht gefunden");
	}catch (IOException e) {
		System.out.println("Error:  Daten sind inkorrekt");
	}catch (NumberFormatException e) {
		System.out.println("Error:  Bitte geben sie eine Postleitzahl ein, nicht einen Nahmen.");
	}
	}
}