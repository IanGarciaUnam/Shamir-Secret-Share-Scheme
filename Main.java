import java.math.BigInteger;  
import java.nio.charset.StandardCharsets; 
import java.security.MessageDigest;  
import java.security.NoSuchAlgorithmException; 

public class Main{

	public static void main(String[] args){
		System.out.println("Hash code generated");

		String s1= args[0];
		System.out.println("\n" + s1 + " : " + toHexString(getSHA(s1))); 


	}

	public static byte[] getSHA(String s){
			MessageDigest md;
		try{
			 md = MessageDigest.getInstance("SHA-256");
			 return md.digest(s.getBytes(StandardCharsets.UTF_8));
		}catch(NoSuchAlgorithmException n){
			System.out.println(n.toString());
		}

		return null;
	}

	
	public static String toHexString(byte[] hash) 
    { 
        // Convert byte array into signum representation  
        BigInteger number = new BigInteger(1, hash);  
  
        // Convert message digest into hex value  
        StringBuilder hexString = new StringBuilder(number.toString(16));  
  
        // Pad with leading zeros 
        while (hexString.length() < 32)  
        {  
            hexString.insert(0, '0');  
        }  
  
        return hexString.toString();  
    }









}