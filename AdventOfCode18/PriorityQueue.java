public class PriorityQueue {
        static final int SIZE = 32;
        Element[] q = new Element[SIZE];
        int len = 0;
        
        // Insert an element into the queue according to its priority
        boolean put(Element x) { 
        boolean done =false;
        try{
        if (len ==0) {
                q[0] = x;
                //System.out.println("erstes element");
        }
        else{
                if (q[len-1].getPriority()>=x.getPriority()) {
                        q[len]=x;
                        //System.out.println("letztes Element");
                }
                else{
                        for (int i=len-1;i>=0;i--) {
                                if (q[i].getPriority()<x.getPriority()) {
                         Element y = q[i];
                                q[i]=x;
                                q[i+1]=y;
                                                       }
                }}
        }
        len++;
        done =true;
        }catch (ArrayIndexOutOfBoundsException e) {
                done = false;
        }
        return done;
        }
        
        // Return the element with the highest priority from the queue
       Element get()       {
        Element x;
        if(len!=0){
        x = q[0];
        for(int i=0;i<=len-1;i++){
        q[i]=q[i+1]; 					
        }
        }else{x = null;}
        len--;
        return x;
        }
        
        // Return the queue length
        int length()        {return len;}

        // Print the queue contents
        public String toString() {
                String s ="";
                for (int i=0;i<len;i++) {
                     s = s+  q[i].getData();
                }
                return s;
        }
     /*   public static void main(String[] args){

                Element a = new Element(10, "hallo");
                put(a);
              System.out.print(get());
        }*/
}
