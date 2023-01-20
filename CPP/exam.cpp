/*--- LQueue.cpp ----------------------------------------------------------
             This file implements LQueue member functions.
-------------------------------------------------------------------------*/

#include <new>
using namespace std;

//--- Definition of Queue constructor
Queue::Queue()
{
	Queue::NodePointer prev= myFront, ptr;

	while (prev != 0)
	{
		ptr= prev-> next;
		delete prev;
		prev = ptr;
	}
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
      NodePointer origPtr = original.myFront->next;
      while (origPtr != 0)
      {
         myBack->next = new Queue::Node(origPtr->data);
         myBack = myBack->next;
         origPtr = origPtr->next;
      }
   }
}


//--- Definition of Queue destructor
Queue::~Queue()
{
  // Set pointer to run through the queue
  Queue::NodePointer prev = myFront,
                     ptr;
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
	return (myFront==0);
 }

//--- Definition of enqueue()
void Queue::enqueue(QueueElement value)
{
	NodePointer newptr = new Queue::Node(value);

	if(empty())
		myFront=myBack=newptr;
	else
	{
		myFront->next=newptr;
		myBack= newptr;

	}
}

//--- Definition of display()
void Queue::display()
{
	while(head != NULL)
	cout<<head;

}



//--- Definition of front()
QueueElement Queue::front()
{
	myFront->value;
}

//--- Definition of dequeue()
void Queue::dequeue()
{
	if(!empty())
	{
		Queue::nodepointer ptr=myFront;
		myFront= myFront-> next;
		delete ptr;
	}

	if(myFront==0)
		myFront==0;
}

