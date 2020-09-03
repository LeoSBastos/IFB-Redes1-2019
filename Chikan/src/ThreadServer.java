import java.net.*;
import java.io.*;
public class ThreadServer extends Thread
{
  Socket connectionSocket; 
  public ThreadServer(Socket s)    {       
    connectionSocket = s;
   } 
  public void run()
  {
   String clientSentence;
   try{
   BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
   DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
   String hello = "Bem Vindo ao TCPServer\n";
   outToClient.writeBytes(hello);
   do{
      clientSentence = inFromClient.readLine();
      outToClient.writeBytes(clientSentence+"\n");
     }while(!clientSentence.equals("quit"));
   }catch(Exception E)
   { System.out.println(E);}
  }
}
