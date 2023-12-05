import java.util.*;
import java.io.*;

class IntcodeComputerAOC2 {
	static int[] code;
	static int[] backup;
	static boolean log = true;
	static int testFailed = 0;
	static int testPassed = 0;
	static boolean allTests = false;
	
	static void reset1202(){
		code[1]=12;
		code[2]=2;
	}
	
	public static int opcode(int a, int b, int c, int d){
	int re = -1;
		if (a == 1) {
			code[d] = code[b]+code[c];
			if(log)System.out.println(code[d]);
			re = 1;
		}
		if (a == 2) {
			code[d] = code[b]*code[c];
			if(log)System.out.println(code[d]);
			re = 1;
		}
		if (a == 99) {
			System.out.println("Finished with Code 99");
			re = 0;
		}
		return re;
	}
	
	public static int opcodeV2(int a, int b, int c, int d){
	int re = -1;
	if(log)System.out.println("ausgeführte CodeBefehle:");
	switch (a) {
		case 1:
			code[d] = code[b]+code[c];
			if(log)System.out.println("1-> "+d+"="+code[d]);
			re = 1;
			break;
		case 2:
			code[d] = code[b]*code[c];
			if(log)System.out.println("2-> "+d+"="+code[d]);
			re = 1;
			break;
		case 99:
			if(log)System.out.println("99");
			re = 0;
			break;
		/*case 101:
			code[d] = b+code[c];
			if(log)System.out.println("101-> "+d+"="+code[d]);
			re = 1;
			break;*/
		case 1001:
			code[d] = code[b]+c;
			if(log)System.out.println("1001-> "+d+"="+code[d]);
			re = 1;
			break;
		case 1002:case 74:
			code[d] = code[b]*c;
			if(log)System.out.println("1002-> "+d+"="+code[d]);
			re = 1;
			break;
		case 11001:case 1101:
			code[d] = b+c;
			if(log)System.out.println("11001-> "+d+"="+code[d]);
			re = 1;
			break;
		case 11002://case 1102://:case -85:
			code[d] = b*c;
			if(log)System.out.println("11002-> "+d+"="+code[d]);
			re = 1;
			break;
		case 3:
			input(b);
			if(log)System.out.println("3-> input="+code[b]);
			re = 2;
			break;
		case 4:
			output(code[b]);
			if(log)System.out.println("4->output");
			re = 2;
			break;
		default:
			if(log)System.out.println(" \033[4;35m unknown Comand: \033[0m"+ a);
			break;
	}
	return re;
	}
	
	public static int opcode(int a){
		int re = -1;
		if (a == 99) {
			System.out.println("Finished with Code 99");
			re = 0;
		}
		return re;
	}
	
	static void wrontInputHandler(int a, int b, int c, int d){
		
	}
	
	static void input(int pos){
		boolean individual = false;
		if (individual) {
			Scanner scanner = new Scanner(System.in);
			System.out.println("Bitte geben Sie einen input ein:");
			String input = scanner.nextLine();
			code[pos]= Integer.parseInt(input);
		}else {
			code[pos]=1;
		}
		
	}
	
	static void output(int b){
		int testCounter = testFailed + testPassed;
		if (b ==0) {
			System.out.println("\u001B[32m ************-PASSED-************ \u001B[0m");
			testPassed++;
		}else if(testCounter==7){
			System.out.println("\n\033[1;34m \033[42m ### CHECKSUM: " +b+ " ### \u001B[0m");
			System.out.println("\033[0;36m "+testPassed+" of "+testCounter+" tests passed.\u001B[0m");
		}else{
			System.out.println("\u001B[31m"+"OUT:" +b);
			System.out.println("\u001B[31m ************-FAILED-************ \u001B[0m");
			testFailed++;
		}
	}
	
	public static void setUpArray(int size){
		Scanner scanner = new Scanner(System.in);
		String input = scanner.nextLine();
		code = new int[size+1];
		backup = new int[size+1];
		int p = 0;
		int i = 0;
		int j = 1;
		while (j!=-1) {
			code[p]= Integer.parseInt(input.substring(i,j));
			backup[p]= Integer.parseInt(input.substring(i,j));
			if(log)System.out.println(code[p] +" "+p);
			i = j+1;
			j = input.indexOf(",",i);
			p++;	
		}
		code[p]= Integer.parseInt(input.substring(i));
		backup[p]= Integer.parseInt(input.substring(i));
		//if(log)System.out.println(code[p] +" "+p);
		
	}
	public static void setUpArrayV2(int size){
			BufferedReader scanner;
			String input = "hello world";
			try {
				scanner = new BufferedReader(new FileReader("inputAOC5.txt"));
				input = scanner.readLine();
			} catch (Exception e) {
				e.printStackTrace();
			}
			code = new int[size+1];
			backup = new int[size+1];
			int p = 0;
			int i = 0;
			int j = 1;
			while (j!=-1) {
				code[p]= Integer.parseInt(input.substring(i,j));
				backup[p]= Integer.parseInt(input.substring(i,j));
				//if(log)System.out.println(code[p] +" "+p);
				i = j+1;
				j = input.indexOf(",",i);
				p++;	
			}
			code[p]= Integer.parseInt(input.substring(i));
			backup[p]= Integer.parseInt(input.substring(i));
			//if(log)System.out.println(code[p] +" "+p);
			
		}
		
public static void process(){
		int a = 0;
		int b = 1;
		int c = 2;
		int d = 3; 
			while(a< code.length -1 && opcode(code[a], code[b], code[c], code[d])==1){
					a = d+1;
					b = a+1;
					c = b+1;
					d = c+1;
				}
			if (a==code.length-1) {
				int fin = opcode(code[a]);
				if(fin!=0){System.out.println("System Exit with: ");};
			}
}

static void processV2(){
	int a = 0;
	int b = 1;
	int c = 2;
	int d = 3; 
		while (a< code.length -1) {
			if(log)System.out.println("codeZugriffe: "+ a+"/"+code[a]+" "+ b+"/"+code[b]+" "+ c+"/"+code[c]+" "+ d+"/"+code[d]+" ");
			int status = opcodeV2(code[a], code[b], code[c], code[d]);
			if (status*status==1) {
				a = d+1;
				b = a+1;
				c = b+1;
				d = c+1;
			}else if(status ==0){
				System.out.println("\nNotification 99: End of Code");
				break;
			}else{
			a = c;
			b = a+1;
			if(b+1<code.length -1){c = b+1;
			}else{c = -1;}
			if(b+1<code.length -1){d = c+1;
			}else{d = -1;}
		}
	}
}

public static void printCode(){
	for (int i=0;i<code.length;i++) {
			System.out.println(code[i]);
		}
}

public static void resetOneTwo(int noun, int verb){
	code[1]=noun;
	code[2]=verb;
}

public static void findNounVerb(){
	for (int a=0;a<=99;a++) {
		for (int b=0;b<=99;b++) {
			resetOneTwo(a,b);
			process();
			System.out.println(code[0]);
			if (code[0]==19690720) {
				System.out.println("noun: "+ a);
				System.out.println("verb: "+ b);
				int x = 100*a+b;
				System.out.println("NounVerbCode: "+x);
				printCode();
				a=b=100;
			}
			resetCode();
		}
	}
}
public static void resetCode(){
	log =true;
	for (int i =0;i<backup.length;i++) {
		code[i]=backup[i];
	}
	if(log)System.out.println("Code erneuert.");
	log=false;
}
	
public static void main(String[] args) {
	int size = 1000;
	setUpArrayV2(size);
	processV2();
	//printCode();
	}
	
}