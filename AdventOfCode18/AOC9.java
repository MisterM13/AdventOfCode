import java.io.*;
import java.util.Scanner;
import java.nio.file.attribute.*;

class AOC9 {
	static int len = 101;
	static String[] first= new String[len];
	static String[] second= new String[len]; 
	static final String[] abc = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
	static int keyChain[]= new int[26];
	static int key;
	
	static int getInd(int index, int row){
		int res=-1;
		if(row==1){
			for (int i=0;i<26;i++) {
					if(first[index].equals(abc[i])){res=i;}
			}
		}else{
			for (int i=0;i<26;i++) {
					if(second[index].equals(abc[i])){res=i;}
					System.out.println(i);
			}
		}
			
			return res;
	}
	
	static String rekursiveSearch(int index){
		int i=index;
		StringBuilder bob = new StringBuilder();
		while(i<len){
			bob.append(i);
			bob.append(first[i]);
			bob.append(second[i]);
			for (int j=i;j<len;j++) {
				if(first[j].equals(second[i])){
					bob.append(rekursiveSearch(j));
				}
			}
			i++;	
		}
		bob.append("\n");
		return bob.toString();
		
/*		System.out.println("search started"+index+" "+key);
		keyChain[getInd(index,1)]=key;
	boolean nosecond=true;
	for (int i=index+1;i<len;i++) {
		System.out.print(i);
		if(first[index].equals(second[i])){nosecond=false;}
		System.out.println("erste if done");
		if(first[index].equals(first[i])){rekursiveSearch(i,key);}
		System.out.println("zweite if done");
		if(second[index].equals(first[i])){System.out.println("1level down");rekursiveSearch(i,key--);}
		else{keyChain[getInd(index,2)]=key;
		System.out.println(getInd(index,2));}
		System.out.println("dritte if done");
		}
		*/
	}
	
	public static void main(String[] args) {
		try{
		BufferedReader reader = new BufferedReader(new FileReader("inputAOC9.txt"));
		for (int i=0;i<len;i++) {
			String input = reader.readLine();
			first[i]= input.substring(0,1);
			second[i]=input.substring(2,3);
			//System.out.println(second[i]);
		}
		for (int i=0;i<abc.length;i++) {
			keyChain[i]=333;
		}
		reader.close();
		PriorityQueue q = new PriorityQueue(); 
		boolean found =false;
		key = len;
		for(int i=0;i<26;i++){
			boolean sec=false;
			for (int k=0;k<len;k++) {
					if (abc[i].equals(second[k])) {
							//System.out.println("key--");
							key--;
					found=true; sec=true;
					}
					if(abc[i].equals(first[k])){
						found=true;
						key=key+2;
					}
				}
				if(!sec){key=key+300-6*i;}
				if(found){
				q.put(new Element(key, abc[i]));
				System.out.println(key+ " "+abc[i]);
				//System.out.println(q.toString());
				}
				key=len;found=false;
		}
		//rekursiveSearch(0);
	/*	for (int i=0;i<26;i++) {
			if(keyChain[i]<300){q.put(new Element(keyChain[i],abc[i]));}
		}*/
		
		System.out.println(q.toString());
		
		
		
		
		}catch (FileNotFoundException e) {
				System.out.println("Error 404:  das File wurde nicht gefunden");
			}catch (IOException e) {
				System.out.println("Error:  Daten sind inkorrekt");
			}catch (NumberFormatException e) {
				System.out.println("Error");
			}
	}
}