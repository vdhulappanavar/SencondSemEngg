int mot1=11, mot2=10,mot3=9,mot4=5, enable1=6,enable2=3;
void setup(){
  //pinMode(6 , OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
  analogWrite(6,255);
  analogWrite(3,255);
}
void loop(){
  
  Serial.println("enter the distance");
  delay(50000);
  int flag=0;
  int dist;
  if(flag==0)
  {
    dist=Serial.read();
    flag=1;
  }
  int c=((dist-5)/20.420352);
  for(int i=0;i<c;i++){
  analogWrite(11,255);
  analogWrite(10,0);
  delay(100);
  analogWrite(11,0);
  delay(100);
  analogWrite(9,255);
  analogWrite(5,0);
  delay(100);
  analogWrite(9,0);
  delay(100);
  }
  analogWrite(11,0);
  analogWrite(10,0);
  analogWrite(5,0);  
  analogWrite(9,225);
}
