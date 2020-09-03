import java.net.*;
class MultiServer
{
 public static void main(String args[]) throws Exception
 {
   //int    port = Integer.parseInt(args[0]); 
   int port = 8000;	

   ServerSocket welcomeSocket = new ServerSocket(port);
  
   while(true)
   {
    new ThreadServer(welcomeSocket.accept()).start();
   }
 }
} //fim da classe;

