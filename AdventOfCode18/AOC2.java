import java.util.Scanner;

class AOC2 {
	static int x =0;
	static int inlen =0;
	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		int[] y = new int[10000000];
		int[] input = new int[1000000];
		
		int len = 1;
		int res = -987654321;	
		int in = 0;
		boolean first = true;
		boolean notfound = true;
		
		while(true){
			String inp = reader.next();
			if (inp.equals("end")) {
				break;
			}else{
			input[inlen]=Integer.parseInt(inp);
			inlen++;
			//System.out.println(input[inlen-1]);
			}
		}
		
		
		while(notfound){
			if(in==inlen){in=0;}
			x=x+input[in];
			in++;
			for (int i=0;i<len;i++) {
				if(y[i]==x&&first){res =y[i];first=false;notfound =false;}
			}
			y[len]=x;
			len++;
			System.out.println("|"+x+"|");
			}
		//System.out.println(x);
		System.out.println(res);
	}
}
