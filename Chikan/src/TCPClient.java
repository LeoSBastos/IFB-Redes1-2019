import java.io.*;
import java.net.*;
class TCPClient
{
 public static void main(String args[]) throws Exception
 {
   String sentence;
   String modifiedSentence;
   String host = "localhost";
   int    port = 8000; // smtp - 25   POP3 - 110

   			  
   try {
   
   BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
   
   Socket clientSocket = new Socket(host,port);
   DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
   BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
   modifiedSentence = inFromServer.readLine();
   System.out.println(modifiedSentence);

   do{
   System.out.print("CLIENT >> ");

   sentence = inFromUser.readLine();

   outToServer.writeBytes(sentence + '\n');

     do {
          modifiedSentence = inFromServer.readLine();
          System.out.println("SERVER >> "+modifiedSentence);
        } while(inFromServer.ready());
     
   }while(!sentence.equals("SAIR"));
   clientSocket.close();
   } catch(Exception e)
    {
      System.out.println("Conexão recusada");
    }
 }
}
