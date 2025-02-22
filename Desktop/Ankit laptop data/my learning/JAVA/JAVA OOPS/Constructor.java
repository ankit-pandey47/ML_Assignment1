// 1. A constructor in Java is a special method that is used to initialize objects
// 2. The constructor is called when an object of a class is created. It can be used to set initial values for object attributes.
// 3. Constructors must have the same name as the class within which it is defined it is not necessary for the method in Java.
//  Constructors do not return any type while method(s) have the return type or void if does not return any value.
// Constructors are called only once at the time of Object creation while method(s) can be called any number of times.

// Three types of Constructor
// 1> Default Constructor       2> Parametrized  Constructor     3> Copy Constructor

//A copy constructor in Java is a special constructor used to create a new object by copying the properties of an existing object.

class Animal {
    int age = 10;

    Animal() {
        age = 15;
        System.out.println("I am the constructor of Animal class");
    }
}

public class Constructor {
    public static void main(String[] args) {

        Animal animal = new Animal();
        System.out.println(animal.age);
    }
}