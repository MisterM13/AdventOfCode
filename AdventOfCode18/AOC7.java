import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC7 {
	//static int[][][] dayArray =new int[500][365][60]; //GuardNum day time
	static int[] dateArr = new int[365];
	static boolean[][] timeArr = new boolean[365][60];
	static int[] numbArr = new int[365];
	static int[] guardNum;
	static int[] guardSl;
	static boolean sleep = false;
	static boolean notChange =true;
	static int d=0;
	static int n=0;
	static int t=0;
	public static void main(String[] args) {
		try{
				BufferedReader reader = new BufferedReader(new FileReader("inputAOC7c.csv"));
				
				while(true){
				String input = reader.readLine();
				if (input.equals("end")) {
					break;}
					
					
				
				int a= input.indexOf(";");
				int b= input.indexOf(";",a+1);
				int c= input.indexOf(";",b+1);
				
								
				int date = Integer.parseInt(input.substring(0,a));
				if(d==0){dateArr[0]=date;d++;}
				else if(date != dateArr[d-1]){dateArr[d]=date;d++;}
				
				if(c>0){int guardNum = Integer.parseInt(input.substring(b+1,c));
				numbArr[n]=guardNum;
				n++;notChange=false;t=0;sleep=false;
				}
				
				int time = Integer.parseInt(input.substring(a+1,b));
				if(time <60&&notChange){ 
					for(int i=t;i<time;i++){
						timeArr[d-1][i]=sleep;
					}
					sleep=!sleep;
					timeArr[d-1][time]=sleep;
					t=time+1;	
				}
				notChange=true;			
			}	 
			reader.close();
			
			int[] realTime= new int[365];
			for(int i=0;i<365;i++){
					realTime[i]=0;
			}
			
			for(int i=0;i<365;i++){
				for(int j=0;j<60;j++){
					if (timeArr[i][j]) {
						realTime[i]=realTime[i]+1;
					}
				}	
			}	
			guardNum = new int[365];
			guardSl = new int[365];
			
			for (int i=0;i<365;i++) {
				guardNum[i]=0;
				guardSl[i]=0;
			}
			
			for (int i=0;i<365;i++) {
				boolean ndouble =true;
				for (int j=0;j<i;j++) {
					if(numbArr[i]==numbArr[j]){ndouble=false;}
				}
				if(ndouble){
					guardNum[i]=numbArr[i];
					guardSl[i]=realTime[i];
					for (int j=i+1;j<365;j++) {
						if(numbArr[i]==numbArr[j]){guardSl[i]=guardSl[i]+realTime[j];}
					}
				}
			}
			
			int max =0;
			int ind =0;
			for (int i=0;i<365;i++) {
				if(guardSl[i]>max){max=guardSl[i]; ind=guardNum[i];
				
				}
			}
			System.out.println(max +"  #"+ind);	
			GetDurchschnitt guard = new GetDurchschnitt(timeArr, numbArr, ind);
			guard.retMax();
			
				
			}catch (FileNotFoundException e) {
					System.out.println("Error 404:  das File wurde nicht gefunden");
				}catch (IOException e) {
					System.out.println("Error:  Daten sind inkorrekt");
				}catch (NumberFormatException e) {
					System.out.println("Error");
				}	
		
	}
}