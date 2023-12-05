public class BubbleSort {


 /**
 * Vertauscht zwei Werte in einem Array an den gegebenen Positionen.
 **/
public static void swap(int i, int j, char[] characters) {
char z = '!';
z= characters[i];
characters[i] = characters[j];
characters[j] = z;
 }

 /**
 * Sortiert das Eingabearray und aendert das Array in place
 **/
 public static char[] sort(char[] characters) {
 /* Diese Methode muss implementiert werden */

boolean mixed = true;
while (mixed) {
	mixed =false;
	for (int i = 0;i < characters.length-1; i++) {
		if (characters[i]>characters[i+1]) {
			mixed =true;
			swap(i, i+1, characters);
		}
	}
}
return characters;
 }
 /**
 * Schreibt das Array auf die Ausgabekonsole
 **/
 public static String backString(char[] characters) {
 /* Diese Methode muss implementiert werden */
StringBuilder b= new StringBuilder();
for (int i =0; i<characters.length; i++) {
	b.append(characters[i]);
}
return b.toString();
 }

 /**
 * Die Hauptfunktion liest das Character Array und ruft die Sortierfunktion
 * und die Ausgabefunktion auf
 **/
 public static void main(String[] args) {
 if (args.length != 1) {
 System.out.println("Bitte rufen Sie das Programm mit einem Eingabewert auf");
 //System.out.println(" java BubbleSort ’dies ist ein text’");
 System.exit(-1);
 }
 char[] characters = args[0].toCharArray();

 
 //displayArray(sort(characters));

 }
 }