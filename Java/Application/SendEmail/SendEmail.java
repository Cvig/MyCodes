// This java function send an email 
//Reference: http://www.tutorialspoint.com/java/java_sending_email.htm 

import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;

public class SendEmail
{
   public static void main(String [] args)
   {    
      // Recipient's email ID 
      String to = "xxx@gmail.com";

      // Sender's email ID 
      String from = "zzz@gmail.com";

      // sending from localhost
      String host = "localhost";

      // Get system properties
      Properties properties = System.getProperties();

      // Setup mail server
      properties.setProperty("mail.smtp.host", host);

      // Get the default Session object.
      Session session = Session.getDefaultInstance(properties);

      try{
         // Create a default MimeMessage object.
         MimeMessage message = new MimeMessage(session);

         // Set From: header field of the header.
         message.setFrom(new InternetAddress(from));

         // Set To: header field of the header.
         message.addRecipient(Message.RecipientType.TO, new InternetAddress(to));

         // Set Subject: header field
         message.setSubject("Hello");

         // Now set the actual message
         message.setText("Hello");

         // Send message
         Transport.send(message);
         
      }
	  catch (MessagingException mex) {
         mex.printStackTrace();
      }
   }
}