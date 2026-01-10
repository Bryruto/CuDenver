#include <cstdio>

enum class operation{
    Add,
    Subtract,
    Multiply,
    Divide
};

struct Calculator{
    operation op;

    Calculator(operation x) : op{x} {}

    float calculate(int a, int b){
        float value;
        switch(op)
        {
        case operation::Add:
            value = a + b;
            break;
        case operation::Subtract:
            value = a - b;
            break;
        case operation::Multiply:
            value = a * b;
            break;
        case operation::Divide:
            value = a/b;
            break;
        
        default:
            break;
        }
        return value;
    };



};

int main(void){

    Calculator a{operation::Add};
    Calculator s{operation::Subtract};
    Calculator m{operation::Multiply};
    Calculator d{operation::Divide};

    printf("add -> %f\n",a.calculate(5,6));
    printf("subtract -> %f\n",s.calculate(5,4));
    printf("multiply -> %f\n",m.calculate(5,6));
    printf("divide -> %f\n",d.calculate(5,5));
}