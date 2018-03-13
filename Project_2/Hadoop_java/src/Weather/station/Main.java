package Weather.station;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

import Weather.station.Weather_station;

public class Main {
	
	private static BufferedReader br;

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		//open the file
		String localSrc = "/home/louis/Documents/Data_science/Big_data_tools/input.txt";
		Configuration conf = new Configuration();
		FileSystem fs = FileSystem.get(conf);
		InputStream in = new BufferedInputStream(new FileInputStream(localSrc));
		try{
			InputStreamReader isr = new InputStreamReader(in);
			br = new BufferedReader(isr);
			
			// read line by line
			String line = br.readLine();
			int n_line = 0;
			
			while (line !=null){
				// Process of the current line
				// go to the next line
				n_line = n_line + 1;
				line = br.readLine();	
				
				if(n_line>22) {
					
				    Weather_station.showCharacteristics(line);
				
					}
				
				}
			System.out.println("Number of lines is: " + n_line);
		}
		finally{
			//close the file
			in.close();
fs.close();

	}

}
}
