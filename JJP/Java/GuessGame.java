import java.util.Scanner;
	public class GuessGame {
		public static void main (String [] args) {
		Scanner input = new Scanner(System.in);
		
		int guessNumber = 57;
    int count = 1;
    
    System.out.print("Guess a number from (1-100): ");
    int number = input.nextInt();
    
    if (number==guessNumber) {
    System.out.println("You entered the guess number correctly");
    System.exit(0);
    }
    
    while(number>0) {
    System.out.print("Guess a number from (1-100): ");
    number = input.nextInt();
    count += 1;
		
		if (number==guessNumber) {
		System.out.println("You entered the guess number correctly");
		System.out.println(count);
		break;
		}
		}
		}
		}
