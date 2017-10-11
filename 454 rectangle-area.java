public class Rectangle {
    /*
     * Define two public attributes width and height of type int.
     */
    // write your code here
    public int width;
    public int height;

    /*
     * Define a constructor which expects two parameters width and height here.
     */
    // write your code here
    public Rectangle( int x, int y){
        width=x;
        height=y;
    }
    /*
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
     */
     public int getArea(){
        return width*height;
     }
    // write your code here
}
