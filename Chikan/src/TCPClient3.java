import java.io.*;
import java.net.*;
class TCPClient3
{
 public static void main(String args[]) throws Exception
 {
   String sentence;
   String modifiedSentence;
   //String host = args[0];
   //int    port = Integer.parseInt(args[1]);
   String host = "10.5.0.203";
   int    port = 25;



   
   try {
   
   BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
   
   Socket clientSocket = new Socket(host,port);
   DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
   BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
   modifiedSentence = inFromServer.readLine();
   System.out.println(modifiedSentence);

   
   System.out.print("CLIENT >> ");

   sentence = inFromUser.readLine();

   outToServer.writeBytes(sentence + '\n');

    
   modifiedSentence = inFromServer.readLine();
   System.out.println("SERVER >> "+modifiedSentence);
    
     

   clientSocket.close();
   } catch(Exception e)
    {
      System.out.println("Conexão recusada");
    }
 }
}
