class GetDurchschnitt{
	int min[] = new int[60];
	int guard;
	
	GetDurchschnitt(boolean[][] timeArr, int[] numbArr, int guard){
		this.guard = guard;
		for (int i=0;i<60;i++) {
			min[i]=0;
		}
		
		for (int i=0;i<365;i++) {
			if(numbArr[i]==guard){
				for (int j=0;j<60;j++) {
					if(timeArr[i][j]){min[j]=min[j]+1;}
				}
			}
		}
	}
	
	void retMax(){
		int max =0;
		int index =0;
		for (int i=0;i<60;i++) {
			if(min[i]>max){max=min[i]; index =i;
			//System.out.println(max+ " "+ i);
			}
		}	
		System.out.println("Durchschnittlich schläft Guard #"+guard+" in der Minute "+ index+" am meisten. nähmlich "+max +" Mal");
		System.out.println("Die Lösung ist also: "+guard*index);
	}
}