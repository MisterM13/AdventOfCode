class AOC4 {
	static int x = 10;
	static int a = -1;
	static int c =0;
	static boolean doppelt =false;
	static boolean trippel =false;
	static boolean allRight = false;
	static boolean log = false;
	static int old =-1;
/*	
	static boolean test(int i){
		boolean check = true;
		if (i%x*10 == i) {
			check=true;
			x=1;
			a=-1;
			check = doppelt&&!kleiner;
			doppelt =false;
			kleiner =false;
		}else if(a==-1) { 
			a = i%x*10;
		}else {
			if (a == i%x*10) {
				doppelt = true;
			}
			if (a < i%x*10) {
				kleiner = true;
				check = false;
			}	
		}
		x++;
		if (check) {
			check=test(i);
		}
		return check;
	}*/
	static void run(int z){
		boolean res = true;
		int links  = 0;
		int rechts = 0;
		int y =0;
		
		rechts = z%x;
		for (int i=0;i<=4;i++) {
			if(i>0)rechts = links;
			x=x*10;
			links = z%x -rechts;
			links = links/(x/10);
			if(log)System.out.println("rechts: "+rechts);
			if(log)System.out.println("links: "+links);
			if (!test(links, rechts)) {
				res = false;
				break;
			}
			
		}
		if (res&&doppelt) {
			if(log)System.out.println("c++");
			doppelt =false;
			c++;
		}
		x=10;
		
	}
	
	static boolean test(int links, int rechts){
		boolean check;
		if (links>rechts) {
			check =false;
		}else if (links==rechts) {
			if(old==rechts)trippel = true;
			doppelt = true;
			check = true;
			old = links;
		}else {
			if (trippel) {
				check = false;
			}else {
				check = true;
			}
			trippel = false;
			old = -1;
		}
		return check;
	}
	
	
	public static void main(String[] args) {
		
		for (int i = 168630;i<=718098;i++) {
			run(i);
		}
		
		//run(123556);
		System.out.println(c);
	}
}