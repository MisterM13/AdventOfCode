class Fabric {
	int[][] fabric;
	int len = 1000;
	int id;
	
		
	Fabric(int linkRand, int oben, int brX, int brY){
		fabric = new int[len][len];
		for (int i=0;i<len;i++) {
			for(int j=0;j<len;j++){
			fabric[j][i]=0;
			}
		}
		for (int i=oben;i<(oben+brY);i++) {
			for(int j=linkRand;j<(linkRand+brX);j++){
				fabric[j][i]=1;
			}
		}
		
	}
	
	Fabric(int linkRand, int oben, int brX, int brY, int id){
			this.id = id;
			fabric = new int[len][len];
			for (int i=0;i<len;i++) {
				for(int j=0;j<len;j++){
				fabric[j][i]=0;
				}
			}
			for (int i=oben;i<(oben+brY);i++) {
				for(int j=linkRand;j<(linkRand+brX);j++){
					fabric[j][i]=1;
				}
			}
		}

	Boolean overlaps(Fabric other){
		boolean ret = false;
		for (int i=0;i<len;i++) {
			for(int j=0;j<len;j++){
			if(this.fabric[j][i]==1&&other.fabric[j][i]==1){
				ret=true;
			}
			}
		}
		return ret;
	}
	
	int returnID(){
		return this.id;
	}
}