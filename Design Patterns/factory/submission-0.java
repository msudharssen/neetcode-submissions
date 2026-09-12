interface Vehicle {
    String getType();
}

class Car implements Vehicle {
    @Override
    public String getType() {
        return "Car";
    }
}

class Bike implements Vehicle {
    @Override
    public String getType() {
        return "Bike";
    }
}

class Truck implements Vehicle {
    @Override
    public String getType() {
        return "Truck";
    }
}

abstract class VehicleFactory {
    abstract Vehicle createVehicle();
}

class CarFactory extends VehicleFactory {

    private Vehicle v;
    // Write your code here
    public CarFactory(){
        
    }

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Car();
        this.v = ve;
        return ve;
    }

    public String getType(){
        return this.v.getType();
    }


}

class BikeFactory extends VehicleFactory {
    // Write your code here
   private Vehicle v;
    // Write your code here
    public BikeFactory(){
        
    }

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Bike();
        this.v = ve;
        return ve;
    }

    public String getType(){
        return this.v.getType();
    }
}

class TruckFactory extends VehicleFactory {
    // Write your code here
    private Vehicle v;
    // Write your code here
    public TruckFactory(){
        
    }

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Truck();
        this.v = ve;
        return ve;
    }

    public String getType(){
        return this.v.getType();
    }
}
