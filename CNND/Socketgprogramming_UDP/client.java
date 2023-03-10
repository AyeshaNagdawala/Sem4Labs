// Java Program to illustrate Client Side implementation
// of Simple Calculator using UDP

// Importing required classes
import java.io.IOException;
// Importing classes fromjava.nio package as
// this package is responsible for networking
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

// Main class
// Calc_Client_UDP
public class client {

	// Main driver method
	public static void main(String args[])
		throws IOException
	{

		// Creating an object of Scanner class to read user
		// input
		Scanner sc = new Scanner(System.in);

		// Step 1
		// Create the socket object for carrying data
		DatagramSocket ds = new DatagramSocket();

		InetAddress ip = InetAddress.getLocalHost();
		byte buf[] = null;
			System.out.println(
				"Enter two numbers : ");

			// Awaiting from entered input
			String inp = sc.nextLine();
			buf = new byte[65535];

			// Converting the String input into the byte
			// array
			buf = inp.getBytes();

			// Step 2
			// Creating the datagramPacket for sending the
			// data.
			DatagramPacket DpSend = new DatagramPacket(
				buf, buf.length, ip, 1234);

			// Invoking the send call to actually send the
			// data.
			ds.send(DpSend);
			buf = new byte[65535];
			// Creating an object of DatagramPacket class
			DatagramPacket DpReceive
				= new DatagramPacket(buf, buf.length);

			ds.receive(DpReceive);

			// Print and display command
			System.out.println(
				"Answer = "
				+ new String(buf, 0, buf.length));
		}
	}
