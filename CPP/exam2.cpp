/*--- LQueue.cpp ----------------------------------------------------------
             This file implements LQueue member functions.
-------------------------------------------------------------------------*/

#include <new>
using namespace std;
//--- Definition of Queue constructor
Queue::Queue()
{
    myFront =0;
    myBack =0;
}

//--- Definition of Queue copy constructor
Queue::Queue(Queue & original)
{
myFront = myBack = 0;
   if (!original.empty())
   {
      // Copy first node
      myFront = myBack = new Queue::Node(original.front());

      // Set pointer to run through original's linked list
 
      NodePointer orgptr = original.myFront->next;
      
	  while (orgptr != 0)
{
         myBack->next = new Queue::Node(orgptr->data);
         myBack = myBack->next;
         orgptr = orgptr->next;
}
}
}


//--- Definition of Queue destructor
Queue::~Queue()
{
  // Set pointer to run through the queue
  Queue::NodePointer prev = myFront, ptr;
  while (prev != 0)
    {
      ptr = prev->next;
      delete prev;
      prev = ptr;
}
}


//--- Definition of empty()
bool Queue::empty()
{
    return (myFront == 0);
}

//--- Definition of enqueue()
void Queue::enqueue(QueueElement value)
{
NodePointer newptr = new Queue::Node(value);
if (empty())
myFront = myBack = newptr;
else
{
myBack->next = newptr;
myBack = newptr;
}
}

//--- Definition of display()
void Queue::display()
{
Queue::NodePointer ptr;

for (ptr = myFront; ptr!=0; ptr = ptr->next)

cout << ptr->data << "";
cout << endl;
}
//--- Definition of front()
QueueElement Queue::front()
{
    if (!empty())
        return (myFront->data);
    else
    {
        cerr <<"Queue is empty"
               "returning garbage \n";
        QueueElement * temp = new(QueueElement);
        QueueElement garbage = *temp;
        delete temp;
        return garbage;
    }
    }
}

//--- Definition of dequeue()
void Queue::dequeue()
{
if (!empty())
{
Queue::NodePointer ptr = myFront;
myFront = myFront->next;
delete ptr;
if (myFront ==0)
myBack =0;
}
else
cerr<< "The que is empty" <<;
}
