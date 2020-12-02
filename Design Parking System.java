/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
class ParkingSystem {
    int bigSpots;
    int medSpots; 
    int smallSpots;
    
    public ParkingSystem(int big, int medium, int small) {
        this.bigSpots = big;
        this.medSpots = medium;
        this.smallSpots = small;
    }
    
    public boolean addCar(int carType) {
        boolean possible = false;
        switch(carType){
            case 1: // big
                if(this.bigSpots >= 1){
                    possible = true;
                    bigSpots--;
                }else
                    possible = false;
                break;
            case 2: // medium
                 if(this.medSpots >= 1){
                    possible = true;
                    medSpots--;
                 }else
                    possible = false;
                break;
            case 3: // small
                 if(this.smallSpots >= 1){
                    possible = true;
                    smallSpots--;
                 }else
                    possible = false;
                break;
        }
        
        return possible;
    }
}
