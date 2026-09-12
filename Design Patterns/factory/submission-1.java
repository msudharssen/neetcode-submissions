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

    

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Car();
        return ve;
    }

   

}

class BikeFactory extends VehicleFactory {
   

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Bike();
        return ve;
    }

    
}

class TruckFactory extends VehicleFactory {
    

    @Override
    public Vehicle createVehicle(){
        Vehicle ve = new Truck();
        return ve;
    }
}
    
