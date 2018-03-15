package cs.bigdata.Tutorial2;


import java.io.*;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

import cs.bigdata.Tutorial2.Tree;

public class CompterLigneFile {

	private static BufferedReader br;

	public static void main(String[] args) throws IOException {
		
		String localSrc = "/Users/dmpierre/Desktop/DSBA COURSES/semester_1/big_data_algorithms/arbres.csv";
		//Open the file
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
				line = br.readLine();
				n_line = n_line + 1;
				Tree.showCharacteristics(line);
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


