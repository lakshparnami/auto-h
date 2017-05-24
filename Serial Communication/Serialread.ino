int a[]={1,3,5,6,10,11};
void setup() {
  Serial.begin(9600);
  int i=0;
  for(i=0;i<6;i++);
    pinMode(a[i],OUTPUT);
}
int x=0,k=0;
    int val=0;
  int incomingByte=0;
void loop() {
  
  if(Serial.available() > 0) {
    // read the incoming byte:
    if(x==0)
      {
        incomingByte = Serial.read()-48;
        Serial.print("IB="); 
        Serial.println(incomingByte); 
      }
    
      while(!Serial.available()>0);
      while((Serial.available() > 0)&&x<3)
      {
        x++;
        k=Serial.read()-48;
        val=val*10+k;
        Serial.print("k="); 
        Serial.println(k); 
      }
        Serial.print("val="); 
        Serial.println(val); 
        analogWrite(a[incomingByte],val);
      if(x>=3)
    {
      x=0;k=0;val=0;
    }
  }
}
