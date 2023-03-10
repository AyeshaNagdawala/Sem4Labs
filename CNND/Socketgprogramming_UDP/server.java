// Java Program Illustrating Server Side Implementation
// of Simple Calculator using UDP

// Importing required classes
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.StringTokenizer;

// Main class
// Calc_Server_UDP
class server {

	// MAin driver method
	public static void main(String[] args)
		throws IOException
	{

		// Creating a socket to listen at port 1234
		DatagramSocket ds = new DatagramSocket(1234);

		byte[] buf = null;

		// Initializing them initially with null
		DatagramPacket DpReceive = null;
		DatagramPacket DpSend = null;
			buf = new byte[65535];

			// Creating a DatagramPacket to receive the data.
			DpReceive = new DatagramPacket(buf, buf.length);

			// Receiving the data in byte buffer.
			ds.receive(DpReceive);

			String inp = new String(buf, 0, buf.length);

			// Using trim() method to
			// remove extra spaces.
			inp = inp.trim();

			System.out.println("Equation Received:- "
							+ inp);
                            int result;

			// Use StringTokenizer to break the
			// equation into operand and operation
			StringTokenizer st = new StringTokenizer(inp);

			int oprnd1 = Integer.parseInt(st.nextToken());
			int oprnd2 = Integer.parseInt(st.nextToken());
            if(oprnd1==0)
            {result=0;}
			else
				result = oprnd1 / oprnd2;

			System.out.println("Sending the result...");
			String res = Integer.toString(result);

			// Clearing the buffer after every message
			buf = res.getBytes();

			// Getting the port of client
			int port = DpReceive.getPort();

			DpSend = new DatagramPacket(
				buf, buf.length, InetAddress.getLocalHost(),
				port);
			ds.send(DpSend);

            System.out.println(
				"Answer = "
				+ new String(buf, 0, buf.length));
		}
	}
