import java.util.*;
import java.io.*;

class ManhattanDistAOC3 {
	static char[][] net;
	static int cX;
	static int cY;
	static boolean trackXY = true;
		
	static void resetXY(){
		boolean middle = true;
		if (!middle) {
			cX = 1;
			cY = net.length-2;
		}else{
			cX = net.length/2;
			cY = net.length/2;
		}
		
	}
	
	static void setXY(int x, int y){
		cX = x;
		cY = y;
	}
	
	static void setUp(int size){
	net = new char[size][size]; 
	resetXY();
	for (int x=0;x<size;x++) {
		for (int y=0;y<size;y++) {
			net[x][y]='.';
			if (x==cX && y==cY) {
				net[x][y]='o';
			}
		}
	}	
	}
	
	static void checkCorner(){
		for (int x=0;x<net.length;x++) {
				for (int y=0;y<net.length;y++) {
					int i =0;
					int j =0;
					try{
					if(net[x+1][y]=='-')i++;
					}catch (Exception e) {}
					try{
					if(net[x-1][y]=='-')i++;
					}catch (Exception e) {}
					try{
					if(net[x][y+1]=='|')j++;
					}catch (Exception e) {}
					try{
					if(net[x][y-1]=='|')j++;
					}catch (Exception e) {}
					if (j==1&&i==1) {
						if (net[x][y]=='o') {}else{
							net[x][y]='+';
						}
						
					}
				}
			}	
	}
	
	static void displayNet(){
		checkCorner();
		StringBuilder bob = new StringBuilder();
		for (int y=0;y<net.length;y++) {
				for (int x=0;x<net.length;x++) {
					bob.append(net[x][y]);
				}
				bob.append("\n");
			}	
			System.out.print(bob.toString());
	}
	
	static void right(int len){
		right(cX, cY,len);
	}
	
	static void right(int x, int y, int len){
		int i;
		for (i=x+1;i<=x+len;i++) {
			paint(i, y, 1);
		}
		setXY(i, y);
	}
	
	static void down(int len){
			down(cX, cY,len);
		}
		
	static void down(int x, int y, int len){
		int i;
			for (i=y+1;i<=y+len;i++) {
				paint(x, i, 2);
			}
			setXY(x, i);
		}
	
	static void up(int len){
			up(cX, cY,len);
		}	
		
	static void up(int x, int y, int len){
		int i;
				for (i=y-1;i>=y-len;i--) {
					paint(x, i, 2);
				}
				setXY(x, i);
			}
	static void left(int len){
			left(cX, cY,len);
		}
	
	static void left(int x, int y, int len){
			int i;
			for (i=x-1;i>=x-len;i--) {
					paint(i, y, 1)	;
			}
			setXY(i, y);
		}
		
	static void paint(int x, int y, int direction){
		//direction:
		//-> 1: -
		//-> 2: |
		if (net[x][y]!='.') {
			net[x][y]='X';
		}else{
			if (direction==1) {
				net[x][y]='-';
			}else{
				net[x][y]='|';
			}
		}	
	}
	
	static void runNow(String input){
		char dir = input.charAt(0);
		System.out.println(input.substring(1));
		switch (dir) {
			case 'R':
				right(Integer.parseInt(input.substring(1)));
				break;
			case 'L':
				left(Integer.parseInt(input.substring(1)));
				break;
			case 'U':
				up(Integer.parseInt(input.substring(1)));
				break;
			case 'D':
				down(Integer.parseInt(input.substring(1)));
				break;
			default:
				break;
		}
	}
	
	static void interpreter(){
		//Scanner scanner = new Scanner(System.in);
		BufferedReader scanner;
		Queue<String> data = new LinkedList<>();
		
		for(int z=0;z<2;z++) {
			resetXY();
			//String input = scanner.nextLine();
			String input = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51";
			try {
				scanner = new BufferedReader(new FileReader("inputAOC3.txt"));
				input = scanner.readLine();
			} catch (Exception e) {
				e.printStackTrace();
			}
			if (input.equals("")) {
				break;
			}
			int i =0;
			int j = input.indexOf(",",i);
			while (j!=-1) {
				data.add(input.substring(i,j));
				System.out.println("|"+input.substring(i,j)+"|");
				i = j+1;
				j = input.indexOf(",",i);	
			}
			data.add(input.substring(i));
		
			while (data.size()!=0) {
				runNow(data.poll());
			}
		}
	}
	
	static int[][] findX(){
		int[][] xar = new int[net.length*10][2];
		for (int j=0;j<xar.length;j++) {
			xar[j][0]=-1;
			xar[j][1]=-1;
		}
		int i =0;
		for (int y=0;y<net.length;y++) {
				for (int x=0;x<net.length;x++) {
					if (net[x][y]=='X') {
						//System.out.println("i: "+i+ "x: "+x);
						xar[i][0]=x;
						xar[i][1]=y;
						i++;
					}
				}
			}
			int end = xar.length;
			for (int j=0;j<xar.length;j++) {
				if (xar[j][0]==-1) {
					end = j;
					break;
				}
			}
			int[][] res = new int[end][2];
			for (int j=0;j<res.length;j++) {
				res[j][0]=xar[j][0];
				res[j][1]=xar[j][1];
			}
			return res;
	}
	
	static void printX(){
	int[][] res = findX();
	System.out.println("X: ");
	for (int i=0;i<res.length;i++) {
		System.out.println(res[i][0]+ " "+res[i][1] );
	}
	}
	
	static void calcDist(){
		resetXY();
		int[][] res = findX();
		int[] calc = new int[res.length];
		for (int i=0;i<res.length;i++) {
				if (res[i][0]-cX<0) {
					calc[i] = cX - res[i][0];
				}else{
					calc[i] = res[i][0]-cX;
				}
				if (res[i][1]-cY<0) {
					calc[i] =calc[i]+ cY - res[i][1];
				}else{
					calc[i] =calc[i]+ res[i][1]-cY;
				}
			}
			System.out.println("Distance:");
		for (int i=0;i<calc.length;i++) {
				System.out.println(calc[i]);
			}
		int shortest = 10000;
		for (int i=0;i<calc.length;i++) {
				if (calc[i]<shortest) {
					shortest = calc[i];
				}
			}
			System.out.println("\033[1;36m Shortest Distance: "+shortest+ "+-1 \033[0m");
	}
		
	public static void main(String[] args) {
		try {
			setUp(Integer.parseInt(args[0]));
		} catch (Exception e) {
			setUp(20000);
		}
		interpreter();
		resetXY();
		System.out.println("cX: "+cX+" cY: "+cY);
		printX();
		calcDist();
	}
}
