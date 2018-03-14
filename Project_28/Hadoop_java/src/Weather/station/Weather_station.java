package Weather.station;

public class Weather_station {
	//avoid instantiation
	private Weather_station() {}
	static void showCharacteristics(String line) {
		try {
			String station_name = line.substring(13, 42).trim().replaceAll(" +", " ");
			String FIPS =line.substring(43,45);
			String Altitude =line.substring(74,81);
			System.out.println("Station name: "+station_name+", Country: "+FIPS+", Altitude: "+Altitude);
		
		
			
			}
		catch(java.lang.NullPointerException n) {
			System.out.println("End Line");
		}
	}
	
	

}
