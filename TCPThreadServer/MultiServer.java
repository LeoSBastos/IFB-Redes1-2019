import java.net.*;
class MultiServer
{
 public static void main(String args[]) throws Exception
 {
   String clientSentence;
   //int    port = Integer.parseInt(args[0]); 
   int port = 6000;	

   ServerSocket welcomeSocket = new ServerSocket(port);
  
   while(true)
   {
    new ThreadServer(welcomeSocket.accept()).start();
   }
 }
} //fim da classe;

