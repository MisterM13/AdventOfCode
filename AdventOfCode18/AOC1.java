import java.util.Scanner;

class AOC1 {
	static int x =0;
	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		int[] y = new int[100000];
		int len = 1;
		int res = -987654321;	
		boolean first = true;
		y[0]=0;
		
		while(true){
			String input = reader.next();
			if (input.equals("end")) {
				break;
			}else{
			x=x+Integer.parseInt(input);
			for (int i=0;i<len;i++) {
				if(y[i]==x&&first){res =y[i];first=false;}
			}
			y[len]=x;
			len++;
			//System.out.println("|"+x+"|");
			}
		}
		System.out.println(x);
	}
}
