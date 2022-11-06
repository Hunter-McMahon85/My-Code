
#include <stdio.h>
#include <stdlib.h>

/* Place your struct definitions for Circle, Triangle, and Rectangle here */
typedef struct {
	double radius;
	double originx;
	double originy;

} Circle;

typedef struct {
	double maxy;
	double maxx;
	double miny;
	double minx;
} Rectangle;

typedef struct {
	double point_y;
	double base_y;
	double base_x1;
	double base_x2;
} Triangle;

typedef struct {
    void *self;
    void (*bbox)(void *s, double *bbox);
    double (*area)(void *s);
    
} Shape;

/* areas */

double GetCircleArea(void * cir)
{
    Circle * circ = (Circle *)cir;
    return 3.14159 * circ->radius * circ->radius;
};

double GetRectangleArea(void * rec)
{
    Rectangle * rect = (Rectangle *) rec;
    return (rect->maxy - rect->miny) * (rect->maxx - rect->minx);
};

double GetTriangleArea(void * try)
{
    Triangle * tri = (Triangle *) try;
    return .5 * (tri->base_x2 - tri->base_x1) * (tri->point_y - tri->base_y);
};

/* bounding boxes */
/*
 * bbox[0] = min x of bounding box
 * bbox[1] = max x of bounding box
 * bbox[2] = min y of bounding box
 * bbox[3] = max y of bounding box
 */

void GetCircleBoundingBox(void * cir, double * bbox)
{   
    Circle * circ = (Circle *)cir;
    bbox[0] = circ->originx - circ->radius;
    bbox[1] = circ->originx + circ->radius;
    bbox[2] = circ->originy - circ->radius;
    bbox[3] = circ->originy + circ->radius;
};

void GetRectangleBoundingBox(void * rec, double * bbox)
{   
    Rectangle * rect = (Rectangle *) rec;
    bbox[0] = rect->minx;
    bbox[1] = rect->maxx;
    bbox[2] = rect->miny;
    bbox[3] = rect->maxy;
};

void GetTriangleBoundingBox(void * try, double * bbox)
{
    Triangle * tri = (Triangle *) try;
    bbox[0] = tri->base_x1;
    bbox[1] = tri->base_x2;
    bbox[2] = tri->base_y;
    bbox[3] = tri->point_y;
};

/* initialize functions */
Shape * CreateCircle(double radius, double originX, double originY)
{   
    Circle *circ = malloc(sizeof(Circle));
	circ->radius = radius;
	circ->originx = originX;
	circ->originy = originY;
    Shape *f = malloc(sizeof(Shape));
    f->self = circ;
    f->area = GetCircleArea;
    f->bbox = GetCircleBoundingBox;
    return f;
};

Shape * CreateRectangle(double minX, double maxX, double minY, double maxY)
{   
    Rectangle *rect = malloc(sizeof(Rectangle));
	rect->maxy = maxY;
	rect->maxx = maxX;
	rect->miny = minY;
	rect->minx = minX;
    Shape *f = malloc(sizeof(Shape));
    f->self = rect;
    f->area = GetRectangleArea;
    f->bbox = GetRectangleBoundingBox;
    return f;
};

Shape * CreateTriangle(double pt1X, double pt2X, double minY, double maxY)
{   
    Triangle *tri = malloc(sizeof(Triangle));
	tri->point_y = maxY;
	tri->base_y= minY;
	tri->base_x1= pt1X;
	tri->base_x2= pt2X;
    Shape *f = malloc(sizeof(Shape));
    f->self = tri;
    f->area = GetTriangleArea;
    f->bbox = GetTriangleBoundingBox;
    return f;
};

double GetArea(Shape *s){
    return s->area(s->self);
};

void GetBoundingBox(Shape *s, double *bbox){
    return s->bbox(s->self, bbox);
};

/* NEW MAIN */
/* DO NOT MODIFY AFTER THIS POINT */
/* note i added a free statement to free our memory when done */

int main()
{
    Shape *shapes[9];
    int    i;
    shapes[0] = CreateCircle(1, 0, 0);
    shapes[1] = CreateCircle(1.5, 6, 8);
    shapes[2] = CreateCircle(0.5, -3, 4);

    shapes[3] = CreateRectangle(0, 1, 0, 1);
    shapes[4] = CreateRectangle(1, 1.1, 10, 20);
    shapes[5] = CreateRectangle(1.5, 3.5, 10, 12);

    shapes[6] = CreateTriangle(0, 1, 0, 1);
    shapes[7] = CreateTriangle(0, 1, 0, 0.1);
    shapes[8] = CreateTriangle(0, 10, 0, 50);

    for (i = 0 ; i < 9 ; i++)
    {
        double bbox[4];
        printf("Shape %d\n", i);
        printf("\tArea: %f\n", GetArea(shapes[i]));
        GetBoundingBox(shapes[i], bbox);
        printf("\tBbox: %f-%f, %f-%f\n", bbox[0], bbox[1], bbox[2], bbox[3]);
    }
    free;
}
