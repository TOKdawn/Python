#include <iostream>

using namespace std;
//30%C++   70%c这是在企业中的占比
//框架 MFC QT cocox2d
//C++面试题,实现多态的三个条件
//从面向过程==>面向对象思想转换
//C++编译器如何知道是哪一个具体的对象调用函数? C++对象管理模型 多态的原理实现 多态实现的条件
//对象的生命周期
class Circle{//类是吧属性和方法进行封装
public:
    double r;
    double s;
public:
    double getR(){ 
        return r;
    }
    void setR(double val) {
        r = val;
    }
    double getS(){
        s = 3.14*r*r;//增加功能时是在编辑类
        return s;
    }
         
};
//在类的大括号之间是类的内部,其他的是类的外部
class TT{
  public://不管在类的内外都可以使用
  protected:
  private://只能在类的内部使用
    //默认是private
            
};
//面向过程编程加工的是函数
//面向对象编程加工的是类
//
int main(int argc, char *argv[]) {
    Circle c1,c2;//通过类定义对象
    c1.setR(10);
    cout<<c1.getS(); 
    
    system("pause");
}