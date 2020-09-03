import java.io.*; import java.net.*; import javax.swing.JOptionPane;
class TCPClient5
{
 public static void main(String args[]) throws Exception
 {
   String sentence; String modifiedSentence; String host = "127.0.0.1"; 
   int    port = 110;
   String usuario = JOptionPane.showInputDialog("Usuario: ");
   String senha = JOptionPane.showInputDialog("Senha: ");  
   try {
   BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
   Socket clientSocket = new Socket(host,port);
   DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
   BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
   modifiedSentence = inFromServer.readLine();
   System.out.println(modifiedSentence);
   outToServer.writeBytes("user " + usuario + '\n');    
   modifiedSentence = inFromServer.readLine();    
   System.out.println("SERVER >> "+modifiedSentence);
   outToServer.writeBytes("pass " + senha + '\n');
   modifiedSentence = inFromServer.readLine();
   System.out.println("SERVER >> "+modifiedSentence);
   clientSocket.close();
   } catch(Exception e) { System.out.println("Conexão recusada"); } } }
