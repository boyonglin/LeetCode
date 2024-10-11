#include <iostream>
using namespace std;

// class default: private
class Base {
private:
    int privateVar = 1;  // accessible only within the class

protected:
    int protectedVar = 2; // accessible within the class and derived classes

public:
    int publicVar = 3; // accessible from anywhere

    void getPrivateVar() {
        cout << "Private Variable (from Base): " << privateVar << endl;
    }

    void getProtectedVar() {
        cout << "Protected Variable (from Base): " << protectedVar << endl;
    }
};

class Derived : public Base {
public:
    void getProtectedVar() {
        cout << "Protected Variable (from Derived): " << protectedVar << endl;
    }

    // error in accessing private member
    // void accessPrivateVar() {
    //     cout << "Private Variable (from Derived): " << privateVar << endl;
    // }
};

// struct default: public
struct MyStruct {
    int structVar = 4;
};

int main() {
    Base base;
    Derived derived;
    MyStruct myStruct;

    // error in accessing private and protected members
    // base.privateVar = 5;
    // base.protectedVar = 6;

    base.getPrivateVar();
    base.getProtectedVar();

    derived.getProtectedVar();

    cout << "Public Variable (from main): " << base.publicVar << endl;

    cout << "Struct Variable (from main): " << myStruct.structVar << endl;

    return 0;
}
