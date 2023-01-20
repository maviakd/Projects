
void OnStart(){
   
   
   /*
   https://book.mql4.com/basics/common       Main Learning Site
   https://book.mql4.com/trading/ordersend   
   
   int declare;                              Declaring a variable
   
   Date Types
   int one = 1;
   double one = 1.123;
   bool one = true;
   bool one = True;
   string one = "Hello";
   color one = 0xFF3300;
   datetime one = D'1.05.2020 16:30:45'      Jan fifth 2020 @ 4:30:45 pm
   datetime Compile = D'';                   Equivilant of D'[Compilation date] 00:00:00'
   
   ||    NOT
   &&    AND
   !     NOT             
   
   
   int one;
   switch(one){
   case 1: one == 1;
      break;
   case 2: one == 2;
      break;
   }
   
   for (int one = 1; one < 3; one++){
   Print("Hello World");       
   }
   
   if (one == 1){
   Print("It is one");       
   
   else Print("It is not one")
   
   ------------------------------------------------------------------------------------
   ***                                 Necessary   
   
   OrderSend()                         Returns a ticket(Unique Number of an Order assigned by server). Returns -1 if trade has been Rejected
   GetLastError                        Provides more information of most recent error(Trade)
   Symbol = &quot;EURGBP&quot;;        Specifies pair. *** to know where to place trades
   volume                              is the amount of lots
   price                               open price. *** to know what the ask/action price is
   stoploss                            Stop loss
   takeprofit                          Take profit
   expiration                          Date when trade expires
   cmd                                 Opens type of trade. *** to know what type of order to make (BUY/SELL)
   
   OrderSend(Symbol(),OP_BUY,0.1,Ask,2,Bid-15*Point,Bid+15*Point);
   return;  
   
   
   */
   
   OrderSend(Symbol(),OP_BUY,0.1,Ask,2,Bid-15*Point,Bid+15*Point);
   return;  
   Alert("Order Made");
   Alert(GetLastError());
   
  }

